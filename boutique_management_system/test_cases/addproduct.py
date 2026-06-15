from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(r"C:\Users\Tooba\Desktop\boutique_management_system (2)\boutique_management_system\AddProduct.html")
driver.maximize_window()
time.sleep(2)

print("\nADD PRODUCT PAGE TEST CASES")
print("="*40)

# TC1 - Page Load Test
print("\nRunning TC1 - Page Load Test")
try:
    assert "Add New Product" in driver.title or "Product" in driver.title
    print("TC1 PASSED ✔")
except:
    print("TC1 FAILED ❌")

# TC2 - All Fields Visible Test
print("\nRunning TC2 - Fields Visible Test")
try:
    driver.find_element(By.ID, "productName")
    driver.find_element(By.ID, "price")
    driver.find_element(By.ID, "quantity")
    driver.find_element(By.ID, "category")
    print("TC2 PASSED ✔")
except:
    print("TC2 FAILED ❌")

# TC3 - Buttons Visible Test
print("\nRunning TC3 - Buttons Visible Test")
try:
    driver.find_element(By.CLASS_NAME, "checkout-btn")
    driver.find_element(By.CLASS_NAME, "reset-btn")
    print("TC3 PASSED ✔")
except:
    print("TC3 FAILED ❌")

# TC4 - Empty Form Submit Test
print("\nRunning TC4 - Empty Form Submit Test")
try:
    driver.find_element(By.ID, "productName").clear()
    driver.find_element(By.ID, "price").clear()
    driver.find_element(By.ID, "quantity").clear()
    driver.find_element(By.ID, "category").clear()
    
    driver.find_element(By.CLASS_NAME, "checkout-btn").click()
    time.sleep(1)
    
    alert = driver.switch_to.alert
    assert "Please fill all fields" in alert.text
    alert.accept()
    print("TC4 PASSED ✔")
except:
    print("TC4 FAILED ❌")

# TC5 - Valid Form Submission Test
print("\nRunning TC5 - Valid Form Submission Test")
try:
    driver.find_element(By.ID, "productName").send_keys("Summer Dress")
    driver.find_element(By.ID, "price").send_keys("120")
    driver.find_element(By.ID, "quantity").send_keys("10")
    driver.find_element(By.ID, "category").send_keys("Women")
    
    driver.find_element(By.CLASS_NAME, "checkout-btn").click()
    time.sleep(1)
    
    alert = driver.switch_to.alert
    assert "product added successfully" in alert.text
    alert.accept()
    print("TC5 PASSED ✔")
except:
    print("TC5 FAILED ❌")

# TC6 - Form Clear After Submit Test
print("\nRunning TC6 - Form Clear After Submit Test")
try:
    name = driver.find_element(By.ID, "productName").get_attribute("value")
    price = driver.find_element(By.ID, "price").get_attribute("value")
    assert name == "" and price == ""
    print("TC6 PASSED ✔")
except:
    print("TC6 FAILED ❌")

# TC7 - Reset Button Test
print("\nRunning TC7 - Reset Button Test")
try:
    driver.find_element(By.ID, "productName").send_keys("Test")
    driver.find_element(By.CLASS_NAME, "reset-btn").click()
    time.sleep(1)
    value = driver.find_element(By.ID, "productName").get_attribute("value")
    assert value == ""
    print("TC7 PASSED ✔")
except:
    print("TC7 FAILED ❌")

# TC8 - Product Name Field Test
print("\nRunning TC8 - Product Name Field Test")
try:
    field = driver.find_element(By.ID, "productName")
    field.clear()
    field.send_keys("Bridal Lehenga")
    assert field.get_attribute("value") == "Bridal Lehenga"
    print("TC8 PASSED ✔")
except:
    print("TC8 FAILED ❌")

time.sleep(3)
driver.quit()
print("\nALL TEST CASES EXECUTED")