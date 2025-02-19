from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import requests
from selenium.webdriver.edge.service import Service

def get_brand_tags(driver):
    brands_list = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'brands-list'))
    )
    brand_tags = brands_list[0].find_elements(By.TAG_NAME, 'a')
    return brand_tags

def get_occasions_articles(driver):
    occasions_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'occasions-results'))
    )
    articles = occasions_results.find_element(By.CLASS_NAME, 'articles')
    items_list = articles.find_elements(By.CLASS_NAME, 'versions-item')
    return items_list

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



def download_gallery_images( item_dir, model_name, grid_gallery):
    grid_tags = grid_gallery.find_elements(By.TAG_NAME, 'a')
    max_images = 5
    for grid_i, grid_tag in enumerate(grid_tags):
        try:
            grid_img = grid_tag.find_element(By.TAG_NAME, 'img')
            grid_img_url = grid_img.get_attribute('data-src')
            gallery_dir = os.path.join(item_dir, "gallery")
            os.makedirs(gallery_dir, exist_ok=True)
            file_name = os.path.join(gallery_dir, f"{model_name}_{grid_i}.png")
            download_image(grid_img_url, file_name)
            if grid_i == max_images:
                break
        except Exception as e:
            print(f"Error downloading image: {e}")
def scrape_auto_mobile_data():
    base_save_dir = "C:/Bureau/automobile"
    os.makedirs(base_save_dir, exist_ok=True)
    service = Service(executable_path='msedgedriver.exe')
    options = webdriver.EdgeOptions()
    options.page_load_timeout = 10  # Set page load timeout
    options.implicit_wait = 10      # Set implicit wait timeout

    driver = webdriver.Edge(service=service, options=options)

    base_url = "https://www.automobile.tn/fr/neuf#moteur"
    driver.get(base_url)

    brand_tags = get_brand_tags(driver)
    for tag_i in range(len(brand_tags)):
        if tag_i != 0:
        # Refetch brand tags after navigation
            brand_tags = get_brand_tags(driver)
        tag = brand_tags[tag_i]
    
        next_page = tag.get_attribute('href')
        img = tag.find_element(By.TAG_NAME, 'img')
        brand_name = img.get_attribute('alt')
        url_image = img.get_attribute('src')
        item_dir = os.path.join(base_save_dir, f"{brand_name}")
        os.makedirs(item_dir, exist_ok=True)
        file_name = os.path.join(item_dir, f"{brand_name}-logo.png")
        download_image(url_image, file_name)
    
    # Navigate to the next page and handle its content
        driver.get(next_page)
        items_list = get_occasions_articles(driver)
    
        for item_i in range(len(items_list)):
            try:
                if item_i != 0:
                # Refetch items list after potential navigation
                    items_list = get_occasions_articles(driver)
                if item_i > 8 :
                    break
                item = items_list[item_i]
            
                tag_a = item.find_element(By.TAG_NAME, 'a')
                next_page_new = tag_a.get_attribute('href')
                img_a = tag_a.find_element(By.TAG_NAME, 'img')
                model_name = img_a.get_attribute('alt')
                img_url = img_a.get_attribute('src')
                price = ''.join(filter(str.isdigit, item.find_element(By.CLASS_NAME, 'price').text.strip()))
                item_dir = os.path.join(base_save_dir, f"{brand_name}/{model_name},{price}DT")
                os.makedirs(item_dir, exist_ok=True)
                file_name = os.path.join(item_dir, f"{model_name}.png")
                download_image(img_url, file_name)
            
                driver.get(next_page_new)
                time.sleep(3)
                try:
                    grid_gallery = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'grid-gallery'))
                )
                except Exception as e:
                    print(f"No grid-gallery found for {model_name}")
                    driver.back()
                    continue
                if(grid_gallery!=None):
                   download_gallery_images(item_dir, model_name, grid_gallery)
                   driver.back()
                else:
                    print(f"No grid-gallery found for {model_name}")
            

            except Exception as e:
                print(f"Error extracting item details: {e}")

        time.sleep(3)
        driver.back()
    
    driver.quit()
    print("Process completed successfully")

