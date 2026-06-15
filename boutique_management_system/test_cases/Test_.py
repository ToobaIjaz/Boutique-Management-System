from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(r"C:\Users\Tooba\Desktop\boutique_management_system (2)\boutique_management_system\login.html")
driver.maximize_window()
time.sleep(2)

# TC1 - Page Load Test
print("\nRunning TC1 - Page Load Test")
try:
    assert "Boutique Login" in driver.title
    print("TC1 PASSED ✔")
except:
    print("TC1 FAILED ❌")

# TC2 - Username Input Test
print("\nRunning TC2 - Username Input Test")
try:
    username = driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("Natasha123")
    assert username.get_attribute("value") == "Natasha123"
    print("TC2 PASSED ✔")
except:
    print("TC2 FAILED ❌")

# TC3 - Email Input Test
print("\nRunning TC3 - Email Input Test")
try:
    email = driver.find_element(By.ID, "email")
    email.clear()
    email.send_keys("natasha@gmail.com")
    assert email.get_attribute("value") == "natasha@gmail.com"
    print("TC3 PASSED ✔")
except:
    print("TC3 FAILED ❌")

# TC4 - Password Input Test
print("\nRunning TC4 - Password Input Test")
try:
    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys("Password123!")
    assert password.get_attribute("value") == "Password123!"
    print("TC4 PASSED ✔")
except:
    print("TC4 FAILED ❌")

# TC5 - Valid Form Submission (jQuery Dialog)
print("\nRunning TC5 - Valid Form Submission Test")
try:
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys("Natasha123")
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys("natasha@gmail.com")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("Password123!")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    time.sleep(1)
    dialog = driver.find_element(By.CLASS_NAME, "ui-dialog-titlebar")
    assert dialog.is_displayed()
    driver.find_element(By.CLASS_NAME, "ui-dialog-titlebar-close").click()
    print("TC5 PASSED ✔")
except:
    print("TC5 FAILED ❌")

# TC6 - Invalid Email Test
print("\nRunning TC6 - Invalid Email Test")
try:
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys("Natasha123")
    driver.find_element(By.ID, "email").send_keys("wrongemail")
    driver.find_element(By.ID, "password").send_keys("Password123!")
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "emailError").text
    assert result == "Enter a valid email address."
    print("TC6 PASSED ✔")
except:
    print("TC6 FAILED ❌")

# TC7 - Empty Form Validation
print("\nRunning TC7 - Empty Form Validation Test")
try:
    driver.refresh()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "usernameError").text
    assert result == "Username is required."
    print("TC7 PASSED ✔")
except:
    print("TC7 FAILED ❌")

# TC8 - Reset Button Test
print("\nRunning TC8 - Reset Button Test")
try:
    driver.refresh()
    time.sleep(1)
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("Natasha123")
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("natasha@gmail.com")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123!")
    driver.find_element(By.CLASS_NAME, "reset-btn").click()
    time.sleep(1)
    assert username_field.get_attribute("value") == ""
    assert email_field.get_attribute("value") == ""
    assert password_field.get_attribute("value") == ""
    print("TC8 PASSED ✔")
except:
    print("TC8 FAILED ❌")

# TC9 - Element Visibility Test
print("\nRunning TC9 - Element Visibility Test")
try:
    assert driver.find_element(By.ID, "username").is_displayed()
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()
    print("TC9 PASSED ✔")
except:
    print("TC9 FAILED ❌")

# TC10 - Button Visibility Test
print("\nRunning TC10 - Button Visibility Test")
try:
    assert driver.find_element(By.CLASS_NAME, "submit-btn").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "reset-btn").is_displayed()
    print("TC10 PASSED ✔")
except:
    print("TC10 FAILED ❌")

time.sleep(3)
driver.quit()
print("\nALL TEST CASES EXECUTED")