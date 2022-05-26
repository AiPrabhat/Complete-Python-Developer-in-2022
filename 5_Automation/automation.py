from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:/Users/gprab/Documents/Complete Python Developer in 2022/Automation/chromedriver.exe')

driver.maximize_window()
driver.get('https://demo.anhtester.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in driver.title
assert 'Show Message' in driver.page_source

user_message = driver.find_element(by=By.ID, value='user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOL')

show_message = driver.find_element(by=By.CLASS_NAME, value='btn-default')
show_message.click()

output_message = driver.find_element(by=By.ID, value='display')

assert 'I AM EXTRA COOOL' in output_message.text


# driver.close()