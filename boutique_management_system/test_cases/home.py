from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(r"C:\Users\Tooba\Desktop\boutique_management_system (2)\boutique_management_system\home.html")
driver.maximize_window()
time.sleep(2)

print("\nHOME PAGE TEST CASES")
print("="*40)

# TC1 - Page Load Test
print("\nRunning TC1 - Page Load Test")
try:
    assert "Boutique - Home" in driver.title or "Home" in driver.title
    print("TC1 PASSED ✔")
except:
    print("TC1 FAILED ❌")

# TC2 - Welcome Section Test
print("\nRunning TC2 - Welcome Section Test")
try:
    driver.find_element(By.CLASS_NAME, "welcome-section")
    print("TC2 PASSED ✔")
except:
    print("TC2 FAILED ❌")

# TC3 - Image Display Test
print("\nRunning TC3 - Image Display Test")
try:
    img = driver.find_element(By.ID, "sliderImage")
    assert img.is_displayed()
    print("TC3 PASSED ✔")
except:
    print("TC3 FAILED ❌")

# TC4 - Play Button Test
print("\nRunning TC4 - Play Button Test")
try:
    driver.find_element(By.XPATH, "//button[contains(text(), 'PLAY')]")
    print("TC4 PASSED ✔")
except:
    print("TC4 FAILED ❌")

# TC5 - Pause Button Test
print("\nRunning TC5 - Pause Button Test")
try:
    driver.find_element(By.XPATH, "//button[contains(text(), 'PAUSE')]")
    print("TC5 PASSED ✔")
except:
    print("TC5 FAILED ❌")

# TC6 - Image Change Test
print("\nRunning TC6 - Image Change Test")
try:
    img = driver.find_element(By.ID, "sliderImage")
    first = img.get_attribute("src")
    time.sleep(3)
    second = img.get_attribute("src")
    assert first != second
    print("TC6 PASSED ✔")
except:
    print("TC6 FAILED ❌")

# TC7 - Pause Button Test
print("\nRunning TC7 - Pause Button Test")
try:
    pause = driver.find_element(By.XPATH, "//button[contains(text(), 'PAUSE')]")
    pause.click()
    first = driver.find_element(By.ID, "sliderImage").get_attribute("src")
    time.sleep(3)
    second = driver.find_element(By.ID, "sliderImage").get_attribute("src")
    assert first == second
    print("TC7 PASSED ✔")
except:
    print("TC7 FAILED ❌")

# TC8 - Navigation Test
print("\nRunning TC8 - Navigation Test")
try:
    links = driver.find_elements(By.CSS_SELECTOR, ".navbar a")
    assert len(links) >= 7
    print("TC8 PASSED ✔")
except:
    print("TC8 FAILED ❌")

time.sleep(3)
driver.quit()
print("\nALL TEST CASES EXECUTED")