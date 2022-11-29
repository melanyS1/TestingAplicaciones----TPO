from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import perf_counter

tiempo=3
d=webdriver.Chrome(executable_path=r"C:\melany_serquen\chromedriver.exe")
d.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/")
d.maximize_window()
time.sleep(7)
usr=d.find_element(By.XPATH, "//input[@id='email']").send_keys("serquenmelany.b@gmail.com")
time.sleep(tiempo)
pw=d.find_element(By.XPATH, "//input[@name='login[password]']").send_keys("Melanyserquen1")
time.sleep(tiempo)
btn=d.find_element(By.XPATH, "//button[@class='action login primary']")
btn.click()
time.sleep(7)
d.close()