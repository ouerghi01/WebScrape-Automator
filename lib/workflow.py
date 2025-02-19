from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

# Initialize the WebDriver and other settings
service = Service(executable_path='msedgedriver.exe')
options = webdriver.EdgeOptions()
options.page_load_timeout = 10  # Set page load timeout
options.implicit_wait = 10      # Set implicit wait timeout
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Edge(service=service, options=options)
base_url = " https://marketplace-fev14-marketplace.apps.ocp-dev.zitouna.local/#/home/cars"
base_url_1= "https://marketplace-bov7-marketplace.apps.ocp-dev.zitouna.local/#/login"
global marque, marque_desc, model, path_image_marq, version, model_desc, version_desc, version_prix, duration_garantie, query_cap, query_connectivite, query_memoire, query_ram, query_taille, query_processeur, query_systeme, query_appareil, quantite_number, stock_image, stock_desc, clr, type_product


marque = "DRAGONBRANDCEZZZE"
marque_desc = "Brand BRANADCEZZZE description" 
model = "MODELDRAGONBRANDCEZZZE"
version = "versionxcdragon"
model_desc = "Model MODELX description"
version_desc = "Version versionx description"
path_image_marq=r'C:\Users\Ons\WebScrape-Automator\1.png'

version_prix = "1000"
duration_garantie = "2"
query_cap = "3000 mAh"
query_connectivite = "WiFi + 4G"
query_memoire = "8 Go"
query_ram = "4 Go"
query_taille = "6.7 Pouces"
query_processeur = "Snapdragon"
query_systeme = "Android"
query_appareil = "8 MégaPixels"
quantite_number = "10"
stock_image= path_image_marq
stock_desc = "Stock description"
clr="Blanc"
type_product="Smartphone"
email="concessionnaire1@gmail.com"
password="123456789eE"
def perform_login_web1(driver,email="concessionnaire1@gmail.com",password="123456789eE"):
    driver.get(base_url)
    
    time.sleep(10)
    nav = driver.find_element(By.CSS_SELECTOR, '.navbar')
    button_show_login = nav.find_element(By.CSS_SELECTOR, '.th-web-header')
    if "Connexion" in button_show_login.text.strip() :

        ActionChains(driver).move_to_element(nav).click(button_show_login).perform()
        email_input = driver.find_element(By.ID, 'login_email').send_keys(email)
        password_input = driver.find_element(By.ID, 'password').send_keys(password)
        button_ui = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/div/div/div/div/div/div[3]/form[1]/div[5]/button')
        ActionChains(driver).move_to_element(button_ui).click(button_ui).perform()
        current_url = driver.current_url
        return current_url
    else:
        try: 
            ActionChains(driver).move_to_element(button_show_login).click(button_show_login).perform()
            tableau_de_bord = driver.find_element(By.XPATH, '/html/body/app-root/app-principal-home/app-principel-header/header/div/div/div/nav/div[2]/app-settings/div/div[1]/ul/div/li[1]')
            ActionChains(driver).move_to_element(tableau_de_bord).click(tableau_de_bord).perform()
            time.sleep(2)
        except NoSuchElementException:
            print("Element not found, skipping interaction.")
        return driver.current_url
def perform_login_action_web2(driver):
    driver.get(base_url_1)
    time.sleep(5)
    card_body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div/div/div"))  # This is a dummy element
     )
    email_input = card_body.find_element(By.ID, 'login_email')
    email_input.send_keys("commercial@tunistore.tn")
    time.sleep(3)
    password_input = card_body.find_element(By.ID, 'password').send_keys("123456789")
    time.sleep(3)
    button_sigin = card_body.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div/div/div/div/div/form/div[3]/button')
    ActionChains(driver).move_to_element(button_sigin).click(button_sigin).perform()
    time.sleep(3)
    new_url=driver.current_url
    return new_url
