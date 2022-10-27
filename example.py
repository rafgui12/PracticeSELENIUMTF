import os
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

cwd = os.getcwd()
searchs = ["Hola", "Facebook"]
DirLogFile = f'./Logs.txt'
x = 0

#Create Virtual Display
display = Display(visible=0, size=(1024, 768))
display.start()

## Extra
#Download changes parameters
options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", cwd)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)
while x < len(searchs):
    #Start virtual browser
    driver.get("https://www.google.com/")

    #Search Box 
    SearchInput = driver.find_element(By.NAME, "q")
    SearchInput.send_keys(searchs[x])
    ##Search Button n Action Click 
    SearchBTN = driver.find_element(By.NAME, "btnK")
    SearchBTN.click()

    ##Total Results
    ResultTotal = driver.find_element(By.ID, "result-stats").text

    ###
    print(driver.current_url)
    print("-----------------------------------")
    print(ResultTotal)

    #print(f"Variance is Zero")
    with open(DirLogFile, 'a') as f:
        f.write(f'{searchs[x]},{ResultTotal},{driver.current_url}{os.linesep}')

    #
    x = x+1

driver.close()
driver.quit()
display.stop()