# Import required libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from typing import List, Dict


# Configure Chrome options
def configure_chrome_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return options
    """
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    )
    options.add_argument("--disable-blink-features=AutomationControlled")
    """


# Initialize the Chrome driver
def init_driver():
    options = configure_chrome_options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def scraper_producao(ano: int = 2023) -> List[Dict[str, str]]:
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02"
    driver = init_driver()
    driver.get(url)

    try:

        tabela = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        # tabela = driver.find_element(By.TAG_NAME, "table")
        linhas = tabela.find_elements(By.TAG_NAME, "tr")[1:]  # Ignora cabeçalho

        resultados = []
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if len(colunas) >= 2:
                produto = colunas[0].text.strip()
                quantidade_texto = (
                    colunas[1].text.strip().replace(".", "").replace(",", "")
                )
                try:
                    quantidade = int(quantidade_texto)
                except ValueError:
                    quantidade = 0  # Ou `None`, se quiser diferenciar valores inválidos
                dados.append({"produto": produto, "quantidade": quantidade})

        return dados

    except Exception as e:
        print(f"Erro ao fazer scraping: {e}")
        return []

    finally:
        driver.quit()


# Example usage
if __name__ == "__main__":
    resultado = scrape_producao(ano=2023)
    print(resultado)