def automate_insert_web_interaction(driver: webdriver.Edge,marque, marque_desc, model, path_image_marq, version, model_desc, version_desc, version_prix, duration_garantie, query_cap, query_connectivite, query_memoire, query_ram, query_taille, query_processeur, query_systeme, query_appareil, quantite_number, stock_image, stock_desc, clr, type_product):
    driver.get(base_url)
    
    current_url = perform_login_web1(driver)
    driver.get(current_url)
    time.sleep(3)
    x_path_gestion ="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-contenu-mobile/div[2]/div/div[2]/button"
    navigate_to_content_management(driver, x_path_gestion)

    create_ui = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-marque-mobile/div/div[2]/div/div/div/div/div"))  # This is a dummy element
    )
    marke_cc = create_ui.find_element(By.ID, 'Marquee').send_keys(marque)
    desc = create_ui.find_element(By.ID, 'desc').send_keys(marque_desc)
    input_image = create_ui.find_element(By.ID, 'img2').send_keys(path_image_marq)  # file input
    button_enre = driver.find_element(By.XPATH, '/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-marque-mobile/div/div[2]/div/div/div/div/div/form/div[4]/div/button[1]')
    ActionChains(driver).move_to_element(button_enre).click(button_enre).perform()
    
    time.sleep(5)
    new_url = perform_login_action_web2(driver)
    driver.get(new_url)

    time.sleep(3)
    x_path_marques_mobiles="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[11]/ul/li[3]/ul/li[2]/a/span"

    select_mobile_partners(driver, x_path_marques_mobiles)
    current_url = driver.current_url
    driver.get(current_url)
    
    try:
            content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-marque-mobile-validation/div/div/div/div/div[2]/ngx-datatable"))  # This is a dummy element
            )
            rows = content.find_elements(By.CLASS_NAME, "datatable-body")
            if len(rows) != 0:
              for row in rows:
                mark_name = row.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-marque-mobile-validation/div/div/div/div/div[2]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper/datatable-body-row/div[2]/datatable-body-cell[3]/div/span")
                if mark_name.text == marque:
                   validate = row.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-marque-mobile-validation/div/div/div/div/div[2]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper/datatable-body-row/div[2]/datatable-body-cell[5]/div/div/button[2]")
                   ActionChains(driver).move_to_element(validate).click(validate).perform()
                   break
    except TimeoutException:
            print("Table not found, skipping interaction.")
    new_url = perform_login_web1(driver)
    driver.get(new_url)
    time.sleep(2)
    x_path_gestion_model="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-contenu-mobile/div[2]/div/div[3]/button"
    navigate_to_content_management(driver, x_path_gestion_model)
    marques_mobiles = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, 
                                        "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-modele-mobile/div/div[2]/div/div/div/div/div/form/div[1]/div/ng-select/div/div/div[2]"
        ))  # This is a dummy element
    )
    ActionChains(driver).move_to_element(marques_mobiles).click(marques_mobiles).perform()
    time.sleep(1)
    caracterestique_x=driver.find_element(By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-modele-mobile/div/div[2]/div/div/div/div/div/form")
    id_marque = 'marque'
    marque_path="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-modele-mobile/div/div[2]/div/div/div/div/div/form/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique_x, id_marque, marque_path, marque)
    model_c = caracterestique_x.find_element(By.ID, 'Modele')
    model_c.send_keys(model)
    desc = driver.find_element(By.ID, 'Description')
    desc.send_keys(model_desc)
    button_enre = driver.find_element(By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-modele-mobile/div/div[2]/div/div/div/div/div/form/div[4]/button[1]")
    ActionChains(driver).move_to_element(button_enre).click(button_enre).perform()
    time.sleep(3)
    new_url = perform_login_action_web2(driver)
    x_path_models="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[11]/ul/li[3]/ul/li[3]/a/span"
    select_mobile_partners(driver, x_path_models, "MODELX")
    current_url = driver.current_url
    driver.get(current_url)
    content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-model-mobile-validation/div/div/div/div[2]/ngx-datatable")))
    table = content.find_element(By.CLASS_NAME, "datatable-body")
    rows= table.find_elements(By.CLASS_NAME, "datatable-row-wrapper")
    validate = False
    if len(rows) != 0:
        for row in rows:
            model_name = row.find_elements(By.CLASS_NAME, "datatable-body-cell")[2]
            if model_name.text == model:
                validate = row.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-model-mobile-validation/div/div/div/div[2]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[1]/datatable-body-row/div[2]/datatable-body-cell[5]/div/div/button[2]")
                ActionChains(driver).move_to_element(validate).click(validate).perform()
                validate = True
                break
    if validate:
        validate_box=  driver.find_element(By.XPATH,"/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-validation-detail-modele-mobile/div/div/div/div[3]/div/div[2]/div[1]/div/div[1]/label")
        ActionChains(driver).move_to_element(validate_box).click(validate_box).perform()
        validate_button = driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-validation-detail-modele-mobile/div/div/div/div[3]/div/div[2]/div[2]/button")
        ActionChains(driver).move_to_element(validate_button).click(validate_button).perform()
        time.sleep(3)
    validate_product_stock(driver, marque, model, version, quantite_number, stock_image, stock_desc, clr, type_product, current_url)
    new_url = perform_login_action_web2(driver)
    x_path_models="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[11]/ul/li[3]/ul/li[5]/a/span"
    select_mobile_partners(driver, x_path_models, "MODELX")
    content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-model-mobile-validation/div/div/div/div[2]/ngx-datatable")))
    table = content.find_element(By.CLASS_NAME, "datatable-body")
    rows= table.find_elements(By.CLASS_NAME, "datatable-row-wrapper")
    v = False
    if len(rows) != 0:
        for row in rows:
            if model in row.text:
                validate = driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-version-mobile-validation/div/div/div/div/div/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[1]/datatable-body-row/div[2]/datatable-body-cell[6]/div/div/button[1]")
                ActionChains(driver).move_to_element(validate).click(validate).perform()
                v = True
                break
    if v:
        validate_box=  driver.find_element(By.XPATH,"/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-validation-detail-modele-mobile/div/div/div/div[3]/div/div[2]/div[1]/div/div[1]/label")
        ActionChains(driver).move_to_element(validate_box).click(validate_box).perform()
        validate_button = driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-validation-detail-modele-mobile/div/div/div/div[3]/div/div[2]/div[2]/button")
        ActionChains(driver).move_to_element(validate_button).click(validate_button).perform()
        time.sleep(3)

def validate_product_stock(driver, marque, model, version, quantite_number, stock_image, stock_desc, clr, type_product, current_url):
    create_and_validate_version(driver, current_url)
    perform_login_web1(driver)
    time.sleep(1)
    stock_path = "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[1]/div[2]/div[2]/ul/a[6]"
    navigate_to_content_management(driver, stock_path)
    stokes_mobiles = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, 
                                        "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-gestion-stock-mobile/section/div[2]/div/div[1]"
        ))  # This is a dummy element
    )
    ActionChains(driver).move_to_element(stokes_mobiles).click(stokes_mobiles).perform()
    time.sleep(1)
    caracterestique = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-stock-mobile/div/div[2]/div/div/div")))
    
    idTypeMobile="idTypeMobile"
    path_TypeMobile="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-stock-mobile/div/div[2]/div/div/div/form/div[1]/div/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, idTypeMobile, path_TypeMobile, type_product)
    marqueMobile="marqueMobile"
    path_marqueMobile="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-stock-mobile/div/div[2]/div/div/div/form/div[2]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, marqueMobile, path_marqueMobile, marque)
    modeleMobile="modeleMobile"
    path_modeleMobile="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-stock-mobile/div/div[2]/div/div/div/form/div[2]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, modeleMobile, path_modeleMobile, model)
    idVersionMobile="idVersion"
    path_versionMobile="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-stock-mobile/div/div[2]/div/div/div/form/div[3]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, idVersionMobile, path_versionMobile, version)
    idCouleur="idCouleur"
    couleur_path ="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-stock-mobile/div/div[2]/div/div/div/form/div[3]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, idCouleur, couleur_path, clr)
    quantite = driver.find_element(By.XPATH, '/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-stock-mobile/div/div[2]/div/div/div/form/div[4]/div[1]/input')
    quantite.send_keys(quantite_number)
    Description = caracterestique.find_element(By.ID, 'Description')
    Description.send_keys(stock_desc)
    img2=caracterestique.find_element(By.ID, 'img2')
    img2.send_keys(stock_image)
    button_enre = driver.find_element(By.XPATH, '/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-stock-mobile/div/div[2]/div/div/div/form/div[6]/div/button[1]')
    ActionChains(driver).move_to_element(button_enre).click(button_enre).perform()
    # got to backoffice and validate the stock
def create_and_validate_version(driver, current_url):
    create_new_version(driver)
    version_mobile="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[11]/ul/li[3]/ul/li[4]/a/span"
    perform_login_action_web2(driver)
    select_mobile_partners(driver, version_mobile, "TESTVERSION")
    
    try:    
            time.sleep(3)
            content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-version-mobile-validation/div/div/div/div/div/div/ngx-datatable")))
            table = content.find_element(By.CLASS_NAME, "datatable-body")
            rows=table.find_elements(By.CLASS_NAME, "datatable-row-wrapper")
            v = False
            if len(rows) != 0:
              for row in rows:
                if model in row.text:
                   validate = driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-version-mobile-validation/div/div/div/div/div/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[1]/datatable-body-row/div[2]/datatable-body-cell[6]/div/div/button[1]")
                   ActionChains(driver).move_to_element(validate).click(validate).perform()
                   v = True
                   break
            if v:
                check=driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-details-version-mobile/section[2]/div[2]/div/div[2]/div[1]/div/div[1]")
                ActionChains(driver).move_to_element(check).click(check).perform()
                buuu=driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-details-version-mobile/section[2]/div[2]/div/div[2]/div[3]/button")
                ActionChains(driver).move_to_element(buuu).click(buuu).perform()
    except TimeoutException:
            print("Table not found, skipping interaction.")

