from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(r"C:\Users\Tooba\Desktop\boutique_management_system (2)\boutique_management_system\ContactUS.html")
driver.maximize_window()
time.sleep(2)

print("\nCONTACT US PAGE TEST CASES")
print("="*40)

# TC1 - Page Load Test
print("\nRunning TC1 - Page Load Test")
try:
    assert "Contact Us" in driver.title or "Boutique" in driver.title
    print("TC1 PASSED ✔")
except:
    print("TC1 FAILED ❌")

# TC2 - Form Fields Visible Test
print("\nRunning TC2 - Form Fields Test")
try:
    driver.find_element(By.ID, "userName")
    driver.find_element(By.ID, "userEmail")
    driver.find_element(By.ID, "userSubject")
    driver.find_element(By.ID, "userMessage")
    print("TC2 PASSED ✔")
except:
    print("TC2 FAILED ❌")

# TC3 - Empty Form Submit Test
print("\nRunning TC3 - Empty Form Test")
try:
    driver.find_element(By.ID, "userName").clear()
    driver.find_element(By.ID, "userEmail").clear()
    driver.find_element(By.ID, "userSubject").clear()
    driver.find_element(By.ID, "userMessage").clear()
    
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    
    alert = driver.switch_to.alert
    assert "Please enter your name" in alert.text
    alert.accept()
    print("TC3 PASSED ✔")
except:
    print("TC3 FAILED ❌")

# TC4 - Valid Form Submission Test
print("\nRunning TC4 - Valid Form Test")
try:
    driver.find_element(By.ID, "userName").send_keys("Natasha Khan")
    driver.find_element(By.ID, "userEmail").send_keys("natasha@gmail.com")
    driver.find_element(By.ID, "userSubject").send_keys("Order Inquiry")
    driver.find_element(By.ID, "userMessage").send_keys("I want to order a bridal dress")
    
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    
    alert = driver.switch_to.alert
    assert "Thank you" in alert.text
    alert.accept()
    print("TC4 PASSED ✔")
except:
    print("TC4 FAILED ❌")

# TC5 - Form Clear After Submit Test
print("\nRunning TC5 - Form Clear Test")
try:
    name = driver.find_element(By.ID, "userName").get_attribute("value")
    email = driver.find_element(By.ID, "userEmail").get_attribute("value")
    assert name == "" and email == ""
    print("TC5 PASSED ✔")
except:
    print("TC5 FAILED ❌")

# TC6 - Clear Button Test
print("\nRunning TC6 - Clear Button Test")
try:
    driver.find_element(By.ID, "userName").send_keys("Test")
    driver.find_element(By.CLASS_NAME, "reset-btn").click()
    time.sleep(1)
    value = driver.find_element(By.ID, "userName").get_attribute("value")
    assert value == ""
    print("TC6 PASSED ✔")
except:
    print("TC6 FAILED ❌")

# TC7 - Contact Info Test
print("\nRunning TC7 - Contact Info Test")
try:
    page = driver.page_source
    assert "boutique@gmail.com" in page
    assert "0318-2345567" in page
    print("TC7 PASSED ✔")
except:
    print("TC7 FAILED ❌")

time.sleep(3)
driver.quit()
print("\nALL TEST CASES EXECUTED")