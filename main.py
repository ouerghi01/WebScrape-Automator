from lib.main_mobile import scrap_mobile_products
from lib.main_automobile import scrape_auto_mobile_data
import threading
if __name__ == "__main__":
    t1 = threading.Thread(target=scrap_mobile_products)
    t2 = threading.Thread(target=scrape_auto_mobile_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()