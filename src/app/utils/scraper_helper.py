from typing import List, Optional, Type

from pydantic import BaseModel

SUBOPTION_LABELS = {
    "vinhos_de_mesa": "Vinhos de mesa",
    "espumantes": "Espumantes",
    "uvas_frescas": "Uvas frescas",
    "uvas_passas": "Uvas passas",
    "sucos_de_uva": "Suco de uva",
    "viniferas": "Viníferas",
    "americanas_e_hibridas": "Americanas e híbridas",
    "uvas_de_mesa": "Uvas de mesa",
    "sem_classificacao": "Sem classificação",
}


def sanitize_numeric(text: str) -> str:
    text = (
        text.strip()
        .replace("-", "0")
        .replace("*", "0")
        .replace(".", "")
        .replace(",", ".")
    )
    return text if text.replace(".", "").isdigit() else "0"


def parse_table_by_model(
    table,
    model: Type[BaseModel],
    ano: Optional[int] = None,
    suboption: Optional[str] = None,
) -> List[BaseModel]:
    data = []
    model_name = model.__name__
    current_row = {}

    tfoot = table.find("tfoot")
    if tfoot:
        tfoot.decompose()

    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if not cells:
            continue

        cell_class = cells[0].get("class", [])

        # Produção / Comercialização / Processamento
        if "tb_item" in cell_class or "tb_subitem" in cell_class:
            if "tb_item" in cell_class:
                text = cells[0].text.strip()
                current_row.clear()

                if model_name in ["ProductionItem", "CommercialItem"]:
                    current_row["type"] = text
                    # Define categoria baseado no conteúdo de "type"
                    if "vinho" in text.lower():
                        current_row["category"] = "Vinho"
                    elif "suco" in text.lower():
                        current_row["category"] = "Suco"
                    else:
                        current_row["category"] = "Derivado"

                elif model_name == "ProcessingItem":
                    current_row["color"] = text
                    current_row["type"] = SUBOPTION_LABELS.get(suboption, suboption)

            elif "tb_subitem" in cell_class:
                item_data = current_row.copy()

                if model_name in ["ProductionItem", "CommercialItem"]:
                    item_data["product"] = cells[0].text.strip()
                    item_data["quantity"] = float(sanitize_numeric(cells[1].text))
                    item_data["unit_of_measure"] = "L"

                elif model_name == "ProcessingItem":
                    item_data["cultivar"] = cells[0].text.strip()
                    item_data["quantity"] = float(sanitize_numeric(cells[1].text))
                    item_data["unit_of_measure"] = "kg"

                if "year" in model.model_fields and ano is not None:
                    item_data["year"] = ano

                try:
                    data.append(model(**item_data))
                except Exception as e:
                    print(f"Erro ao criar {model_name}: {e} | dados: {item_data}")

        # Importação / Exportação
        elif not cell_class:
            item_data = {}

            if model_name in ["ImportItem", "ExportItem"]:
                item_data["type"] = SUBOPTION_LABELS.get(suboption, suboption)
                item_data["country"] = cells[0].text.strip()
                item_data["quantity"] = float(sanitize_numeric(cells[1].text))
                item_data["unit_of_measure"] = "kg"
                item_data["value"] = float(sanitize_numeric(cells[2].text))
                item_data["currency"] = "USD"

                if "year" in model.model_fields and ano is not None:
                    item_data["year"] = ano

                try:
                    data.append(model(**item_data))
                except Exception as e:
                    print(f"Erro ao criar {model_name}: {e} | dados: {item_data}")

    return data
