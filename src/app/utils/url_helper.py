from typing import Optional
from config_routers import ROUTE_CONFIG

def get_url(option: str, suboption: Optional[str], year: int) -> str:
    if option not in ROUTE_CONFIG:
        raise ValueError(f"Invalid option: '{option}'")

    config = ROUTE_CONFIG[option]
    opt_code = config["option"]

    # Validação do ano
    if year not in config["year"]:
        raise ValueError(f"Invalid year: {year} for option '{option}'")

    # Se não houver subopções definidas
    if config["suboption"] is None:
        return f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={opt_code}&ano={year}"

    # Se houver subopções, mas não foi passado nenhuma
    if suboption is None:
        raise ValueError(f"Suboption is required for option '{option}'")

    # Validação da subopção
    suboptions = config["suboption"]
    if suboption not in suboptions:
        raise ValueError(f"Invalid suboption: '{suboption}' para a opção '{option}'")

    subopt_code = suboptions[suboption]
    return f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao={opt_code}&subopcao={subopt_code}&ano={year}"
