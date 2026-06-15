from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(r"C:\Users\Tooba\Desktop\boutique_management_system (2)\boutique_management_system\cart.html")
driver.maximize_window()
time.sleep(2)

print("\nSHOPPING CART PAGE TEST CASES")
print("="*40)

# TC1 - Page Load Test
print("\nRunning TC1 - Page Load Test")
try:
    assert "Shopping Cart" in driver.title or "Cart" in driver.title
    print("TC1 PASSED ✔")
except:
    print("TC1 FAILED ❌")

# TC2 - Cart Items Display Test
print("\nRunning TC2 - Cart Items Test")
try:
    rows = driver.find_elements(By.CSS_SELECTOR, "#cartBody tr")
    assert len(rows) >= 2
    print("TC2 PASSED ✔")
except:
    print("TC2 FAILED ❌")

# TC3 - Increase Quantity Test
print("\nRunning TC3 - Increase Quantity Test")
try:
    plus_btn = driver.find_element(By.XPATH, "//button[text()='+']")
    plus_btn.click()
    time.sleep(1)
    print("TC3 PASSED ✔")
except:
    print("TC3 FAILED ❌")

# TC4 - Remove Item Test
print("\nRunning TC4 - Remove Item Test")
try:
    initial = len(driver.find_elements(By.CSS_SELECTOR, "#cartBody tr"))
    driver.find_element(By.CLASS_NAME, "remove-btn").click()
    time.sleep(1)
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    new = len(driver.find_elements(By.CSS_SELECTOR, "#cartBody tr"))
    assert new < initial
    print("TC4 PASSED ✔")
except:
    print("TC4 FAILED ❌")

# TC5 - Grand Total Test
print("\nRunning TC5 - Grand Total Test")
try:
    total = driver.find_element(By.ID, "grandTotal")
    assert "$" in total.text
    print("TC5 PASSED ✔")
except:
    print("TC5 FAILED ❌")

# TC6 - Empty Cart Checkout Test
print("\nRunning TC6 - Empty Cart Checkout Test")
try:
    btns = driver.find_elements(By.CLASS_NAME, "remove-btn")
    for btn in btns:
        btn.click()
        time.sleep(0.5)
        try:
            driver.switch_to.alert.accept()
        except:
            pass
    
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "checkout-btn").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    assert "empty" in alert.text.lower()
    alert.accept()
    print("TC6 PASSED ✔")
except:
    print("TC6 FAILED ❌")

time.sleep(3)
driver.quit()
print("\nALL TEST CASES EXECUTED")