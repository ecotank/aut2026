from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.FirefoxOptions()
options.add_argument("--headless")


driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)


try:
    # membuka halaman AUT
    driver.get("http://localhost:8081")

    time.sleep(3)

    # mengambil judul halaman
    title = driver.title

    print("Title halaman AUT:", title)

    # validasi sederhana
    assert title != ""

    print("Testing AUT berhasil")


finally:
    driver.quit()