import nbformat

# Caminho para o notebook
notebook_path = "MVP_Engenharia_de_Dados.ipynb"

# Carregar o notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Limpar saídas de todas as células
for cell in notebook.cells:
    if cell["cell_type"] == "code":
        cell["outputs"] = []
        cell["execution_count"] = None

# Salvar o notebook limpo
with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(notebook, f)

print("Saídas das células limpas com sucesso!")