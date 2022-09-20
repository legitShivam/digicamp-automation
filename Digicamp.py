""" Importing functions from external module Selenium """

import chromedriver_autoinstaller
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# try:
chromedriver_autoinstaller.install()# Chrome driver
options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging', 'enable-automation'])

b = webdriver.Chrome(
    executable_path=r"C:\Users\dell\Downloads\Compressed\chromedriver.exe", options=options)  # This will download chromedriver if it is not available.
b.maximize_window()
# This line will make sure that this program waits for max 5s if the effect of a code is taking time to display
b.implicitly_wait(300)

# Opening Digicamp website on Chrome
b.get("https://www.apsdigicamp.com/")

b.find_element_by_class_name("loginbut").click()  # login button
b.find_element_by_xpath(  # Teachers button
    "//*[@id='login-modal']/div/div/div/div/div/div/div/div[1]/div/a[2]").click()

# Selecting username and filling kun020
b.find_element_by_xpath("//*[@id='username']").send_keys("username")
# Selecting password and filling password
b.find_element_by_xpath('//*[@id="password"]').send_keys("password")
# Selecting schoolName and choosing APS Kunraghat
b.find_element_by_xpath(
    '//*[@id="divSchool"]/div/div[1]/input').send_keys("ARMY PUBLIC SCHOOL KUNRAGHAT", Keys.ENTER)
# Selecting captcha input box
b.find_element_by_xpath('//*[@id="txtCaptcha"]').click()

wait = WebDriverWait(b, 300)
wait.until(EC.title_is(
    "ARMY PUBLIC SCHOOL KUNRAGHAT - APSKUN | ~ TotalES ~"))

b.find_element_by_xpath('//*[@id="nav"]/li[3]/a').click()
b.find_element_by_xpath(
    '//*[@id="dtblStudentAssign"]/tbody/tr/td[7]/button[1]').click()

# os.system('TASKKILL /F /IM chromedriver.exe')
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
# si.wShowWindow = subprocess.SW_HIDE # default
subprocess.call('taskkill /F /IM chromedriver.exe',
                startupinfo=si)  # Closes the program
# except:
#     si = subprocess.STARTUPINFO()
#     si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#     # si.wShowWindow = subprocess.SW_HIDE # default
#     subprocess.call('taskkill /F /IM chromedriver.exe',
#                     startupinfo=si)  # Closes the program
