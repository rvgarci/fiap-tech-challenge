from typing import List, Type
from pydantic import BaseModel


def sanitize_numeric(text: str) -> str:
    """
    Limpa e normaliza valores numéricos para conversão segura.
    Substitui símbolos como '*' ou strings vazias por '0'.
    """
    text = text.strip().replace("-", "0").replace("*", "0").replace(".", "").replace(",", ".")
    return text if text.replace(".", "").isdigit() else "0"


def parse_table(table, model, ano=None) -> List[BaseModel]:
    data = []
    headers = list(model.model_fields)
    current_row = {}

    # Remove rodapé (tfoot) da tabela
    tfoot = table.find("tfoot")
    if tfoot:
        tfoot.decompose()

    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if not cells:
            continue

        cell_class = cells[0].get("class", [])

        # Caso 1: Produção, Processamento e Comercialização
        if "tb_item" in cell_class or "tb_subitem" in cell_class:
            if "tb_item" in cell_class:
                current_row[headers[0]] = cells[0].text.strip()

            elif "tb_subitem" in cell_class or len(cells) == len(headers):
                item_data = current_row.copy()
                for i, field in enumerate(headers[1:]):
                    raw = cells[i].text.strip() if i < len(cells) else "0"
                    item_data[field] = sanitize_numeric(raw)

                if "ano" in model.model_fields and ano is not None:
                    item_data["ano"] = ano

                try:
                    data.append(model(**item_data))
                except Exception as e:
                    print(f"Erro ao criar modelo: {e} | dados: {item_data}")

        # Caso 2: Importação e Exportação
        elif not cell_class:
            item_data = {}
            for i, field in enumerate(headers):
                raw = cells[i].text.strip() if i < len(cells) else "0"
                item_data[field] = sanitize_numeric(raw)

            if "ano" in model.model_fields and ano is not None:
                item_data["ano"] = ano

            try:
                data.append(model(**item_data))
            except Exception as e:
                print(f"Erro ao criar modelo: {e} | dados: {item_data}")

    return data
