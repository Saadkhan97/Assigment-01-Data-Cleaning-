import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://www.lookfantastic.com/health-beauty/make-up/lips/lipsticks.list?autocomplete=searchsuggestion"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    product_elements = soup.find_all("li", class_="productListProducts_product")
    print(len(product_elements))
    data = []

    for product in product_elements:
        link = product.find("a", class_="productBlock_link")
        title = product.find("h3", class_="productBlock_productName")
        price = product.find("span",class_="productBlock_priceValue")
        product_link = 'https://www.lookfantastic.com'+link["href"]

        # Extract the text from title and price elements
        title_text = title.text.strip()
        price_text = price.text.strip()

        # Append data to the list
        data.append([title_text, price_text, product_link, "www.lookfantastic.com"])

        # Save the data to a CSV file
        with open("products2.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)


            csv_writer.writerow(["Title", "Price", "Product Link", "Source Website"])
            csv_writer.writerows(data)

            print("Data scraped and saved to products.csv.")

