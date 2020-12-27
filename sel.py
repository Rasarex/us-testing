from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time 
def test_all_groups(driver):
    dates = ["10-10-2018","10-10-2009","10-10-2008","10-10-2005","10-10-1999","10-10-1920"] #all dates representing each group once
    tickboxes=[[0,0],[0,1],[1,0],[1,1]] #possible combinations /  0 is false as in unticked 1 is true as in ticked
    expected_res = [
        "Brak kwalifikacji",
        "Brak kwalifikacji",
        "Brak kwalifikacji",
        "Brak kwalifikacji",
        "Blad danych",
        "Blad danych",
        "Blad danych",
        "Skrzat",
        "Blad danych",
        "Blad danych",
        "Blad danych",
        "Mlodzik",
        "Blad danych",
        "Blad danych",
        "Blad danych",
        "Junior",
        "Dorosly",
        "Dorosly",
        "Dorosly",
        "Dorosly",
        "Blad danych",
        "Senior",
        "Blad danych",
        "Senior"
    ] # valid results
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[])
    i = 0
    for date in dates:
        for ticks in tickboxes:            
            test_group(driver,date,ticks[0],ticks[1])
            
            alert  = wait.until(expected_conditions.alert_is_present())
            alert.accept() #skip date calculation alert
            
            alert = wait.until(expected_conditions.alert_is_present())
            assert alert.text == expected_res[i] #check if result is the same as expected
            i += 1
            alert.accept()
            

def test_group(driver,date,parents,doctor):
    """
    type in sample data 
    """
    driver.find_element_by_id("inputEmail3").send_keys(Keys.BACKSPACE +  "a" + Keys.RETURN)
    driver.find_element_by_id("inputPassword3").send_keys(Keys.BACKSPACE + "a" + Keys.RETURN)
    """
    type in date to be tested
    """
    driver.find_element_by_id("dataU").clear()
    driver.find_element_by_id("dataU").send_keys(date + Keys.RETURN)

    
    parentchbx = driver.find_element_by_id("rodzice")
    doctorchbx  = driver.find_element_by_id("lekarz")
    """
    untick already ticked checkboxes
    """
    if parentchbx.is_selected():
        parentchbx.click()
    if doctorchbx.is_selected():
        doctorchbx.click()

    """
    tick checkboxes 
    """
    if parents:
        driver.find_element_by_id("rodzice").click()
    if doctor:
        driver.find_element_by_id("lekarz").click()
    """
    Send
    """
    driver.find_element_by_class_name("btn").click()

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(options=options)
driver.get('https://lamp.ii.us.edu.pl/~mtdyd/zawody/')

test_all_groups(driver)
driver.close()
