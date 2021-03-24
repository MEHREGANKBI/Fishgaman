#!/usr/bin/env python3
import re
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from data2img import text2img, setwp, img2bg
import os

from time import sleep
from selenium import webdriver
#from usps import usps_dict
def get_volume():
    #some of the options below just exist so as to lower the likelihood of chromedriver throwing a render error. 
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--dns-prefetch-disable")

    fish = webdriver.Chrome('/home/mehregankbi/chromedriver', options = chrome_options)
    fish.get('https://user.pishgaman.net/Login.aspx')
    # usin = fish.find_element_by_xpath('//input[@id="tbUsername"]')
    usin = WebDriverWait(fish, 30).until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'input#tbUsername')))
    # psin = fish.find_element_by_xpath('//input[@id="tbPassword"]')
    psin = WebDriverWait(fish, 30).until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'input#tbPassword')))
    bttn = fish.find_element_by_xpath('//*[@id="bSubmit"]')
    usin.send_keys(user_dict['username'])
    psin.send_keys(user_dict['userpass'])
    print('==== started clicking')
    bttn.click()
    print('==== done logging in ')
    sleep(5)
    vol_afz =  WebDriverWait(fish, 30).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="ContentPlaceHolder1_timeBaseCreditBox"]/div[2]/label[2]'))).text.strip()
    vol_norm = WebDriverWait(fish, 30).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="form1"]/div[5]/div[2]/div/div[4]/div/div/div[3]/div/div[1]/div[2]/label[2]'))).text.strip()
    days_left = WebDriverWait(fish, 30).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="form1"]/div[5]/div[2]/div/div[4]/div/div/div[3]/div/div[3]/div[2]/label[3]'))).text.strip()

    print(re.findall(r'[\d,]+',vol_afz)[0])
    print(re.findall(r'[\d,]+',vol_norm)[0])
    print(re.findall(r'[\d\/\: ]',days_left)[1])

    with open('/home/mehregankbi/fishgaman/netlog.log', 'a') as f :
        f.write(' '.join(['\n', 'Date:', datetime.utcnow().__str__(), '\n', 'Afzoodeh left:', re.findall(r'[\d,]+', vol_afz)[0], '\n',
         'Normal left:', re.findall(r'[\d,]+', vol_norm)[0], '\n', 'Expiry date'+ re.findall(r'[\d\/\: ]+', days_left)[1], '\n', '\n']))
        f.write('==========================================\n')
    fish.quit()

    return ['Time: {}'.format(datetime.now().__str__()), 'Afzoodeh left: {}'.format(re.findall(r'[\d,]+', vol_afz)[0]),
     'Normal left: {}'.format(re.findall(r'[\d,]+', vol_norm)[0]), 'Expiry date{}'.format(re.findall(r'[\d\/\: ]+', days_left)[1])]
     

if __name__ == '__main__' :
    try:
        stringList = get_volume()
        imgArray = text2img(stringList)
        if 'ubuntu-patched-finale.png' in os.listdir('/home/mehregankbi/fishgaman') :
            os.remove('/home/mehregankbi/fishgaman/ubuntu-patched-finale.png')
        imageFile = img2bg(imgArray)
        setwp(imageFile)
    except Exception as e :
        with open('/home/mehregankbi/fishgaman/netlog.log', 'a') as f :
            f.write('\nDate: {}\n{}\n'.format(datetime.utcnow().__str__(),e.__str__()))
            f.write('==========================================\n')
