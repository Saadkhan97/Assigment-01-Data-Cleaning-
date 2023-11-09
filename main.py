import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://onlinebeautyessentials.com/search?q=MAC+Bestsellers&options%5Bprefix%5D=last"

# Send an HTTP GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    product_elements = soup.find_all("div", class_="card-wrapper product-card-wrapper underline-links-hover")
    print(len(product_elements))
    data = []

    for product in product_elements:
        title = product.find("a", class_="full-unstyled-link")
        price = product.find("span",class_="price-item price-item--sale price-item--last")
        product_link = "https://onlinebeautyessentials.com"+title["href"]

        # Extract the text from title and price elements
        title_text = title.text.strip()
        price_text = price.text.strip()

        # Append data to the list
        data.append([title_text, price_text, product_link, "onlinebeautyessentials.com"])

        # Save the data to a CSV file
        with open("products.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)


            csv_writer.writerow(["Title", "Price", "Product Link", "Source Website"])
            csv_writer.writerows(data)

            print("Data scraped and saved to products.csv.")