def create_new_version(driver):
    perform_login_web1(driver)
    version_path = "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[1]/div[2]/div[2]/ul/a[5]/li/div/div/span"
    navigate_to_content_management(driver, version_path)
    nav_version = driver.find_element(By.CSS_SELECTOR, "div.mb-20:nth-child(2)")
    add_version = nav_version.find_element(By.CLASS_NAME, "addVersion")
    ActionChains(driver).move_to_element(add_version).click(add_version).perform()
    nav_caracteristiques = driver.find_element(By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/ul")
    caracteristiques = nav_caracteristiques.find_elements(By.CLASS_NAME, "nav-item")
    for i,caracteristique in enumerate(caracteristiques):
        if i == 0:
          fill_version_form(driver, caracteristique,model)
        if i == 1:
          populate_device_specs(driver, caracteristique)
        if i == 2:
            ActionChains(driver).move_to_element(caracteristique).click(caracteristique).perform()
            button_en = driver.find_element(By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/div/div[2]/button")
            time.sleep(1)
            ActionChains(driver).move_to_element(button_en).click(button_en).perform()
            time.sleep(3)

def populate_device_specs(driver, caracteristique):
    id_cap= "idCapaciteBatterie"
    path="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/div/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
    
    select_parametre(driver, caracteristique, id_cap, path, query_cap)
    idConnectivite="idConnectivite"
    path_connectivite="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]"
    
    select_parametre(driver, caracteristique, idConnectivite, path_connectivite, query_connectivite)
    idMemoire="idMemoire"
    
    path_memoire="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/div/div[3]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracteristique, idMemoire, path_memoire, query_memoire)
    idRam="idRam"
    ram_path="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/div/div[5]/div/ng-select/ng-dropdown-panel/div/div[2]"
    
    select_parametre(driver, caracteristique, idRam, ram_path, query_ram)
    idTailleEcran="idTailleEcran"
    taille_path="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/div/div[7]/div/ng-select/ng-dropdown-panel/div/div[2]"
    
    select_parametre(driver, caracteristique, idTailleEcran, taille_path, query_taille)
    idProcesseur="idProcesseur"
    processeur_path="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/div/div[4]/div/ng-select/ng-dropdown-panel/div/div[2]"
   
    select_parametre(driver, caracteristique, idProcesseur, processeur_path, query_processeur)
    idSystemeExploitation="idSystemeExploitation"
    systeme_path="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/div/div[6]/div/ng-select/ng-dropdown-panel/div/div[2]"
    
    select_parametre(driver, caracteristique, idSystemeExploitation, systeme_path, query_systeme)
    idAppareilPhoto="idAppareilPhoto"
    appareil_path="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/div/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]"
    
    select_parametre(driver, caracteristique, idAppareilPhoto, appareil_path, query_appareil)


def select_parametre(driver, caracteristique, id, path, query_cap):
    ActionChains(driver).move_to_element(caracteristique).click(caracteristique).perform()
    capacite = driver.find_element(By.ID, id)
    time.sleep(2)
    ActionChains(driver).move_to_element(capacite).click(capacite).perform()
    capacite_content=driver.find_element(By.XPATH,path)
    for content in capacite_content.find_elements(By.TAG_NAME, "div"):
        if query_cap.strip() in content.text.strip():
            ActionChains(driver).move_to_element(content).click(content).perform()
            break
def fill_version_form(driver, caracteristique,model):
    ActionChains(driver).move_to_element(caracteristique).click(caracteristique).perform()
    id_marque="marque"
    marque_path="/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/form/div/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracteristique, id_marque, marque_path, marque)
  
    inputs_container = driver.find_element(By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/form")
    nom = inputs_container.find_element(By.ID, 'nom')
    nom.send_keys(version)
    desc = inputs_container.find_element(By.ID, 'desc')
    desc.send_keys(version_desc)
    
    models = driver.find_element(By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/form/div/div[2]/div/ng-select")
    ActionChains(driver).move_to_element(models).click(models).perform()
    list_models = models.find_elements(By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/form/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]")
    for model_n in list_models:
        print(model_n.text)
        if model in model_n.text:
           ActionChains(driver).move_to_element(model_n).click(model_n).perform()
           break
    prix_version = driver.find_element(By.ID, 'prixVersion')
    prix_version.send_keys(version_prix)
    garantie = driver.find_element(By.XPATH, '/html/body/app-root/app-partner-mobile/section/div/div[1]/div[2]/div/app-ajouter-version-mobile/section/section/div/div/form/div/div/section/div/form/div/div[6]/label/span')
    ActionChains(driver).move_to_element(garantie).click(garantie).perform()
    duration = inputs_container.find_element(By.ID, 'dureeGanrantie')
    duration.send_keys(duration_garantie)


            

    
def select_mobile_partners(driver, x_path_marques_mobiles,name="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[11]/a/span",name2="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[11]/ul/li[3]/a/span"):
    side_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[11]/a/span"))  # This is a dummy element
     )
    partenaires_mobiles= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, name))  # This is a dummy element
     )
    

    ActionChains(driver).move_to_element(side_bar).click(partenaires_mobiles).perform()
    validation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, name2))  # This is a dummy element
     )
    driver.execute_script("arguments[0].scrollIntoView(true);", validation)
    ActionChains(driver).move_to_element(side_bar).click(validation).perform()
    marques_mobiles = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, x_path_marques_mobiles))  # This is a dummy element
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", marques_mobiles)
    ActionChains(driver).move_to_element(side_bar).click(marques_mobiles).perform()
    
    


def navigate_to_content_management(driver, x_path_gestion):
    time.sleep(2)
    gestion_contenu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-partner-mobile/section/div/div[1]/div[1]/div[2]/div[2]/ul/a[7]/li/div/div/span"))  # This is a dummy element
    )
    ActionChains(driver).move_to_element(gestion_contenu).click(gestion_contenu).perform()
    gestion_mark = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, x_path_gestion))  # This is a dummy element
    )
    ActionChains(driver).move_to_element(gestion_mark).click(gestion_mark).perform()
## Main AutoMobile Partner ##
model ="MODELXDRAGON"
marque_v="BRANADCEDRAZZZE"
version="versionzxx"
nbreRapport=4
nbrePlaceVersion=4

