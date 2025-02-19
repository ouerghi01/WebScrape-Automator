from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.edge.service import Service


import requests

service = Service(executable_path='msedgedriver.exe')
options = webdriver.EdgeOptions()
options.page_load_timeout = 10  # Set page load timeout
options.implicit_wait = 10      # Set implicit wait timeout

driver = webdriver.Edge(service=service, options=options)
base_url = "https://techmarket.co.uk/collections/"
products = [ "iphones","ipods", "ipads", "airpods", "apple-pencil", "apple-watch", "accessories", "clearance", "mac", "samsung", "cheap-laptop-deals"]

base_save_dir = "C:/Bureau/mobile"
os.makedirs(base_save_dir, exist_ok=True)
def download_image(image_url, file_name):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Image saved: {file_name}")
        else:
            print(f"Failed to download image: {image_url}")
    except Exception as e:
        print(f"Error downloading image: {e}")
def get_grid_items(driver):
    div_element = driver.find_element(By.CSS_SELECTOR, 'div[data-section-id]')
    market = div_element.find_element(By.CLASS_NAME, 'product-collection')
    grid_items = market.find_elements(By.CSS_SELECTOR, ".grid-item.col-6.col-md-4.col-lg-3")
    return grid_items
def process_product_category(base_url, base_save_dir, product_category):
    driver.implicitly_wait(10)
    new_url = f"{base_url}{product_category}"
    driver.get(new_url)
    
    try:
        grid_items = get_grid_items(driver)
        print(f"Product Category: {product_category} | Items Found: {len(grid_items)}")
        for index in range(len(grid_items)):
            if index != 0:
                grid_items = get_grid_items(driver)
            if index > 8 :
                break
            try:
                item = grid_items[index]
                box = item.find_element(By.CLASS_NAME, "product-bottom")
                title = box.find_element(By.TAG_NAME, 'a').text.strip().replace("/", "-")  # Replace special characters
                price_box = box.find_element(By.CLASS_NAME, 'price-box')
                price = price_box.text.strip().replace(" ", "")
            except Exception as e:
                raise Exception(f"Error extracting item details: {e}")
            item_dir = os.path.join(base_save_dir, f"{title[:12]},{price}")
            os.makedirs(item_dir, exist_ok=True)
            driver.execute_script("arguments[0].scrollIntoView(true);", item)
            item.click()
            main_image = driver.find_element(By.XPATH, "//*[contains(@id, 'product-featured-image-')]")
            image_url_main = main_image.get_attribute("src")
            main_file_name = os.path.join(item_dir, f"main_image.jpg")
            download_image(image_url_main, main_file_name)
            gallery = driver.find_elements(By.CLASS_NAME, "fancybox")
            try:
                i = 1
                while i < len(gallery): 
                    image_url = gallery[i].get_attribute("href")
                    file_name = os.path.join(item_dir, f"image_{i}.jpg")
                    download_image(image_url, file_name)
                    i += 1
            except Exception as e:
                print("No more images in the carousel or error occurred")
            driver.back()
    except Exception as e:
        print(f"Error processing product '{product_category}': {e}")
    finally:
        driver.quit()
def scrap_mobile_products():
    for p in products:
        process_product_category( base_url, base_save_dir, p)

       




