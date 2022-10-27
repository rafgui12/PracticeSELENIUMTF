from pyvirtualdisplay import Display
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

DirLogFile = f'./Logs.txt'

display = Display(visible=0, size=(1024,768))
display.start()

driver = webdriver.Firefox()
driver.get("https://www.google.com")

searchInput = driver.find_element(By.NAME, "q")
searchInput.send_keys('hello') 

btSearch = driver.find_element(By.NAME, "btnK")
btSearch.click()

resultTotal = driver.find_element(By.ID, "result-stats").text

#print(f"Variance is Zero")
with open(DirLogFile, 'a') as f:
    f.write(f'Hello,{resultTotal},{driver.current_url}{os.linesep}')

print(driver.current_url)
print(resultTotal)

driver.close()
driver.quit()
display.stop()




