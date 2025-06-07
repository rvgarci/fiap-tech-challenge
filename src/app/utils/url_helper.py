from typing import Optional
from app.utils.router_config import ROUTER_CONFIG


def get_url(option: str, suboption: Optional[str], year: int) -> str:
    """
    Gera a URL de scraping para a aba da Embrapa conforme a opção, subopção e ano.

    Args:
        option: Nome da aba (ex: "produção", "exportação")
        suboption: Subcategoria (ex: "vinhos de mesa")
        year: Ano da consulta (ex: 2023)

    Returns:
        URL montada como string.
    """
    base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php"

    if option not in ROUTER_CONFIG:
        raise ValueError(f"Invalid option: {option}")

    config = ROUTER_CONFIG[option]
    opt_code = config["option"]

    # Validação do ano
    if year not in config["year"]:
        raise ValueError(f"Invalid year: {year} for option '{option}'")

    # Se não houver subopções definidas
    if config["suboption"] is None:
        return f"{base_url}?opcao={opt_code}&ano={year}"

    # Se houver subopções, mas não foi passado nenhuma
    if suboption is None:
        raise ValueError(f"Suboption is required for option '{option}'")

    # Validação da subopção
    suboptions = config["suboption"]
    if suboption not in suboptions:
        raise ValueError(f"Invalid suboption: '{suboption}' para a opção '{option}'")

    subopt_code = suboptions[suboption]
    return f"{base_url}?opcao={opt_code}&subopcao={subopt_code}&ano={year}"
