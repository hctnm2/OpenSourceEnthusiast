from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from random import choice

today = date.today().strftime("%d/%m/%Y")

with open("credentials.txt", "r") as f:
    data = f.readlines()
    username = data[3].split("=")[1].split("\n")[0]
    email = data[4].split("=")[1].split("\n")[0]
    number = data[5].split("=")[1].split("\n")[0]
    model = data[6].split("=")[1].split("\n")[0] 
    description = ["My power went out and I couldn't charge my phone. I'm sorry!","I have lost my snapstreak due to unavailability of internet connection. Please assist me in retrieving it.", "Even though we repeatedly snapped each other yesterday and today, our snapstreaks mysteriously vanished and the hourglass icon didn't show up either.", "I was out of town so I couldnt send my streak, kindly recover it", "There has been a fault in Snapchat recently, even though I exchanged snaps with a friend yet my snapstreak has disappeared. Kindly help me retrieve it"]

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://support.snapchat.com/en-US/i-need-help")

# driver.find_element().click()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.page-container div.view-container:nth-child(1) div.ui.container.desktop-navigation:nth-child(3) div.sc-content:nth-child(2) div.fix-a-problem-wizard div.sc-wizard-content.wait-until-loaded.ready div.sc-wizard-question-block:nth-child(1) div.sc-radios div.ui.container.grid.option_wrapper div.sixteen.wide.mobile.eight.wide.computer.column:nth-child(4) div.option label:nth-child(2) > div.sc-radio-circle"))))
# driver.find_element(By.CSS_SELECTOR, "#field-24281229").send_keys(username)
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#field-24281229"))))
driver.find_element(By.CSS_SELECTOR, "#field-24281229").send_keys(username)
driver.find_element(By.CSS_SELECTOR, "#field-24335325").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#field-24369716").send_keys(number)
driver.find_element(By.CSS_SELECTOR, "#field-24369726").send_keys(model)
driver.find_element(By.CSS_SELECTOR, "#field-24326423").send_keys(choice(["yesterday", "today", today]))
driver.find_element(By.CSS_SELECTOR, "#field-24641746").send_keys("929079")
driver.find_element(By.CSS_SELECTOR, "#field-22808619").send_keys(choice(description))
driver.find_element(By.CSS_SELECTOR, "#field-24369736").send_keys(friend) #to be added automagically by main.py
#click on a dropdown menu
driver.find_element(By.CSS_SELECTOR, "div.page-container div.view-container:nth-child(1) div.ui.container.desktop-navigation:nth-child(3) div.sc-content:nth-child(2) div.fix-a-problem-wizard div.sc-wizard-content.wait-until-loaded.ready div.contact-form:nth-child(2) div:nth-child(2) form.ui.form div.field:nth-child(9) div.field.required > div.ui.dropdown.selection:nth-child(2)").click()
driver.find_element(By.XPATH, "//div[contains(text(),'No')]").click()
