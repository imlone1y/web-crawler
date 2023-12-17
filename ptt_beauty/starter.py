import requests
from bs4 import BeautifulSoup
import os

def download_img(url, save_path):
    print(f"downloading image: {url}")
    response = requests.get(url)
    with open(save_path, "wb") as file:# b represent of binary
        file.write(response.content)
    print("-" * 30)



def main():
    url = "https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html"

    headers = {"Cookie": "over18=1"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    spans = soup.find_all("span", class_="article-meta-value")
    title = (spans[2].text)
    dir_name = f"images/{title}"

    # make dir
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # find all images in websites
    links = soup.find_all("a")
    allow_file_name = ["jpg", "peg", "jpeg", "gif"]
    for link in links:
        href = link.get("href")
        if not href:
            continue
        file_name = href.split("/")[-1]
        extension = href.split(".")[-1].lower()
        # print(extension)
        if extension in allow_file_name:
            print(f"file format: {extension}")
            print(f"url: {href}")
            download_img(href, f"{dir_name}/{file_name}")

        # print(href)

    # if its image, download
if __name__ == "__main__":
    main()