query_carross="SUV"
prix="10000"
nbrePorteVer="4"
query_carburon="Essence"
query_puissance="23"
duration    ="2"
couplenmVr="4"
cylindre_v="4"
nbreCylindreVer="4"
couplenVr="4"
query_pui="23"
boite_name="Automatique"
longueurPd="4"
Traction="Traction"
largeurPrd="4"
hauteurPod="4"
volumeoffre="4"
Performanceetconsommation=["4","4","4","4","4","4" ]
one="ABS"
two= "Frontaux"
three="BMW Professional CD"
xz_t="Velours"
xz_y="Pour vitres de portes arrières"
xzx=[xz_t,xz_y]
lumierAmbiance_value="5"
sellerie_value="Cuir"
Finitionintérieure="Bois"
Siege="Réglage lombaire"
volant="Cuir"
kit="Kit fumeurs"
kit_1="Kit de réparation"
Accoudoirs="Avant"
feu_value="Feux de jour"
phare_value="LED"
radar_v="Avant"
energies=["Climatronic","Electriques","Radar de stationnement AR","Ouvrant"]
anti_values=["Antibrouillards","Boulons de roues protégés"]
vitre_value="Teintées | Athermiques"
volant_v_k="En hauteur"
three_xze="USB"
three_xxze="Tactile"
sol="Velours"
Stores ="Pour vitres de portes arrières"
#### Insertion des marques, modeles et versions ####
email_automobile="ennakl.automobiles@gmail.com"
def process_automobile_brand_submission(driver, path_image_marq, password, perform_login_web1, perform_login_action_web2, select_mobile_partners, marque_v:str, desc_marque,email_automobile):
    current_url=perform_login_web1(driver,email_automobile,password)

    nav="/html/body/app-root/app-partner/section/div/div[1]/div[1]/div[2]"
    time.sleep(10)
    if current_url:
        time.sleep(10)
        nav_e=WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, nav))  # This is a dummy element
    )
    Gestiondecontenu =WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[1]/div[2]/div[2]/ul/a[8]"))  # This is a dummy element
)
    ActionChains(driver).move_to_element(nav_e).click(Gestiondecontenu).perform()
    gestion_marque="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-contenu/div[2]/div/div[2]/button"
    button_marque=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, gestion_marque))  # This is a dummy element
    )
    ActionChains(driver).move_to_element(button_marque).click(button_marque).perform()
    ajouter_nouvelle_marque="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-gestion-marque/div/div[2]/div/div/div/form/div[1]/div/button"
    ajouter_marque=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ajouter_nouvelle_marque))  # This is a dummy element
    )
    ActionChains(driver).move_to_element(ajouter_marque).click(ajouter_marque).perform()
    container=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-marque/div/div[2]/div/div/div/div/div")))
    marque_input=container.find_element(By.ID, 'Marquee')
    des=container.find_element(By.ID, 'desc')
    img2=container.find_element(By.ID, 'img2')
    img2.send_keys(path_image_marq)
    des.send_keys(desc_marque)
    marque_input.send_keys(marque_v)
    submit=driver.find_element(By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-marque/div/div[2]/div/div/div/div/div/form/div[4]/div/button[1]") # type: ignore
    ActionChains(driver).move_to_element(submit).click(submit).perform()
    time.sleep(5)
    perform_login_action_web2(driver)
    x_path_marques_mobiles="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/a/span"
    name2="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/ul/li[3]/a"
    marque_x="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/ul/li[3]/ul/li[3]/a/span"
    select_mobile_partners(driver,marque_x, x_path_marques_mobiles, name2)
    content = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-validation-marque/div/div/div/div/div[2]/ngx-datatable"))
)
    table = content.find_element(By.CLASS_NAME, "datatable-body")
    rows = table.find_elements(By.CLASS_NAME, "datatable-row-wrapper")
    if len(rows) != 0:
        for row in rows:
            if marque_v in row.text:
                validate = driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-validation-marque/div/div/div/div/div[2]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[1]/datatable-body-row/div[2]/datatable-body-cell[5]/div/div/button[2]")
                ActionChains(driver).move_to_element(validate).click(validate).perform()
                break
    current_url=perform_login_web1(driver,email_automobile,password)

    

def add_automobile_model(driver, model, path_image_marq, perform_login_action_web2, select_parametre, select_mobile_partners, marque_v):
    nav="/html/body/app-root/app-partner/section/div/div[1]/div[1]/div[2]"
    
    time.sleep(5)
    nav_e=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, nav))  # This is a dummy element
    )
    
    Gestiondecontenu =WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[1]/div[2]/div[2]/ul/a[8]"))  # This is a dummy element
)
    ActionChains(driver).move_to_element(nav_e).click(Gestiondecontenu).perform()
    gestion_marque="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-contenu/div[2]/div/div[3]/button"
    button_marque=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, gestion_marque))  # This is a dummy element
)
    ActionChains(driver).move_to_element(button_marque).click(button_marque).perform()
    ajouter_nouvelle_marque="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-gestion-modele/div/div[2]/div/div/button"
    ajouter_marque=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ajouter_nouvelle_marque))  # This is a dummy element
)
    ActionChains(driver).move_to_element(ajouter_marque).click(ajouter_marque).perform()
    time.sleep(2)
    container=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-modele/div/div[2]/div/div/div/div")))
    marque_id="marque"
    select_parametre(driver, container, marque_id, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-modele/div/div[2]/div/div/div/div/div/form/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]", marque_v)
    breakmodel_i=container.find_element(By.ID, 'Modele')
    breakmodel_i.send_keys(model)
    des=container.find_element(By.ID, 'Description')
    img2=container.find_element(By.ID, 'imageVitrine1')
    img2.send_keys(path_image_marq)
    des.send_keys("Brand X description")

    submit=driver.find_element(By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-modele/div/div[2]/div/div/div/div/div/form/div[6]/button[1]")
    ActionChains(driver).move_to_element(submit).click(submit).perform()
    time.sleep(5)
#### validation  des model ####
    perform_login_action_web2(driver)
    x_path_marques_mobiles="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/a/span"
    name2="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/ul/li[3]/a"
    marque_x="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/ul/li[3]/ul/li[4]/a/span"
    select_mobile_partners(driver,marque_x, x_path_marques_mobiles, name2)
    content = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-validation-modele/div/div/div/div[2]/ngx-datatable"))
)
    table = content.find_element(By.CLASS_NAME, "datatable-body")
    rows = table.find_elements(By.CLASS_NAME, "datatable-row-wrapper")
    v = False
    if len(rows) != 0:
        for row in rows:
            if model in row.text:
                validate = driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-validation-modele/div/div/div/div[2]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[1]/datatable-body-row/div[2]/datatable-body-cell[5]/div/div/button[2]")
                ActionChains(driver).move_to_element(validate).click(validate).perform()
                v = True
                break#automate_insert_web_interaction(driver,marque, marque_desc, model, path_image_marq, version, model_desc, version_desc, version_prix, duration_garantie, query_cap, query_connectivite, query_memoire, query_ram, query_taille, query_processeur, query_systeme, query_appareil, quantite_number, stock_image, stock_desc, clr, type_product)
    if v :
        approuver=driver.find_element(By.ID, "edo-ani1") 
        ActionChains(driver).move_to_element(approuver).click(approuver).perform()
        button=driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-validation-details-modele/div/div/div/div[2]/div/div[2]/div[2]/button")
        ActionChains(driver).move_to_element(button).click(button).perform()
        time.sleep(3)

