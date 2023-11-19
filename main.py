import requests
from bs4 import BeautifulSoup
import lxml
import openpyxl


book = openpyxl.Workbook()
sheet1 = book.active


sheet1["A1"] = "Title"
sheet1["B1"] = "Reviews"
sheet1["C1"] = "Price"


user = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
header = {"User-Agent": user}
session = requests.Session()


count = 2


with open("tvs.txt", "a", encoding="utf-8") as file:
    for j in range(1, 26):
        print(f"Page = {j}")
        url = f"https://allo.ua/ua/televizory//p-={j}"
        response = session.get(url, headers=header)


        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            all_products = soup.find_all("div", class_="product-card")


            for product in all_products:
                    title = product.find("a", class_="product-card__title")
                    review = product.find("span", class_="comments-preview__count")
                    price = product.find("span", class_="sum")


                    print(title.text, review, price.text)
                    file.write(f"{title.text} {review} {price.text}\n")
                    sheet1[f"A{count}"] = title.text
                    sheet1[f"B{count}"] = review
                    sheet1[f"C{count}"] = price.text
                    count += 1


            book.save("tvs.xlsx")
            book.close()