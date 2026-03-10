import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import re
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_session():
        try: 
            sess = uc.Chrome()
        except Exception as e: 
            main_version_string = re.search(r"Current browser version is (\d+\.\d+\.\d+)", str(e)).group(1)
            main_version = int(main_version_string.split(".")[0])
            sess = uc.Chrome(version_main=main_version)
        return sess

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
    wait = WebDriverWait(driver, 10)
    try:
        # Aguardar o campo de input estar presente
        campo_input = wait.until(
            EC.presence_of_element_located((By.NAME, "ctl00$body$txtConsulta"))
        )
        print("Campo input encontrado")
        campo_input.send_keys(numero_nota_fiscal)
        
        # Aguardar o botão estar clicável
        botao_input = wait.until(
            EC.element_to_be_clickable((By.NAME, "ctl00$body$Button1"))
        )
        print("Botão encontrado e clicável")
        
        # Tentar diferentes métodos de clique
        try:
            botao_input.click()
            print("Clique realizado com sucesso")
        except:
            # Se o clique normal falhar, tentar com JavaScript
            driver.execute_script("arguments[0].click();", botao_input)
            print("Clique realizado via JavaScript")
        
        # Aguardar a próxima página carregar
        time.sleep(5)
        
    except TimeoutException:
        print("Timeout ao esperar pelos elementos")
    except Exception as e:
        print(f"Erro durante a execução: {e}")
    # driver.quit()

if     __name__ == "__main__":
    nota_fiscal = int(input())
    first_test_script(nota_fiscal)
