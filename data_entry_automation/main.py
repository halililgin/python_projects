from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSdyRlYDIw4XtavN_0iWyi4az3fBd_IgQ1I1OyXHTqt4VjH8lw/viewform?usp=sf_link"
LINKS_SOURCE = "https://appbrewery.github.io/Zillow-Clone/"
ADDRESS_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
PRICE_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
LINK_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
SUBMIT_BUTTON_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'


class DataEntry:
    def __init__(self):
        self.data_source_markup = ""
        self.links = []
        self.prices = []
        self.addresses = []

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.get_listing_details()

    def get_listing_details(self):
        data_source_markup = requests.get(url=LINKS_SOURCE).text

        data_source_soup = BeautifulSoup(markup=data_source_markup, features="html.parser")

        listings = data_source_soup.select(".List-c11n-8-84-3-photo-cards li")

        for listing in listings:
            try:
                url = listing.find(name="a", class_="property-card-link").get("href")
                price = listing.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").text
                address = listing.find(name="address").text

                self.links.append(url)
                self.prices.append(self.clean_price(price))
                self.addresses.append(self.clean_address(address))

            except AttributeError as e:
              pass

    def clean_price(self, price: str):
        symbol_pos = False
        symbols = ""

        for letter in price:
            if letter in ['+', '/']:
                symbol_pos = True

            if symbol_pos:
                symbols += letter

        return price.replace(symbols, "")

    def clean_address(self, address: str):
        return address.replace("|", "").strip()

    def enter_data(self):
        form_driver = webdriver.Chrome(self.chrome_options)

        form_driver.get(FORM_LINK)

        for n in range(len(self.addresses)):

            address_field = form_driver.find_element(By.XPATH, ADDRESS_XPATH)
            price_field = form_driver.find_element(By.XPATH, PRICE_XPATH)
            link_field = form_driver.find_element(By.XPATH, LINK_XPATH)

            address_field.send_keys(self.addresses[n])
            price_field.send_keys(self.prices[n])
            link_field.send_keys(self.links[n])

            form_driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH).click()

            form_driver.find_element(By.LINK_TEXT, "Submit another response").click()


data_entry = DataEntry()
data_entry.enter_data()

