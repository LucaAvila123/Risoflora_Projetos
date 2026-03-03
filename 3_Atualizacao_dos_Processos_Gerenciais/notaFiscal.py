import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def elemento_existe(driver, by, seletor):
    """Verifica se um elemento existe sem lançar exceção"""
    try:
        driver.find_element(by, seletor)
        return True
    except NoSuchElementException:
        return False

def first_test_script():
    # Create an instance of the Chrome WebDriver
    # you can use other browsers too
    driver = webdriver.Chrome()
    
    # navigate to the website
    driver.get("https://app.sefaz.es.gov.br/ConsultaNFCe/")
    
    # Get the actual title of the page
    title = driver.title
    
    # Print the title of the website
    print("Title: " + title)
    campo_input = driver.find_element(By.NAME, "ctl00$body$txtConsulta")
    print("Campo input: ", campo_input)

    campo_input.send_keys(numero_nota_fiscal)
    
    time.sleep(3)
    # Close the browser window
    driver.quit()
    



if     __name__ == "__main__":
    first_test_script()
