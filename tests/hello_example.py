from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


options = Options()
options.add_argument("--headless")


driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)


try:
    driver.get("http://aut-container")

    print("Page title:", driver.title)

    assert "Welcome" in driver.page_source

    print("TEST PASSED")

finally:
    driver.quit()