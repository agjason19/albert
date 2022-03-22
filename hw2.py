#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:09:34 2022

@author: agjason19
"""

import time
# pip install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup # pip install beautifulsoup4

chrome_driver_path = '/usr/local/bin/chromedriver'
delay = 60

driver = webdriver.Chrome(executable_path=chrome_driver_path)

rows = []

for page_number in range(0,30,30):
    page_url = 'https://rent.591.com.tw/?kind=0&region=1&firstRow={page_number}'
    driver.get(page_url)
    time.sleep(10)

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-container-content')))
    except TimeoutException:
        print('Loading exceeds delay time')
        break
    else:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        case_list = soup.find('div', {'class': 'list-container-content'})
        cases = case_list.find_all('a',{'target': '_blank'})
        

