import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import re
import undetected_chromedriver as uc

def initialize_session():
        try: 
            sess = uc.Chrome()
        except Exception as e: 
            main_version_string = re.search(r"Current browser version is (\d+\.\d+\.\d+)", str(e)).group(1)
            main_version = int(main_version_string.split(".")[0])
            sess = uc.Chrome(version_main=main_version)
        return sess

def elemento_existe(driver, by, seletor):
    """Verifica se um elemento existe sem lançar exceção"""
    try:
        driver.find_element(by, seletor)
        return True
    except NoSuchElementException:
        return False

def first_test_script(numero_nota_fiscal):
    # Create an instance of the Chrome WebDriver
    # you can use other browsers too
    
    driver = initialize_session()
    
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

    botao_input = driver.find_element(By.NAME, "ctl00$body$Button1")
    botao_input.click()
    time.sleep(3)

    driver.quit()

if     __name__ == "__main__":
    # nota_fiscal = input("Insira numero da nota Fiscal no formato apropriado: ")
    first_test_script(nota_fiscal)
