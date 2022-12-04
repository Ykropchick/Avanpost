import os
import shutil

from django.conf import settings
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CategoryModel, PhotoModel
from .serializers import CategorySerializer, PhotoSerializer
from icrawler.builtin import GoogleImageCrawler

# import torch
# import clip
from PIL import Image

host_url = "https://web-production-0241.up.railway.app"

# device = "cuda" if torch.cuda.is_available() else "cpu"
# model, preprocess = clip.load("RN50", device=device)
# THRESHOLD = 0.5
# categories = ['snowboard','skateboard','truck','car','train','horse','lawnmower','ski','snowmobile','dump truck', 'van']

def predict_image_from_path(path):
    image = preprocess(Image.open(path)).unsqueeze(0).to(device)
    text = clip.tokenize(categories).to(device)
    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)

        logits_per_image, logits_per_text = model(image, text)
        probs = list(logits_per_image.softmax(dim=-1).cpu().numpy().flatten())
        labels = []
        for i, prob in enumerate(probs):
            if prob >= THRESHOLD:
                labels.append(categories[i])

    return labels


def find_photos(category, num):
    paths = []
    crawl = GoogleImageCrawler(storage={'root_dir': f'../mediafiles/images/{category}'})
    crawl.crawl(keyword=category, max_num=num, filters={'type':"photo"})
    # paths = [f'mediafiles/images/{category}/{f"{i + "0" * }"}' for i in range(0, num + 1)]
    for i in range(1, num + 1):
        path = f'mediafiles/images/{category}/'
        photo = "0" * (6 - len(str(i))) + f"{i}" + ".jpg"
        paths.append(path + photo)

    return paths


@api_view(['POST'])
def start_neuron(request):
    if request.method == "POST":
        image_path = "../mediafiles/images/tests"
        answer_dict = {}
        for filename in os.listdir(image_path):
            if ".jpg" in filename.lower():
                labels = predict_image_from_path(os.path.join(image_path, filename))
                answer_dict['http://127.0.0.1:8000/media/images/tests' + filename] = labels
        print(answer_dict)

        #"trunc.img" : ['trunc']
        try:
            shutil.rmtree(image_path)
        except:
            pass
    return HttpResponse("Ответ нейронки")


@api_view(['GET', 'POST'])
def save_photo(request):
    if request.method == 'GET':
        snippets = PhotoModel.objects.all()
        serializer = PhotoSerializer(snippets, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            imageUrl = request.build_absolute_uri(serializer.data['imageUrl'])
            response = {'imageUrl': imageUrl}
            return Response(response)

    return HttpResponse("Error")


@api_view(['GET', 'POST'])
def take_category(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = CategoryModel.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        for object in serializer.data:
            if object['imageUrl']:
                object['imageUrl'] = request.build_absolute_uri(object['imageUrl'])
        results = {"categories": serializer.data}
        return Response(results)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.validated_data.get('name')

            paths = find_photos(category, 5)
            path = paths[0].replace("mediafiles", "")
            serializer.save(imageUrl=path)
            return Response({"name": serializer.data['name'],
                             'imageUrl': "http://127.0.0.1:8000" + serializer.data['imageUrl']})

    return HttpResponse("ok")




