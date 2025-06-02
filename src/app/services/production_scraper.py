import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from utils.url_helper import get_url


def get_production_data(option: str, suboption: Optional[str], year: int) -> List[Dict[str, str]]:
    """
    Scrapes production data from the Embrapa website for the year 1985.
    Returns a list of dictionaries containing the type, product, and quantity.
    """
    # URL for the production data of the year 1985

    url = get_url(option, suboption, year)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", class_="tb_base tb_dados")

    data = []

    for row in table.find_all("tr"):

        cells = row.find_all("td")

        if not cells:
            continue

        cell_class = cells[0].get("class", [])

        if "tb_item" in cell_class:
            tipo = cells[0].text.strip()
        elif "tb_subitem" in cell_class:
            produto = cells[0].text.strip()
            quantidade = (cells[1].text.strip().replace("-", "0").replace(".", "").replace(",", "."))
            data.append({"tipo": tipo, "produto": produto, "quantidade": quantidade})

    for row in data:
        print(row)
    
    return data

if __name__ == "__main__":
    # Example usage
    option = "producao"
    suboption = None
    year = 1985
    production_data = get_production_data(option, suboption, year)
    print(production_data)