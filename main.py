import os
import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChain

#Navigate to the website
url = "https://labour.gov.in/"
driver = webdriver.Chrome()

driver.get(url)
#Navigate to the Monthly Progress Report page
documents_menu= driver.find_element(By.LINK_TEXT, 'Documents')
action = ActionChain (driver)
action.move_to_element(documents_menu).perform()
time.sleep(1)
monthly_progress_report = driver.find_element(By.LINK_TEXT,'monthly progress report')
monthly_progress_report.click()

#locate the file and click the document

document = driver.find_element(By.XPATH,("//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/")
document.click()

time.sleep(1)

I

#Accept the pop-up dialog

driver.switch_to.alert.accept()

time.sleep(5)

#Download the pdf file to the specified location

pdf_url = driver.current_url

pdf_filename = os.path.join('documents', 'monthly_progress_report.pdf')

urllib.request.urlretrieve(pdf_url, pdf_filename)

driver.close()

driver.switch_to.window(driver.window_handles[0])

time.sleep(2)

driver.quit()