def initialize_car_version(driver, model, password, perform_login_web1, select_parametre, version, nbreRapport, nbrePlaceVersion, marque_v, query_carross, prix, nbrePorteVer, query_carburon, query_puissance, duration, couplenmVr, cylindre_v, nbreCylindreVer, couplenVr, query_pui, boite_name, longueurPd, Traction, largeurPrd, hauteurPod, volumeoffre, Performanceetconsommation, one, two, three, xzx, lumierAmbiance_value, sellerie_value, Finitionintérieure, Siege, volant, kit, Accoudoirs, feu_value, phare_value, radar_v, energies, anti_values, vitre_value, volant_v_k, email_automobile, volumestr_coffre):

    perform_login_web1(driver,email_automobile,password)
    
    time.sleep(5)   
    max_attempts = 3
    attempt = 0
    while attempt < max_attempts:
        try:
            Finition = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body > app-root > app-partner > section > div > div.row.mon-espace > div.col.w-10.menu-dashbord > div.dashboard-left > div.left-menu > ul > a:nth-child(6) > li > div > div > span"))
            )
            break
        except (TimeoutException, StaleElementReferenceException):
            attempt += 1
            if attempt == max_attempts:
                print(f"Failed to find Finition element after {max_attempts} attempts")
                raise
            time.sleep(2)
    ActionChains(driver).move_to_element(Finition).click(Finition).perform()
    ajouter_finition="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-gestion-version/section/div/div[2]/div/div[1]/button"
    ajouter_finition=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ajouter_finition))  # This is a dummy element
    )

    ActionChains(driver).move_to_element(ajouter_finition).click(ajouter_finition).perform()
    lists=driver.find_elements(By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/ul/li")
    for i,caracteristique in enumerate(lists):
        if i == 5 :
            ActionChains(driver).move_to_element(caracteristique).click(caracteristique).perform()
            but ="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div/div[2]/button"
            button_en = driver.find_element(By.XPATH, but)
            time.sleep(1)
            ActionChains(driver).move_to_element(button_en).click(button_en).perform()
        if i == 0:
            ActionChains(driver).move_to_element(caracteristique).click(caracteristique).perform()
            marque_id= "marque"
            path_marque="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/form/div/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, marque_id, path_marque, marque_v)
            nom_id=driver.find_element(By.ID, 'nom')
            nom_id.send_keys(version)
            nombre_id=driver.find_element(By.ID, 'nbrePlaceVersion').send_keys(nbrePlaceVersion)
            nbreRapportVersion=driver.find_element(By.ID, 'nbreRapportVersion').send_keys(nbreRapport)
    
            idCarross="idCarross"
            path_carross="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/form/div/div[8]/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, idCarross, path_carross, query_carross)
            voiture_pop=driver.find_element(By.XPATH, '/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/form/div/div[9]/label/input').click()
            garantie=driver.find_element(By.XPATH, '/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/form/div/div[10]/label/input').click()
            model_id="modele"
            model_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/form/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, model_id, model_path, model)
            prixVersion=driver.find_element(By.ID, 'prixVersion').send_keys(prix)
            nbrePorte=driver.find_element(By.ID, 'nbrePorteVer').send_keys(nbrePorteVer)
            dureeGanrantie=driver.find_element(By.ID, 'dureeGanrantie').send_keys(duration)
        if i == 1:
            ActionChains(driver).move_to_element(caracteristique).click(caracteristique).perform()

            idCarburon="idCarburon"
            path_carburon="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, idCarburon, path_carburon, query_carburon)
            idPuissance="idPuissance"
            path_puissance="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, idPuissance, path_puissance, query_puissance)
            nbreCylindre=driver.find_element(By.ID, 'nbreCylindreVer').send_keys(nbreCylindreVer)
            cylindre=driver.find_element(By.ID,"cylindre").send_keys(cylindre_v)
            puissance=driver.find_element(By.ID, 'puissance').send_keys(query_pui)
            couplenmVer=driver.find_element(By.ID, 'couplenmVer').send_keys(couplenmVr)
            coupletrVer=driver.find_element(By.ID, 'coupletrVer').send_keys(couplenVr)
        if i == 2:
            ActionChains(driver).move_to_element(caracteristique).click(caracteristique).perform()
            time.sleep(3)
            try:
               boite_vitesse = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#ngb-nav-2-panel > section > div > div > div.col-md-12.form-group1 > div:nth-child(2) > div'))
               )
               driver.execute_script("arguments[0].scrollIntoView(true);", boite_vitesse)

               ll = WebDriverWait(boite_vitesse, 10).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, "label"))
                )

            except StaleElementReferenceException:
               boite_vitesse = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#ngb-nav-2-panel > section > div > div > div.col-md-12.form-group1 > div:nth-child(2) > div'))
               )

               ll = WebDriverWait(boite_vitesse, 10).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, "label"))
                )

            if len(ll) == 0:
                print("Could not find boite vitesse inputs, skipping this section")
            else:
                print("Found boite vitesse inputs")
            for boite in ll:
                
                if boite_name in  boite.text  :
                    ActionChains(driver).move_to_element(boite).click(boite).perform()
                    break
            transmission="transmission"
            transmission_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, transmission, transmission_path, Traction)
            longueurProd=driver.find_element(By.ID, 'longueurProd').send_keys (longueurPd)
            largeurProd=driver.find_element(By.ID, 'largeurProd').send_keys(largeurPrd)
            hauteurProd=driver.find_element(By.ID, 'hauteurProd').send_keys(hauteurPod)
            volumeCoffre=driver.find_element(By.ID, 'volumeCoffre').send_keys(volumeoffre)
        if i ==3:
            ActionChains(driver).move_to_element(caracteristique).click(caracteristique).perform()
            time.sleep(1)
            try:
                performance_container = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div"))
                )
                input_fields = performance_container.find_elements(By.TAG_NAME, "input")
                for k, input_field in enumerate(input_fields):
                    if k < len(Performanceetconsommation):
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(input_field))
                        input_field.clear()
                        input_field.send_keys(Performanceetconsommation[k])
                        time.sleep(0.5)
            except TimeoutException:
                print("Could not find performance inputs, skipping this section")
        if i == 4:
            ActionChains(driver).move_to_element(caracteristique).click(caracteristique).perform()
            c_one_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[1]"
            c_one = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, c_one_path))
            )
            time.sleep(1)  # Small delay to ensure DOM is stable
            lists = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, f"{c_one_path}/div"))
            )
            
            for c in lists:
                if one in c.text:
                    b=c.find_element(By.TAG_NAME, "input")
                    ActionChains(driver).move_to_element(c).click(b).perform()
                    break
            time.sleep(2)
            two_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[2]/div/div[2]"
            twox=driver.find_element(By.XPATH, two_path)
            sss=twox.find_elements(By.TAG_NAME, "div")
            for c in sss:
                if two in c.text:
                    b=c.find_element(By.TAG_NAME, "input")
                    ActionChains(driver).move_to_element(c).click(b).perform()
                    break
            three_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[3]/div[1]/div[2]"
            three_x=driver.find_element(By.XPATH, three_path)
            for c in three_x.find_elements(By.TAG_NAME, "div"):
                if three in c.text:
                    ActionChains(driver).move_to_element(c).click(c.find_element(By.TAG_NAME, "input")).perform()

                    break
            threes_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[3]/div[2]/div[2]"
            threesz_x=driver.find_element(By.XPATH, threes_path)
            for c in threesz_x.find_elements(By.TAG_NAME, "div"):
                if three_xze in c.text:
                    ActionChains(driver).move_to_element(c).click(c.find_element(By.TAG_NAME, "input")).perform()
                    break
            threes_sspath="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[3]/div[3]/div[2]"
            threesz_ssx=driver.find_element(By.XPATH, threes_sspath)
            for c in threesz_ssx.find_elements(By.TAG_NAME, "div"):
                if three_xxze in c.text:
                    c.find_element(By.TAG_NAME, "input").click()
                    break
            xz="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[4]/div[1]/div[2]"
            xz=driver.find_element(By.XPATH, xz)
            
            for c in xz.find_elements(By.TAG_NAME, "div"):
                if sol  in c.text:
                    c.find_element(By.TAG_NAME, "label").click()
                    break
            xzz="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[4]/div[2]/div[2]/div"
            xzzx=driver.find_element(By.XPATH, xzz)
            ss=xzzx.find_elements(By.TAG_NAME, "label")
            for c in ss:
                if Stores  in c.text:
                    ActionChains(driver).move_to_element(c).click(c).perform()
                    break
                    
            lumierAmbiance = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'lumierAmbiance'))
            )
            lumierAmbiance.send_keys(lumierAmbiance_value)
            sellerie_id="sellerie"
            sellerie_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[6]/div/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, sellerie_id, sellerie_path, sellerie_value)
            five_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[7]/div[1]/div[2]"
            five_x=driver.find_element(By.XPATH, five_path)
            for c in five_x.find_elements(By.TAG_NAME, "div"):
                if Finitionintérieure in c.text:
                    button=c.find_element(By.TAG_NAME, "input")
                    ActionChains(driver).move_to_element(button).click(button).perform()
                    break
            sixe_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[7]/div[2]/div[2]"
            sixe_x=driver.find_element(By.XPATH, sixe_path)
            for c in sixe_x.find_elements(By.TAG_NAME, "div"):
                if Siege in c.text:
                    input_element = c.find_element(By.TAG_NAME, "input")
                    ActionChains(driver).move_to_element(input_element).click(input_element).perform()
                    break
            seet_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[7]/div[3]/div[2]"
            seet_x=driver.find_element(By.XPATH, seet_path)
            for c in seet_x.find_elements(By.TAG_NAME, "div"):
                if volant in c.text:
                    input_element = c.find_element(By.TAG_NAME, "input")
                    ActionChains(driver).move_to_element(input_element).click(input_element).perform()
                    break
            kit_1="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[8]"
            kit_1=driver.find_element(By.XPATH, kit_1)
            ll=kit_1.find_elements(By.TAG_NAME, "div")
            #driver.execute_script("arguments[0].scrollIntoView(true);",kit_1 )
            for c in ll:
                if  kit in c.text:
                    ActionChains(driver).move_to_element(c).click(c.find_element(By.TAG_NAME, "input")).perform()
                    break
        
            kit_2="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[9]"
            kit_2=driver.find_element(By.XPATH, kit_2)
            #driver.execute_script("arguments[0].scrollIntoView(true);", kit_2)
            for c in kit_2.find_elements(By.TAG_NAME, "div"):
                if  "Kit rangement" in c.text:
                        ActionChains(driver).move_to_element(c).click(c.find_element(By.TAG_NAME, "input")).perform()

                        break
            acc_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[10]/div/div[2]"
            acc_x=driver.find_element(By.XPATH, acc_path)
            #driver.execute_script("arguments[0].scrollIntoView(true);", acc_x)
            for c in acc_x.find_elements(By.TAG_NAME, "div"):
                if  Accoudoirs in c.text:
                    ActionChains(driver).move_to_element(c).click(c.find_element(By.TAG_NAME, "label")).perform()

                    break
            feu_id="feu"
            feu_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[11]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, feu_id, feu_path, feu_value)
            phare_id="phare"
            phare_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[11]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, phare_id, phare_path, phare_value)
            radar_id="radar"
            radar_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[11]/div[3]/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, radar_id, radar_path, radar_v)
            anti_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[12]"
            anti_x=driver.find_element(By.XPATH, anti_path)
            for c in anti_x.find_elements(By.TAG_NAME, "div"):
                for x in c.find_elements(By.TAG_NAME, "div"):
                    if x.text in anti_values:
                        b=x.find_element(By.TAG_NAME, "input")
                        ActionChains(driver).move_to_element(x).click(b).perform()
                        break
            xxx_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[13]/div[1]/div[2]"
            xxx_x=driver.find_element(By.XPATH, xxx_path)
            mm=xxx_x.find_elements(By.TAG_NAME, "div")
            for c in mm:
                if c.text in energies:
                    ActionChains(driver).move_to_element(c).click(c.find_element(By.TAG_NAME, "input")).perform()

                    break
            zzz_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[13]/div[2]/div[2]"
            zzz_z= driver.find_element(By.XPATH, zzz_path)
            for c in zzz_z.find_elements(By.TAG_NAME, "div"):
                if c.text in energies:
                    c.find_element(By.TAG_NAME, "input").click()
                    break
            Toit_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[13]/div[3]/div[2]"
            Toit_z= driver.find_element(By.XPATH, Toit_path)
            for c in Toit_z.find_elements(By.TAG_NAME, "div"):
                if c.text in energies:
                    c.find_element(By.TAG_NAME, "input").click()
                    break
            vitre_id="vitre"
            vitre_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[14]/div/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, vitre_id, vitre_path,vitre_value)
            volant_id="volant"
            volant_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[15]/div/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, volant_id, volant_path, volant_v_k)
            coffre_id="coffre"
            coffre_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-version/section/section/div/div/form/div/div/section/div/div[16]/div/div/ng-select/ng-dropdown-panel/div/div[2]"
            select_parametre(driver, caracteristique, coffre_id, coffre_path, volumestr_coffre)
