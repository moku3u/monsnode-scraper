import requests
from bs4 import BeautifulSoup

def search(page):
    video_urls=[]
    status=[]
    for i in range(page):
        res = requests.get("https://monsnode.com/user/postman080/", data={"page": i})
        html = BeautifulSoup(res.content, "lxml-html")
        url = html.findAll("a",  attrs={"rel": "nofollow"})
        url = [u.get("href") for u in url if "https://monsnode.com/redirect.php" in u.get("href")]
        [video_urls.append(u) for u in url]
        status.append(res.status_code)
    return {"status_code": status, "video_url": video_urls}
while True:
    try:
        page = int(input("Number of pages to search(1page: 40 video)\n>> "))
        result = search(page)
        print(result)
        break
    except:
        print("please input count *number only")