from typing import List, Optional

import requests
from bs4 import BeautifulSoup

from app.models import schema
from app.utils.scraper_helper import parse_table_by_model
from app.utils.url_helper import get_url


def fetch_table_data(option: str, suboption: Optional[str], year: int, model):
    url = get_url(option, suboption, year)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    return parse_table_by_model(table, model, year, suboption)


def get_production_data(
    option: str, suboption: Optional[str], year: int
) -> List[schema.ProductionItem]:
    """
    Faz scraping da aba de Produção da Embrapa e retorna os dados como lista de
    ProductionItem.
    """
    return fetch_table_data(option, suboption, year, schema.ProductionItem)


def get_processing_data(
    option: str, suboption: Optional[str], year: int
) -> List[schema.ProcessingItem]:
    """
    Faz scraping da aba de Processamento da Embrapa e retorna os dados como lista de
    ProcessingItem.
    """
    return fetch_table_data(option, suboption, year, schema.ProcessingItem)


def get_commercial_data(
    option: str, suboption: Optional[str], year: int
) -> List[schema.CommercialItem]:
    """
    Faz scraping da aba de Comercialização da Embrapa e retorna os dados como lista de
    CommercialItem.
    """
    return fetch_table_data(option, suboption, year, schema.CommercialItem)


def get_import_data(
    option: str, suboption: Optional[str], year: int
) -> List[schema.ImportItem]:
    """
    Faz scraping da aba de Importação da Embrapa e retorna os dados como lista de
    ImportItem.
    """
    return fetch_table_data(option, suboption, year, schema.ImportItem)


def get_export_data(
    option: str, suboption: Optional[str], year: int
) -> List[schema.ExportItem]:
    """
    Faz scraping da aba de Exportação da Embrapa e retorna os dados como lista de
    ExportItem.
    """
    return fetch_table_data(option, suboption, year, schema.ExportItem)