def process_vehicle_information(driver, model, password, perform_login_web1, perform_login_action_web2, select_mobile_partners, email_automobile):
    #current_url = process_automobile_brand_submission(driver, model, path_image_marq, password, perform_login_web1, perform_login_action_web2, select_parametre, select_mobile_partners, marque_v, email_automobile)


    

    perform_login_action_web2(driver)
    x_path_marques_mobiles="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/a/span"
    name2="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/ul/li[3]/a"
    marque_x="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/ul/li[3]/ul/li[5]/a/span"
    select_mobile_partners(driver,marque_x, x_path_marques_mobiles, name2)
    content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-versions/div/div[2]/div/div/div/div/ngx-datatable")))
    table = content.find_element(By.CLASS_NAME, "datatable-body")
    rows= table.find_elements(By.CLASS_NAME, "datatable-row-wrapper")
    v = False
    if len(rows) != 0:
        for row in rows:
            if model in row.text:
                validate = driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-versions/div/div[2]/div/div/div/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[1]/datatable-body-row/div[2]/datatable-body-cell[6]/div/div/button[1]")
                ActionChains(driver).move_to_element(validate).click(validate).perform()
                v = True
                break
    if v:
        validate_box=  driver.find_element(By.XPATH,"/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-version-details/div/div/div/div[3]/div/div[2]/div[1]/div/div[1]/label")
        ActionChains(driver).move_to_element(validate_box).click(validate_box).perform()
        validate_button = driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-version-details/div/div/div/div[3]/div/div[2]/div[3]/button")
        ActionChains(driver).move_to_element(validate_button).click(validate_button).perform()
        time.sleep(3)

