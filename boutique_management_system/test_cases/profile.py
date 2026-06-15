from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(r"C:\Users\Tooba\Desktop\boutique_management_system (2)\boutique_management_system\Profile.html")
driver.maximize_window()
time.sleep(2)

print("\nPROFILE PAGE TEST CASES")
print("="*40)

# TC1 - Page Load Test
print("\nRunning TC1 - Page Load Test")
try:
    assert "Boutique Profile" in driver.title or "Profile" in driver.title
    print("TC1 PASSED ✔")
except:
    print("TC1 FAILED ❌")

# TC2 - Page Heading Test
print("\nRunning TC2 - Page Heading Test")
try:
    heading = driver.find_element(By.TAG_NAME, "h1")
    assert "Boutique Management System" in heading.text
    print("TC2 PASSED ✔")
except:
    print("TC2 FAILED ❌")

# TC3 - Navigation Bar Test
print("\nRunning TC3 - Navigation Test")
try:
    links = driver.find_elements(By.CSS_SELECTOR, ".navbar a")
    assert len(links) >= 7
    print("TC3 PASSED ✔")
except:
    print("TC3 FAILED ❌")

# TC4 - About Section Test
print("\nRunning TC4 - About Section Test")
try:
    page = driver.page_source
    assert "Attiqa, Natasha & Tooba" in page
    assert "Since 2026" in page
    print("TC4 PASSED ✔")
except:
    print("TC4 FAILED ❌")

# TC5 - Services and Offers Test
print("\nRunning TC5 - Services Test")
try:
    page = driver.page_source
    assert "Bridal Dresses" in page
    assert "Party Wear" in page
    assert "20% Off" in page or "Summer Sale" in page
    print("TC5 PASSED ✔")
except:
    print("TC5 FAILED ❌")

# TC6 - Footer Test
print("\nRunning TC6 - Footer Test")
try:
    page = driver.page_source
    assert "boutique@gmail.com" in page
    assert "0318-2345567" in page
    print("TC6 PASSED ✔")
except:
    print("TC6 FAILED ❌")

time.sleep(3)
driver.quit()
print("\nALL TEST CASES EXECUTED")