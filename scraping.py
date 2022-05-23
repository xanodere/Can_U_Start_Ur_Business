import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import json


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument(r'--user-data-dir=C:\Users\lenovo\AppData\Local\Google\Chrome\test\User Data')
options.add_argument('--headless')

def note_site(nom_site):

    driver = webdriver.Chrome( chrome_options=options)
    
    driver.get("https://freetools.seobility.net/en/seocheck/"+ nom_site)
    valueprinc = driver.find_elements_by_class_name("donutrenderlabel")[0].text
    final_val = int(valueprinc[:len(valueprinc)-1])


    values = driver.find_elements_by_class_name("progress-bar")

    B=[]
    B.append(final_val)
    for i in range(len(values)):
        
        if '%' in values[i].text: 
            a = values[i].text
            a = a[:len(a)-2]
            B.append(int(a))
        
    return B   #  en ordre [total, meta inf, page quality, page structure, link structure, Server, facteurs externe] 
 


def note_compettivite(keyword):

    driver1 = webdriver.Chrome( chrome_options=options)
    driver1.get("https://app.kwfinder.com/dashboard?language_id=1002&location_id=0&query="+ keyword)
    time.sleep(4)
    resultat = driver1.find_elements_by_class_name("mg-rank")[0].text
    

    return int(resultat)
  

"""def note_compettivite_nomsite(keyword,nom_site):

    driver1 = webdriver.Chrome( chrome_options=options)
    driver2 = webdriver.Chrome( chrome_options=options)
   
    driver1.get("https://mangools.com/users/sign_in")
    driver2.get("https://freetools.seobility.net/en/seocheck/"+ nom_site)
    element = driver1.find_elements_by_class_name ("mg-input")
    driver2.find_element_by_css_selector('.btn.btn-success.pull-right').click()
    element[0].send_keys("anthoDarKe@gmail.com")
    element[1].send_keys("moujahid")
    valueprinc = driver2.find_elements_by_class_name("donutrenderlabel")[0].text
    final_val = int(valueprinc[:len(valueprinc)-1])


    values = driver2.find_elements_by_class_name("progress-bar")

    B=[]
    B.append(final_val)
    for i in range(len(values)):
        
        if '%' in values[i].text: 
            a = values[i].text
            a = a[:len(a)-2]
            B.append(int(a))
    driver1.find_elements_by_class_name("mg-btn")[0].send_keys(Keys.ENTER)
    driver1.get("https://app.kwfinder.com/dashboard?language_id=1002&location_id=0&query="+ keyword)
    time.sleep(4)
    resultat = driver1.find_elements_by_class_name("mg-rank")[0].text
    
    
    
   
    
    
    
   
    return [int(resultat),B]"""




## note_compettivite_nomsite("informatique","farad.ma")    



