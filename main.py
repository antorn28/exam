import requests
from bs4 import BeautifulSoup
import lxml



user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
header = {"User-Agent": user}
session = requests.Session()


count = 2

with open("tv.txt", "a", encoding="utf=8") as file:
    for i in range(1,26):
        print(f"page = {i}")
        url = "https://allo.ua/ua/televizory/"
        response = session.get(url, headers=header)


    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features = "lxml")

        all_products = soup.find_all(name = "div", class_="product-card")

        print(len(all_products))

        for product in all_products:
            if product.find("div", class_="product-card"):
                price = product.find("span", class_="product-card__title")
                title = product.find("span", class_="v-pb__cur discount")

                file.write(f"{title.text} {price.text}")