def navigate_to_stock(driver, password, perform_login_web1, email_automobile,marque,model,version,clr,quantite_number,stock_desc):
    perform_login_web1(driver,email_automobile,password)
    time.sleep(5)
    stock_nav =WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[1]/div[2]/div[2]/ul/a[7]/li/div/div"))  # This is a dummy element
    )
    ActionChains(driver).move_to_element(stock_nav).click(stock_nav).perform()
    stock_ajout="html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-gestion-voiture/section/div[2]/div/div[1]/button"
    button_stock=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, stock_ajout))  # This is a dummy element
    )
    ActionChains(driver).move_to_element(button_stock).click(button_stock).perform()
    ca_path="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-voiture/div/div[2]/div/div/div"
    caracterestique=WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, ca_path)))
    marqueMobile="marque"
    path_marqueMobile="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-voiture/div/div[2]/div/div/div/form/div[1]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, marqueMobile, path_marqueMobile, marque)
    modeleMobile="modele"
    path_modeleMobile="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-voiture/div/div[2]/div/div/div/form/div[1]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, modeleMobile, path_modeleMobile, model)
    idVersionMobile="idVersion"
    path_versionMobile="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-voiture/div/div[2]/div/div/div/form/div[2]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, idVersionMobile, path_versionMobile, version)
    idCouleur="idCouleur"
    couleur_path ="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-voiture/div/div[2]/div/div/div/form/div[2]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, idCouleur, couleur_path, clr)
    quantite_stock=driver.find_element(By.XPATH, '/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-voiture/div/div[2]/div/div/div/form/div[3]/div[1]/input').send_keys(quantite_number)
    descr=driver.find_element(By.ID,'Description').send_keys(stock_desc)
    button_stock=driver.find_element(By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-ajouter-voiture/div/div[2]/div/div/div/form/div[4]/div/button[1]")
    ActionChains(driver).move_to_element(button_stock).click(button_stock).perform()
    time.sleep(3)
    perform_login_action_web2(driver)
    x_path_marques_mobiles="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/a/span"
    name2="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/ul/li[3]/a"
    marque_x="/html/body/app-root/app-content-layout/div/div/div/div[1]/app-sidebar/div[2]/ul/li[10]/ul/li[3]/ul/li[6]/a/span"
    select_mobile_partners(driver,marque_x, x_path_marques_mobiles, name2)
    content = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-versions/div/div[2]/div/div/div/div/ngx-datatable")))
    table = content.find_element(By.CLASS_NAME, "datatable-body")
    rows= table.find_elements(By.CLASS_NAME, "datatable-row-wrapper")
    v = False
    if len(rows) != 0:
        for row in rows:
            if model in row.text:
                validate = driver.find_element(By.XPATH, "/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-voitures/div/div/div[2]/div/div/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[1]/datatable-body-row/div[2]/datatable-body-cell[12]/div/div/button")
                ActionChains(driver).move_to_element(validate).click(validate).perform()
                v = True
                break
    if v:
        validate_box=  driver.find_element(By.XPATH,"/html/body/app-root/app-content-layout/div/div/div/div[2]/main/app-offre/div/div[2]/div/div/div/button[1]")
        ActionChains(driver).move_to_element(validate_box).click(validate_box).perform()
        
        time.sleep(3)
    


#process_vehicle_information(driver, model, path_image_marq, version, password, perform_login_web1, perform_login_action_web2, select_parametre, select_mobile_partners, marque_v, nbreRapport, nbrePlaceVersion, query_carross, prix, nbrePorteVer, query_carburon, query_puissance, duration, couplenmVr, cylindre_v, nbreCylindreVer, couplenVr, query_pui, boite_name, longueurPd, Traction, largeurPrd, hauteurPod, volumeoffre, Performanceetconsommation, one, two, three, xzx, lumierAmbiance_value, sellerie_value, Finitionintérieure, Siege, volant, kit, Accoudoirs, feu_value, phare_value, radar_v, energies, anti_values, vitre_value, volant_v_k, email_automobile, process_automobile_brand_submission, initialize_car_version)
#validate_product_stock(driver, marque, model, version, quantite_number, stock_image, stock_desc, clr, type_product, driver.current_url)
#navigate_to_stock(driver, password, perform_login_web1, email_automobile)
def upload_gallery(driver, password, perform_login_web1, select_parametre, email_automobile,gallery_img,limousine="A3 Limousine"):
    perform_login_web1(driver,email_automobile,password)
    
    
    max_attempts = 3
    attempt = 0
    while attempt < max_attempts:
        try:
            Finition = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > app-root > app-partner > section > div > div.row.mon-espace > div.col.w-10.menu-dashbord > div.dashboard-left > div.left-menu > ul > a:nth-child(6) > li > div > div > span"))
        )
            break
        except (TimeoutException, StaleElementReferenceException):
            attempt += 1
            if attempt == max_attempts:
                print(f"Failed to find Finition element after {max_attempts} attempts")
                raise
            time.sleep(2)
    ActionChains(driver).move_to_element(Finition).click(Finition).perform()
    ajouter_finition="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-gestion-version/section/div/div[2]/div/div[3]/button"
    ajouter_finition=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, ajouter_finition))  # This is a dummy element
    )
    ActionChains(driver).move_to_element(ajouter_finition).click(ajouter_finition).perform()
    caracterestique=driver.find_element(By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-upload-galerie/div[2]/div/div")
    idVersionMobile="version"
    path_versionMobile="/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-upload-galerie/div[2]/div/div/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]"
    select_parametre(driver, caracterestique, idVersionMobile, path_versionMobile, limousine)
    img=caracterestique.find_element(By.ID,"image")
    img.send_keys(gallery_img)
    button_stock=driver.find_element(By.XPATH, "/html/body/app-root/app-partner/section/div/div[1]/div[2]/div/app-upload-galerie/div[3]/div/button")
    ActionChains(driver).move_to_element(button_stock).click(button_stock).perform()

automobile_data = {
    "marques": {
        "BXZZE": {  # Marque
            "desc": "Description of XXEDRAZZZE",
            "imp_path": "C:/Users/Ons/WebScrape-Automator/lib/audi.jpg",
            "models": {
                "MODELXDRAGXON": {  # Model
                    "desc": "Description of MODELXDRAGON",
                    "clr":"blank",
                    "quantite_number":5,
                    "stock_desc":"stock_desc",
                    "imp_path": path_image_marq,
                    "gallery_img": path_image_marq,
                    "version": "versionzxxx",
                    "nbreRapport": 4,
                    "nbrePlaceVersion": 4,
                    "query_carross": "SUV",
                    "prix": "10000",
                    "nbrePorteVer": "4",
                    "query_carburon": "Essence",
                    "query_puissance": "23",
                    "duration": "2",
                    "couplenmVr": "4",
                    "cylindre_v": "4",
                    "nbreCylindreVer": "4",
                    "couplenVr": "4",
                    "query_pui": "23",
                    "boite_name": "Automatique",
                    "longueurPd": "4",
                    "Traction": "Traction",
                    "largeurPrd": "4",
                    "hauteurPod": "4",
                    "volumeoffre": "4",
                    "Performanceetconsommation": ["4", "4", "4", "4", "4", "4"],
                    "volumestr_coffre":"Fermeture électrique",
                    "limousine":"A3 Limousine",
                    "finitions": {
                        "securite": {
                            "one": "ABS",
                            "two": "Frontaux",
                            "three": "BMW Professional CD"
                        },
                        "confort": {
                            "lumierAmbiance_value": "5",
                            "sellerie_value": "Cuir",
                            "Finitionintérieure": "Bois",
                            "Siege": "Réglage lombaire",
                            "volant": "Cuir",
                            "kit": "Kit fumeurs",
                            "kit_1": "Kit de réparation",
                            "Accoudoirs": "Avant"
                        },
                        "eclairage": {
                            "feu_value": "Feux de jour",
                            "phare_value": "LED"
                        },
                        "aide_conduite": {
                            "radar_v": "Avant",
                            "energies": ["Climatronic", "Electriques", "Radar de stationnement AR", "Ouvrant"]
                        },
                        "securite_supplementaire": {
                            "anti_values": ["Antibrouillards", "Boulons de roues protégés"]
                        },
                        "vitres": {
                            "vitre_value": "Teintées | Athermiques",
                            "Stores": "Pour vitres de portes arrières"
                        },
                        "volant": {
                            "volant_v_k": "En hauteur"
                        },
                        "multimedia": {
                            "three_xze": "USB",
                            "three_xxze": "Tactile"
                        },
                        "materiaux": {
                            "sol": "Velours",
                            "xz": ["Velours", "Pour vitres de portes arrières"]
                        }
                    }
                }
            }
        }
    }
}

for marque, marque_data in automobile_data["marques"].items():
    marque_v = marque
    desc_marque = marque_data["desc"]
    path_image_marq = marque_data["imp_path"]

    # Process automobile brand (function placeholder)
    process_automobile_brand_submission(driver,  path_image_marq, password, perform_login_web1, 
      perform_login_action_web2, select_mobile_partners,marque_v, desc_marque,email_automobile)

    for model, model_data in marque_data["models"].items():
        desc_model = model_data["desc"]
        path_image_model = model_data["imp_path"]
        version = model_data["version"]
        nbreRapport = model_data["nbreRapport"]
        nbrePlaceVersion = model_data["nbrePlaceVersion"]
        query_carross = model_data["query_carross"]
        prix = model_data["prix"]
        nbrePorteVer = model_data["nbrePorteVer"]
        query_carburon = model_data["query_carburon"]
        query_puissance = model_data["query_puissance"]
        duration = model_data["duration"]
        couplenmVr = model_data["couplenmVr"]
        cylindre_v = model_data["cylindre_v"]
        nbreCylindreVer = model_data["nbreCylindreVer"]
        couplenVr = model_data["couplenVr"]
        query_pui = model_data["query_pui"]
        boite_name = model_data["boite_name"]
        longueurPd = model_data["longueurPd"]
        Traction = model_data["Traction"]
        largeurPrd = model_data["largeurPrd"]
        hauteurPod = model_data["hauteurPod"]
        volumeoffre = model_data["volumeoffre"]
        Performanceetconsommation = model_data["Performanceetconsommation"]
        volumestr_coffre=model_data["volumestr_coffre"]
        limousine=model_data["limousine"]
        gallery_img=model_data["gallery_img"]
        clr,quantite_number,stock_desc = model_data["clr"],model_data["quantite_number"],model_data["stock_desc"]

        # Extracting finition details
        one = model_data["finitions"]["securite"]["one"]
        two = model_data["finitions"]["securite"]["two"]
        three = model_data["finitions"]["securite"]["three"]

        lumierAmbiance_value = model_data["finitions"]["confort"]["lumierAmbiance_value"]
        sellerie_value = model_data["finitions"]["confort"]["sellerie_value"]
        Finitionintérieure = model_data["finitions"]["confort"]["Finitionintérieure"]
        Siege = model_data["finitions"]["confort"]["Siege"]
        volant = model_data["finitions"]["confort"]["volant"]
        kit = model_data["finitions"]["confort"]["kit"]
        Accoudoirs = model_data["finitions"]["confort"]["Accoudoirs"]

        feu_value = model_data["finitions"]["eclairage"]["feu_value"]
        phare_value = model_data["finitions"]["eclairage"]["phare_value"]

        radar_v = model_data["finitions"]["aide_conduite"]["radar_v"]
        energies = model_data["finitions"]["aide_conduite"]["energies"]  # List

        anti_values = model_data["finitions"]["securite_supplementaire"]["anti_values"]  # List

        vitre_value = model_data["finitions"]["vitres"]["vitre_value"]
        Stores = model_data["finitions"]["vitres"]["Stores"]

        volant_v_k = model_data["finitions"]["volant"]["volant_v_k"]

        multimedia_usb = model_data["finitions"]["multimedia"]["three_xze"]
        multimedia_tactile = model_data["finitions"]["multimedia"]["three_xxze"]

        sol_materiaux = model_data["finitions"]["materiaux"]["sol"]
        xz_materiaux = model_data["finitions"]["materiaux"]["xz"]  # List

        add_automobile_model(driver, model, path_image_model, perform_login_action_web2, select_parametre, select_mobile_partners, marque_v)
        initialize_car_version(driver, model, password, perform_login_web1, select_parametre,version,nbreRapport ,
                           nbrePlaceVersion, marque_v, query_carross, prix, nbrePorteVer, query_carburon, query_puissance, duration,
                             couplenmVr, cylindre_v, nbreCylindreVer, couplenVr, query_pui, boite_name, longueurPd, Traction, largeurPrd, hauteurPod, 
                             volumeoffre, Performanceetconsommation, one, two, three, xz_materiaux, lumierAmbiance_value, sellerie_value, Finitionintérieure, 
                             Siege, volant, kit, Accoudoirs, feu_value, phare_value, radar_v, energies, anti_values, vitre_value, volant_v_k, 
                             email_automobile, volumestr_coffre)
        upload_gallery(driver, password, perform_login_web1, select_parametre, email_automobile, gallery_img, limousine)
        process_vehicle_information(driver, model, password, perform_login_web1, perform_login_action_web2, select_mobile_partners, email_automobile)
        navigate_to_stock(driver, password, perform_login_web1, email_automobile,marque,model,version,clr,quantite_number,stock_desc)


driver.quit()
#backoffice
# commercial@tunistore.tn
# 123456789 