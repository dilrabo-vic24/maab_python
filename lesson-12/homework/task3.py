from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")

driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(3) 

laptops = []

while True:
    products = driver.find_elements(By.CLASS_NAME, "card-title")
    prices = driver.find_elements(By.CLASS_NAME, "card-block")

    for product, price_block in zip(products, prices):
        name = product.text
        price = price_block.find_element(By.TAG_NAME, "h5").text
        description = price_block.find_element(By.TAG_NAME, "p").text
        laptops.append({"name": name, "price": price, "description": description})

    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(3)
    except:
        break 

driver.quit()

with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptops, file, indent=4, ensure_ascii=False)

print("Laptops ma'lumotlari JSON faylga saqlandi.")
