from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

def get_driver():
    PATH = "C:\\Program Files\\chromedriver\\chromedriver.exe"
    service = Service(PATH)
    driver = webdriver.Chrome(service=service)
    return driver

def main():
    driver = get_driver()
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    sleep(4)

    historical_data = driver.find_element(By.XPATH, "//a[@class='atab index_history_trigger']")
    historical_data.click()
    sleep(4)

    all_data = driver.find_elements(By.XPATH, "//td[@class='st-decimal grow'] | //td[@class='st-decimal drop']")
    all_data_list = []
    sleep(4)
    for data in all_data:
        all_data_list.append(data.text)

    for info in all_data_list:
        with open("Percentage_change.txt", "a") as file:
            file.write(f"{info}\n")

main()