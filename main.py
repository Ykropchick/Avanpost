from icrawler.builtin import GoogleImageCrawler


def find_photos(category, num):
    paths = []
    crawl = GoogleImageCrawler(storage={'root_dir': f'/home/kirill/outsource_project/AvanpostHak/mediafiles/images/{category}'})
    crawl.crawl(keyword=category, max_num=num)
    # paths = [f'mediafiles/images/{category}/{f"{i + "0" * }"}' for i in range(0, num + 1)]
    for i in range(1, num + 1):
        path = f'mediafiles/images/{category}/'
        photo = "0" * (6 - len(str(i))) + f"{i}" + ".jpg"
        paths.append(path + photo)

    return paths
