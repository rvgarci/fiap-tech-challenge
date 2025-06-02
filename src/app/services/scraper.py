import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from app.utils.scraper_helper import parse_table
from app.utils.url_helper import get_url


def get_production_data(option: str, suboption: Optional[str], year: int) -> List[Dict[str, str]]:
    
    # url = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano=1985&opcao=opt_02"
    
    url = get_url(option, suboption, year)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    data = parse_table(table)

    return data

if __name__ == "__main__":
    option = "producao"
    suboption = None
    year = 1985
    production_data = get_production_data(option, suboption, year)
    for row in production_data:
        print(row)