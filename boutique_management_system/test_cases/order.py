from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(r"C:\Users\Tooba\Desktop\boutique_management_system (2)\boutique_management_system\orders.html")
driver.maximize_window()
time.sleep(2)

print("\nPLACE ORDER PAGE TEST CASES")
print("="*40)

# TC1 - Page Load Test
print("\nRunning TC1 - Page Load Test")
try:
    assert "Place Order" in driver.title or "Boutique" in driver.title
    print("TC1 PASSED ✔")
except:
    print("TC1 FAILED ❌")

# TC2 - All Fields Visible Test
print("\nRunning TC2 - Fields Visible Test")
try:
    driver.find_element(By.ID, "customerName")
    driver.find_element(By.ID, "customerEmail")
    driver.find_element(By.ID, "customerPhone")
    driver.find_element(By.ID, "dressName")
    driver.find_element(By.ID, "quantity")
    driver.find_element(By.ID, "customerAddress")
    print("TC2 PASSED ✔")
except:
    print("TC2 FAILED ❌")

# TC3 - Buttons Visible Test
print("\nRunning TC3 - Buttons Visible Test")
try:
    driver.find_element(By.CLASS_NAME, "submit-btn")
    driver.find_element(By.CLASS_NAME, "reset-btn")
    print("TC3 PASSED ✔")
except:
    print("TC3 FAILED ❌")

# TC4 - Empty Form Submit Test
print("\nRunning TC4 - Empty Form Test")
try:
    driver.find_element(By.ID, "customerName").clear()
    driver.find_element(By.ID, "customerEmail").clear()
    driver.find_element(By.ID, "customerPhone").clear()
    driver.find_element(By.ID, "dressName").clear()
    driver.find_element(By.ID, "quantity").clear()
    driver.find_element(By.ID, "customerAddress").clear()
    
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    time.sleep(1)
    
    alert = driver.switch_to.alert
    assert "Please fill all fields" in alert.text
    alert.accept()
    print("TC4 PASSED ✔")
except:
    print("TC4 FAILED ❌")

# TC5 - Valid Form Submission Test
print("\nRunning TC5 - Valid Form Test")
try:
    driver.find_element(By.ID, "customerName").send_keys("Natasha Khan")
    driver.find_element(By.ID, "customerEmail").send_keys("natasha@gmail.com")
    driver.find_element(By.ID, "customerPhone").send_keys("03182345567")
    driver.find_element(By.ID, "dressName").send_keys("Bridal Dress")
    driver.find_element(By.ID, "quantity").send_keys("2")
    driver.find_element(By.ID, "customerAddress").send_keys("Islamabad")
    
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    time.sleep(1)
    
    alert = driver.switch_to.alert
    assert "Order Placed Successfully" in alert.text
    alert.accept()
    print("TC5 PASSED ✔")
except:
    print("TC5 FAILED ❌")

# TC6 - Clear Button Test
print("\nRunning TC6 - Clear Button Test")
try:
    driver.find_element(By.ID, "customerName").send_keys("Test")
    driver.find_element(By.CLASS_NAME, "reset-btn").click()
    time.sleep(1)
    value = driver.find_element(By.ID, "customerName").get_attribute("value")
    assert value == ""
    print("TC6 PASSED ✔")
except:
    print("TC6 FAILED ❌")

# TC7 - Quantity Field Test
print("\nRunning TC7 - Quantity Field Test")
try:
    field = driver.find_element(By.ID, "quantity")
    field.clear()
    field.send_keys("5")
    assert field.get_attribute("value") == "5"
    print("TC7 PASSED ✔")
except:
    print("TC7 FAILED ❌")

# TC8 - Form Clear After Submit Test
print("\nRunning TC8 - Form Clear After Submit Test")
try:
    name = driver.find_element(By.ID, "customerName").get_attribute("value")
    email = driver.find_element(By.ID, "customerEmail").get_attribute("value")
    assert name == "" and email == ""
    print("TC8 PASSED ✔")
except:
    print("TC8 FAILED ❌")

time.sleep(3)
driver.quit()
print("\nALL TEST CASES EXECUTED")