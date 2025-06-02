from typing import Dict, Optional, Union

ROUTER_CONFIG: Dict[
    str,
    Dict[str, Union[str, Optional[Dict[str, str]], range]]
] = {
    "producao": {
        "option": "opt_02",
        "suboption": None,
        "year": range(1970, 2024)
    },
    "processamento": {
        "option": "opt_03",
        "suboption": {
            "viniferas": "subopt_01",
            "americanas_e_hibridas": "subopt_02",
            "uvas_de_mesa": "subopt_03",
            "sem_classificacao": "subopt_04",
        },
        "year": range(1970, 2024)
    },
    "comercializacao": {
        "option": "opt_04",
        "suboption": None,
        "year": range(1970, 2024)
    },
    "importacao": {
        "option": "opt_05",
        "suboption": {
            "vinhos_de_mesa": "subopt_01",
            "espumantes": "subopt_02",
            "uvas_frescas": "subopt_03",
            "uvas_passas": "subopt_04",
            "sucos_de_uva": "subopt_05",
        },
        "year": range(1970, 2025)
    },
    "exportacao": {
        "option": "opt_06",
        "suboption": {
            "vinhos_de_mesa": "subopt_01",
            "espumantes": "subopt_02",
            "uvas_frescas": "subopt_03",
            "sucos_de_uva": "subopt_04",
        },
        "year": range(1970, 2025)
    }
}
