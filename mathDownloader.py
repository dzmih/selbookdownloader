from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://flibusta.is/")
driver.find_element(By.PARTIAL_LINK_TEXT, "Жанры").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Математика").click()


links = driver.find_elements(By.XPATH, "//ol//a[not(ancestor::h5)]")
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

for l in links:
    try:
        l.click()

        time.sleep(0.5)

        try:
            download_link = driver.find_element(By.PARTIAL_LINK_TEXT, "скачать")
            if "pdf" in download_link.text:
                download_link.click()
                print("Ссылка на скачивание PDF была нажата.")
        except NoSuchElementException:
            print("Ссылка на скачивание не найдена на этой странице.")

        driver.back()

        time.sleep(0.5)
        links = driver.find_elements(By.TAG_NAME, "a")
    except StaleElementReferenceException:
        print("Элемент устарел. Пропускаем.")
        continue




