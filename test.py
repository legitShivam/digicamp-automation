import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random

options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging', 'enable-automation'])

b = webdriver.Chrome(
    executable_path=r"C:\Users\dell\Downloads\Compressed\chromedriver.exe", options=options)  # This will download chromedriver if it is not available.
b.maximize_window()
# This line will make sure that this program waits for max 5s if the effect of a code is taking time to display
b.implicitly_wait(10)

# Opening Digicamp website on Chrome
b.get("https://www.apsdigicamp.com/")

b.find_element_by_class_name("loginbut").click()  # login button
b.find_element_by_xpath(  # Teachers button
    "//*[@id='login-modal']/div/div/div/div/div/div/div/div[1]/div/a[2]").click()

# Selecting username and filling kun020
b.find_element_by_xpath("//*[@id='username']").send_keys("kun020")
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





b.get("https://www.apsdigicamp.com/school/teacher-profile/attendance/entry/GEN_2020-21_APSKUN~VII_2020-21_APSKUN~D_2020-21_APSKUN~ATTN_2020-21_APSKUN")

checkBoxByRollNo1 = '//*[@id="chk1' # Remove 1
checkBoxByRollNo2 = '"]'

wait = WebDriverWait(b, 300)
wait.until(EC.title_is("Attendance - Entry"))


#month selector
b.find_element_by_id( 'txtAttdDate').click()
# b.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/a[1]').click()
# b.find_element_by_xpath(  '//*[@id="chk9"]').click()




starttd = 2
endtd = 3
dateXpath1 = '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[3]/a'

# tcStudents = [1, 26, 32]

rollNos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47]
chutti = [1,2,3,4,5,6,7,8,9,14,21]

output = {}
time
for tr in range(1, 6):
	if tr == 1:
		for td in range(starttd, 8):
			if td != starttd:
				# Month selector
				b.find_element_by_id( 'txtAttdDate').click()

			abStudentsList = []
			dt = b.find_element_by_xpath(f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{tr}]/td[{td}]/a')
			dt.click()
			date = dt.get_attribute("text")
			if not date in chutti:
				# Code here 
				time.sleep(1)
				abStudents = random.choice(range(1, 5))
				for _ in range(abStudents):
					rollNo = random.choice(rollNos)
					if rollNo >= 16:
						abStudentsList.append(rollNo+1)
					else:
						abStudentsList.append(rollNo)
					b.find_element_by_xpath( f'//*[@id="chk{rollNo}"]').click()

				time.sleep(1)
				output[f'Date - {date}-09-20'] = f'RollNo = {abStudentsList}, Total Absent = {abStudents}'
				print(output)
				b.find_element_by_xpath('//*[@id="btnSave"]').click()
				
	elif tr == 6:
		for td in range(endtd, endtd+1):
			b.find_element_by_id( 'txtAttdDate').click()

			abStudentsList = []
			dt = b.find_element_by_xpath(f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{tr}]/td[{td}]/a')
			dt.click()
			date = dt.get_attribute("text")
			if not date in chutti:
				#code here 
				time.sleep(1)
				abStudents = random.choice(range(1, 5))
				for _ in range(abStudents):
					rollNo = random.choice(rollNos)
					if rollNo >= 16:
						abStudentsList.append(rollNo+1)
					else:
						abStudentsList.append(rollNo)
					b.find_element_by_xpath( f'//*[@id="chk{rollNo}"]').click()

				time.sleep(1)
				output[f'Date - {date}-09-20'] = f'RollNo = {abStudentsList}, Total Absent = {abStudents}'
				print(output)
				b.find_element_by_xpath('//*[@id="btnSave"]').click()
				
	else:
		for td in range(2, 8):
			b.find_element_by_id( 'txtAttdDate').click()

			abStudentsList = []
			dt = b.find_element_by_xpath(f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{tr}]/td[{td}]/a')
			dt.click()
			date = dt.get_attribute("text")
			if not date in chutti:
				#code here 
				time.sleep(1)
				abStudents = random.choice(range(1, 5))
				for _ in range(abStudents):
					rollNo = random.choice(rollNos)
					if rollNo >= 16:
						abStudentsList.append(rollNo+1)
					else:
						abStudentsList.append(rollNo)
					b.find_element_by_xpath( f'//*[@id="chk{rollNo}"]').click()

				time.sleep(1)
				output[f'Date - {date}-09-20'] = f'RollNo = {abStudentsList},\tTotal Absent = {abStudents}'
				print(output)
				b.find_element_by_xpath('//*[@id="btnSave"]').click()
				


# for key, value in output.items():
# 	print(key, '/\t', value)







# os.system('TASKKILL /F /IM chromedriver.exe')
# si = subprocess.STARTUPINFO()
# si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
# # si.wShowWindow = subprocess.SW_HIDE # default
# subprocess.call('taskkill /F /IM chromedriver.exe',
#                 startupinfo=si)  # Closes the program