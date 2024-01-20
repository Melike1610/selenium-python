from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

browser=webdriver.Chrome()
browser.get("https://www.lcwaikiki.com/")
time.sleep(2)

pyautogui.moveTo(491,283, duration=3,tween=pyautogui.easeInOutQuad)
pyautogui.click()
pyautogui.moveTo(800,900, duration=3,tween=pyautogui.easeInOutQuad)
pyautogui.click()


pyautogui.moveTo(84,316, duration=3,tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(84,350, duration=3,tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(358,445, duration=3,tween=pyautogui.easeInOutQuad)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(940,532, duration=3,tween=pyautogui.easeInOutQuad)
pyautogui.click()
time.sleep(2)
 



 
   

cevap = []
last_height = browser.execute_script("return document.documentElement.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(1)     
    new_height = browser.execute_script("return document.documentElement.scrollHeight")

    if last_height == new_height:
        break

    last_height = new_height
    time.sleep(1)

    ana_ogeler = browser.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[5]/div/div[2]/div/a')

    for ana_oge in ana_ogeler:
        link = ana_oge.get_attribute("href")
        cevap.append(link)

for link in cevap:  
    browser.get(link)
    cevap2 = []
    last_height = browser.execute_script("return document.documentElement.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1)      
        new_height = browser.execute_script("return document.documentElement.scrollHeight")

        if last_height == new_height:
            break

        last_height = new_height
        time.sleep(1)

        ana_ogelerr = browser.find_elements(By.XPATH, '//*[@id="dv-mp-reviews"]/div[2]/div[7]/a')
       

        for ana_oge in ana_ogelerr:
            link = ana_oge.get_attribute("href")
            browser.get(link)
            results = []
            results2 = []


            list =browser.find_elements(By.XPATH,'//*[@id="all-reviews-root"]/div/div[4]/div[3]/div/p[2]')
            list2 =browser.find_elements(By.XPATH,'//*[@id="all-reviews-root"]/div/div[4]/div[3]/div/p[1]/span[1]')
            list3 = browser.find_elements(By.XPATH, '//*[@id="all-reviews-root"]/div/div[4]/div[3]/div/div[1]/div/div')
            time.sleep(1)

            last_height = browser.execute_script("return document.documentElement.scrollHeight")
            while True:
             browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
             time.sleep(1)
             new_height =browser.execute_script("return document.documentElement.scrollHeight")
             if last_height == new_height:
              break
             last_height = new_height
             list =browser.find_elements(By.XPATH,'//*[@id="all-reviews-root"]/div/div[4]/div[3]/div/p[2]')#yorum
             list2 =browser.find_elements(By.XPATH,'//*[@id="all-reviews-root"]/div/div[4]/div[3]/div/p[1]/span[1]')#tarih
             list3 = browser.find_elements(By.XPATH, '//*[@id="all-reviews-root"]/div/div[4]/div[3]/div/div[1]/div/div')#yıldız

             time.sleep(1)
             print("count: "+ str(len(list)))
             print("count: "+ str(len(list2)))
             for i in list:
                results.append(i.text)
             for j in list2:
              results2.append(j.text)

            list4 =browser.find_element(By.XPATH,'//*[@id="all-reviews-root"]/div/div[3]/div/div[1]/div[1]/div')
            star_percentage1 = list4.get_attribute('class').split('pct-')[1]#genel yıldız
            review_count_element = browser.find_element(By.CLASS_NAME,"review-count")
            review_count = review_count_element.text#yorum sayısı

            count = 1

            with open("pythonprojemmmm.txt", "a", encoding="UTF-8") as file:
              file.write(f"====Ürün Genel Değerlendirme %{star_percentage1} Yıldız, ")
              file.write(f"{review_count}====\n ")

              for item, item2, index in zip(results, results2, list3):
                file.write(f"Ürün {count} Yorum: {item}\n")
                file.write(f"Ürün {count} Tarih: {item2}\n")
                star_percentage = index.get_attribute('class').split('pct-')[1]
                file.write(f"Ürün {count} Yıldız Değeri: %{star_percentage}\n")

                count +=1
        

browser.quit()





   

  













































    





  