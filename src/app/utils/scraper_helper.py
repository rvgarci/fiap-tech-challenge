from typing import List, Type
from pydantic import BaseModel


def parse_table(table, model: Type[BaseModel]) -> List[BaseModel]:
    """
    Faz parsing de uma tabela HTML da Embrapa para uma lista de objetos Pydantic.

    Args:
        table: Objeto BeautifulSoup da tabela <table>.
        model: Classe Pydantic com os campos correspondentes à tabela.

    Returns:
        Lista de instâncias validadas do modelo fornecido.
    """
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
            # print("Use Case 1: [Produção, Processamento, Comercialização]")

            if "tb_item" in cell_class:
                current_row[headers[0]] = cells[0].text.strip()

            elif "tb_subitem" in cell_class or len(cells) == len(headers):
                item_data = current_row.copy()
                for i, field in enumerate(headers[1:]):
                    text = cells[i].text.strip() if i < len(cells) else "0"
                    text = text.replace("-", "0").replace(".", "").replace(",", ".")
                    item_data[field] = text
                try:
                    data.append(model(**item_data))
                except Exception as e:
                    print(f"Erro ao criar modelo: {e} | dados: {item_data}")

        # Caso 2: Importação e Exportação (td sem classe)
        elif not cell_class:
            # print("Use Case 2: [Importação, Exportação]")
            item_data = {}
            for i, field in enumerate(headers):
                text = cells[i].text.strip() if i < len(cells) else "0"
                text = text.replace("-", "0").replace(".", "").replace(",", ".")
                item_data[field] = text
            try:
                data.append(model(**item_data))
            except Exception as e:
                print(f"Erro ao criar modelo: {e} | dados: {item_data}")

    return data
