import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.ptt.cc/bbs/NBA/index.html"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("div", class_="r-ent")

data_list = []
for a in articles:
    data = {}
    title = a.find("div", class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "no found title"
    data["title"] = title
    popular = a.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    data["popular"] = popular
    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["date"] = date
    data_list.append(data)
df = pd.DataFrame(data_list)
df.to_excel("ptt_nba.xlsx", index=False, engine="openpyxl")


# with open("ptt_nba_data.json", "w", encoding="utf-8") as file:
#     json.dump(data_list, file, ensure_ascii=False, indent=4)
# print("success in json")

    # print(f"title:{title} popular:{popular} date:{date}")
# if response.status_code == 200:#如果回傳值為200表示有爬到正確網站
#     with open('output.html', 'w', encoding='utf-8') as f:
#         f.write(response.text)
#     print("success!")
# else:
#     print("failed")
# print(response.text)

