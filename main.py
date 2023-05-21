import csv
import os
from bs4 import BeautifulSoup
import requests
url_list = open('URL.txt', 'r', encoding='utf-8')
os.makedirs('scrapped', exist_ok=True)
os.chdir('scrapped')
directory_main = os.getcwd()
for a in url_list:
    URL_TEMPLATE = a.rstrip()
    request = requests.get(URL_TEMPLATE)
    soup = BeautifulSoup(request.text, "html.parser")
    header = soup.find("h1").text
    header = header.replace('/', '')
    os.makedirs(header, exist_ok=True)  # создание папки
    os.chdir(header)  # заходим в папку

    link = soup.find(
        "section", class_="jsx-3159969563 duplicate-panel-container")
    link = link.find('a')
    link = link.get('href')
    if "https://" not in link:
        link = f"https://www.notion.so{link}"

    os_link = open("Purchase template", "w")
    os_link.write(link)
    os_link.close()

    tags = soup.find_all("section", class_="meta-tag")
    tags_list = []
    for j in tags:
        tags_list.append(j.text)
    with open('CATEGORIES.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            tags_list
        )

    description = soup.find('article', class_="rich-text")
    description = description.find('p')

    os_description = open(f"{header}.txt", "w")
    for n in description:
        os_description.write(str(n))
    os_description.close()

    os.chdir(directory_main)  # возврат в основную директорию
