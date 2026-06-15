from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(r"C:\Users\Tooba\Desktop\boutique_management_system (2)\boutique_management_system\About.html")
driver.maximize_window()
time.sleep(2)

print("\nABOUT US PAGE TEST CASES")
print("="*40)

# TC1 - Page Load Test
print("\nRunning TC1 - Page Load Test")
try:
    assert "About Us" in driver.title or "Boutique" in driver.title
    print("TC1 PASSED ✔")
except:
    print("TC1 FAILED ❌")

# TC2 - Navigation Bar Test
print("\nRunning TC2 - Navigation Bar Test")
try:
    nav_links = driver.find_elements(By.CSS_SELECTOR, ".navbar a")
    assert len(nav_links) >= 7
    print("TC2 PASSED ✔")
except:
    print("TC2 FAILED ❌")

# TC3 - Heading Test
print("\nRunning TC3 - Heading Test")
try:
    driver.find_element(By.TAG_NAME, "h2")
    print("TC3 PASSED ✔")
except:
    print("TC3 FAILED ❌")

# TC4 - Images Test
print("\nRunning TC4 - Images Test")
try:
    images = driver.find_elements(By.TAG_NAME, "img")
    assert len(images) >= 3
    print("TC4 PASSED ✔")
except:
    print("TC4 FAILED ❌")

# TC5 - Our Story Section Test
print("\nRunning TC5 - Our Story Section Test")
try:
    driver.find_element(By.XPATH, "//h3[contains(text(), 'Our Story')]")
    print("TC5 PASSED ✔")
except:
    print("TC5 FAILED ❌")

# TC6 - Services Section Test
print("\nRunning TC6 - Services Section Test")
try:
    driver.find_element(By.XPATH, "//h3[contains(text(), 'Our Services')]")
    print("TC6 PASSED ✔")
except:
    print("TC6 FAILED ❌")

# TC7 - Special Offer Test
print("\nRunning TC7 - Special Offer Test")
try:
    page_text = driver.page_source
    assert "20% OFF" in page_text or "Summer Sale" in page_text
    print("TC7 PASSED ✔")
except:
    print("TC7 FAILED ❌")

# TC8 - Footer Test
print("\nRunning TC8 - Footer Test")
try:
    driver.find_element(By.CLASS_NAME, "footer")
    print("TC8 PASSED ✔")
except:
    print("TC8 FAILED ❌")

time.sleep(3)
driver.quit()
print("\nALL TEST CASES EXECUTED")