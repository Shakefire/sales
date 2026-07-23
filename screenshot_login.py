import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")

service = webdriver.EdgeService(
    executable_path=r"C:\Users\user\.cache\selenium\msedgedriver\win64\150.0.4078.83\msedgedriver.exe"
)
driver = webdriver.Edge(options=options, service=service)
try:
    # 1. Desktop view
    driver.set_window_size(1440, 900)
    driver.get("http://127.0.0.1:8000/login/?next=/")
    time.sleep(1.2)
    driver.save_screenshot("screenshots/login_new_desktop.png")

    # 2. Error state (bad credentials)
    driver.find_element(By.ID, "id_username").send_keys("wronguser")
    driver.find_element(By.ID, "id_password").send_keys("wrongpass")
    driver.find_element(By.ID, "btn-login").click()
    time.sleep(1.2)
    driver.save_screenshot("screenshots/login_new_error.png")
    repopulated = driver.find_element(By.ID, "id_username").get_attribute("value")
    print("username repopulated after failed login:", repopulated == "wronguser")

    # 3. Mobile view
    driver.set_window_size(390, 844)
    driver.get("http://127.0.0.1:8000/login/?next=/")
    time.sleep(1.2)
    driver.save_screenshot("screenshots/login_new_mobile.png")

    print("screenshots saved")
finally:
    driver.quit()
