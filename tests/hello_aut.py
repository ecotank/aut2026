from selenium import webdriver
import time


options = webdriver.FirefoxOptions()
options.add_argument("--headless")


driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)


try:

    driver.get("http://aut-container")

    time.sleep(5)

    print("URL:", driver.current_url)
    print("TITLE:", driver.title)

    assert driver.current_url.startswith("http")

    print("AUT Testing Success")


finally:

    driver.save_screenshot("screenshot.png")

    driver.quit()