from selenium import webdriver
import time
def main():
    #driverPath = r"/Users/cheuklamyuen/Documents/liker/chromedriver_mac"
    driver = webdriver.Chrome(executable_path=r"/Users/cheuklamyuen/Documents/popcat_clicker/chromedriver_mac") # Chrome
    driver.get("https://popcat.click/")
    while True: 
        driver.find_element_by_xpath("//*[@id='app']").click()

    

main()
