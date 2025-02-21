from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import torch
import io, base64
from PIL import Image
from diffusers import StableDiffusionPipeline
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import undetected_chromedriver as uc
import threading

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
pipeline = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16
)
pipeline = pipeline.to('cuda')
# Initialize the WebDriver and other settings
email="azizwerghighi@gmail.com"
password="12312300aziz@A"
base_url = "https://www.youtube.com/"
def authenticate_user(email, password, base_url):
    options = uc.ChromeOptions()
    options.user_data_dir = "c:\\temp\\profile"
    driver = uc.Chrome(
    options = options 
    )  
    driver.delete_all_cookies()
    driver.get(base_url)
    time.sleep(5)

    try:
        connexion= WebDriverWait(
        driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')))
        connexion.click()
        
        try:
            identifiant= WebDriverWait(
            driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId')))
            identifiant.send_keys(email)
            suivant= WebDriverWait(
            driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button')))
            ActionChains(driver).move_to_element(suivant).click(suivant).perform()
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
            email_exist=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[1]')
            if email_exist:
                print("Email already exists")
                ActionChains(driver).move_to_element(email_exist).click(email_exist).perform()
        time.sleep(10)
        password= driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
        login= WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button')))
        ActionChains(driver).move_to_element(login).click(login).perform()
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
         print("Already connected")
 

    
    return driver

driver = authenticate_user(email, password, base_url)
llm=Ollama(model="qwen2.5:3b", base_url="http://localhost:11434")

template = """  
        I am an AI assistant specialized in generating imaginative and dynamic stories. Each line represents a new scene in the unfolding narrative. Here is the randomly generated story:  

        [Describe the opening setting and introduce the protagonist.]  
        [Introduce a conflict or mystery that drives the story forward.]  
        [A new character or twist complicates the situation.]  
        [The protagonist takes action to overcome the obstacle.]  
        [A dramatic turning point or revelation changes everything.]  
        [The climax—tension peaks as the main conflict is confronted.]  
        [Resolution—loose ends are tied up, and a final note is given.]  
        {question}
        """  

QA_CHAIN_PROMPT = PromptTemplate(
        template=template,
        input_variables=[ "question" ],
        )
        
llm_chain = LLMChain(
            llm=llm, 
            prompt=QA_CHAIN_PROMPT, 
            callbacks=None, 
            verbose=True
        )
# Generate a creative story prompt
question = "Generate a creative story with engaging scenes and characters."
response = [x for i, x in enumerate(llm_chain.run(question=question).split("\n")) if i % 2 == 0]

add = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
add.click()
ligne= driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item')
max_attempts = 5
attempt = 0
success = False
while not success and attempt < max_attempts:
    try:
        ligne = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item'))
        )
        ActionChains(driver).move_to_element(ligne).click().perform()
        success = True
    except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
        print(f"Attempt {attempt + 1}: Failed to click on ligne element")
        attempt += 1
        time.sleep(1)

try:
    chaine_new = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-creation-dialog-renderer/div/div[6]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
    chaine_new.click()
except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
    print("chaine already exists")
selection_video=driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-uploads-file-picker-animation/div/div[3]')
#selection_video.click()

llm_gen_description = Ollama(model="ALIENTELLIGENCE/genaiimagecsprompt", base_url="http://localhost:11434")
template_description = """  
I am an AI assistant specialized in generating imaginative and dynamic stories. My role is to take a scene description and provide a detailed visualization of how the image for that scene could look.  

### Scene Description:  
{scene}  

### Image Visualization:  
[Describe in detail what the scene would look like as an image, including lighting, colors, setting, characters, mood, and any key visual elements.]  
"""  
QA_CHAIN_PROMPT_2= PromptTemplate(
        template=template_description,
        input_variables=[ "scene" ],
        )
llm_chain_2= LLMChain(
            llm=llm_gen_description, 
            prompt=QA_CHAIN_PROMPT_2, 
            callbacks=None, 
            verbose=True
        )
scene_discriptions = []
threads = []

def process_scene(scene):
    scene_discription = llm_chain_2.run(scene=scene)
    scene_discriptions.append(scene_discription)
    print(scene_discription)
    print("\n")

for scene in response:
    thread = threading.Thread(target=process_scene, args=(scene,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

images = []
threads = []


def generate_image(scene_descr):
    import requests

    res = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
        headers={
            "authorization": f"Bearer sk-QCRo3VgRXhWSgjppZl2ksNyovoxS37K3tWE2IthfVWxyYDnc",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": scene_descr,
            "output_format": "png",
        },
    )

    if res.status_code == 200:
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(res.content, "utf-8"))))
        images.append(img)
    else:
        raise Exception(str(res.json()))

for scene_descr in scene_discriptions:
    thread = threading.Thread(target=generate_image, args=(scene_descr,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    

driver.quit()
    
    