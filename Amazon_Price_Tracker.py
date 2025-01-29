import requests
from bs4 import BeautifulSoup
import smtplib

# User input for URL and target price
URL = input("Enter the URL of the product: ")
target_price = float(input("Enter your target price (in rupees): "))

HEADERS = {
    "User-Agent": "Search for User Agent in your browser and copy the generated text and paste it out here"
}

# Fetch product details
response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

try:
    name = soup.find('span', attrs={'class': 'a-size-large product-title-word-break'}).get_text().strip()
except AttributeError:
    name = "Product name not found"

try:
    price = soup.find('span', attrs={'class': 'a-price-whole'}).get_text().strip().replace(',', '')
    current_price = float(price)
except (AttributeError, ValueError):
    current_price = None

try:
    availability = soup.find(id='availability').get_text().strip()
except AttributeError:
    availability = "Availability information not found"

# Check if current price is less than or equal to the target price
if current_price is not None and current_price <= target_price:
    # Compose email
    subject = f"Price Alert: {name} is now {current_price} rupees!"
    body = f"Details:\n{name}\nPrice: {current_price} rupees\nAvailability: {availability}\n\nCheck the product here: {URL}"
    msg = f"Subject: {subject}\n\n{body}"

    # Send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('<EMAIL>', '<the app password that you may generate>')
        server.sendmail('<EMAIL>', '<EMAIL>', msg)
    print('Email has been sent!')
else:
    print(f"No email sent. Current price ({current_price} rupees) is higher than the target price.")