import json

# Caminho para o notebook
notebook_path = "MVP_Engenharia_de_Dados.ipynb"

# Carregar o notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Limpar metadados indesejados
for cell in notebook.get("cells", []):
    if "metadata" in cell:
        # Remover metadados específicos do Databricks
        cell["metadata"].pop("application/vnd.databricks.v1+cell", None)
        # Remover outros metadados indesejados (opcional)
        cell["metadata"] = {k: v for k, v in cell["metadata"].items() if not k.startswith("application/")}

# Salvar o notebook limpo
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Metadados limpos com sucesso!")