from typing import List, Dict

def parse_table(table) -> List[Dict[str, str]]:

    data = []
    tipo = ""

    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if not cells:
            continue

        cell_class = cells[0].get("class", [])

        if "tb_item" in cell_class:
            tipo = cells[0].text.strip()
        elif "tb_subitem" in cell_class:
            produto = cells[0].text.strip()
            quantidade = cells[1].text.strip().replace("-", "0").replace(".", "").replace(",", ".")
            data.append({"tipo": tipo, "produto": produto, "quantidade": quantidade})
    
    return data
