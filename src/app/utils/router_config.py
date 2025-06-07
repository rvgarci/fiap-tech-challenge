from typing import Dict, Optional, TypedDict


class RouterOption(TypedDict):
    option: str
    suboption: Optional[Dict[str, str]]
    year: range


ROUTER_CONFIG: Dict[str, RouterOption] = {
    # ------------------------
    # Aba: Produção
    # ------------------------
    "producao": {"option": "opt_02", "suboption": None, "year": range(1970, 2024)},
    # ------------------------
    # Aba: Processamento
    # ------------------------
    "processamento": {
        "option": "opt_03",
        "suboption": {
            "viniferas": "subopt_01",
            "americanas_e_hibridas": "subopt_02",
            "uvas_de_mesa": "subopt_03",
            "sem_classificacao": "subopt_04",
        },
        "year": range(1970, 2024),
    },
    # ------------------------
    # Aba: Comercialização
    # ------------------------
    "comercializacao": {
        "option": "opt_04",
        "suboption": None,
        "year": range(1970, 2024),
    },
    # ------------------------
    # Aba: Importação
    # ------------------------
    "importacao": {
        "option": "opt_05",
        "suboption": {
            "vinhos_de_mesa": "subopt_01",
            "espumantes": "subopt_02",
            "uvas_frescas": "subopt_03",
            "uvas_passas": "subopt_04",
            "sucos_de_uva": "subopt_05",
        },
        "year": range(1970, 2025),
    },
    # ------------------------
    # Aba: Exportação
    # ------------------------
    "exportacao": {
        "option": "opt_06",
        "suboption": {
            "vinhos_de_mesa": "subopt_01",
            "espumantes": "subopt_02",
            "uvas_frescas": "subopt_03",
            "sucos_de_uva": "subopt_04",
        },
        "year": range(1970, 2025),
    },
}
