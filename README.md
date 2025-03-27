# MVP_Engenharia_de_Dados


### Descrição do Projeto

Este repositório contém os arquivos relacionados ao projeto MVP Engenharia de Dados , que analisa postagens da plataforma Bluesky para identificar e classificar temas discutidos pelos usuários. O projeto inclui versões do notebook no formato original (Databricks), LaTeX (.tex), e PDF (.pdf), além de scripts para limpeza de metadados e saídas.

Estrutura do Repositório:

- MVP_Engenharia_de_Dados.ipynb : Versão original do notebook no formato Databricks. Este é o arquivo principal usado para execução no ambiente Databricks.
- MVP_Engenharia_de_Dados.tex : Versão em LaTeX do trabalho, gerada a partir do notebook. Pode ser editada manualmente para ajustes de formatação.
- MVP_Engenharia_de_Dados.pdf : Versão final do trabalho em formato PDF, pronta para visualização ou impressão.
- limpar_metadados.py : Script Python para limpar os metadados do notebook. Remove informações desnecessárias, como IDs de execução e configurações específicas do Databricks.
- limpar_saidas.py : Script Python para limpar as saídas das células de código do notebook. Remove resultados de execução (ex.: tabelas, gráficos, logs) para facilitar a revisão e exportação do código-fonte.
     

### Como Usar os Scripts

1. Limpeza de Metadados (limpar_metadados.py)

O script limpar_metadados.py remove metadados desnecessários do notebook, como IDs de execução e configurações específicas do Databricks. Para usá-lo:

```
python limpar_metadados.py
```

Resultado:  O arquivo MVP_Engenharia_de_Dados.ipynb será atualizado com os metadados removidos.

2. Limpeza de Saídas (limpar_saidas.py)

O script limpar_saidas.py remove as saídas das células de código do notebook, deixando apenas o código-fonte. Isso é útil para exportar o notebook para LaTeX ou PDF sem saídas estáticas. Para usá-lo: 
 
```
python limpar_saidas.py
```

Resultado:  O arquivo MVP_Engenharia_de_Dados.ipynb será atualizado com as saídas das células removidas. 
Fluxo de Trabalho Recomendado 

1. Desenvolvimento no Databricks:

- Use o notebook MVP_Engenharia_de_Dados.ipynb no Databricks para desenvolver e executar o código.
- Salve o notebook após concluir suas alterações.
         

2. Limpeza de Metadados e Saídas:

- Execute os scripts limpar_metadados.py e limpar_saidas.py para preparar o notebook para exportação.
- Certifique-se de que o notebook esteja limpo antes de exportar para LaTeX ou PDF.
         

3. Exportação para LaTeX e PDF:

- Use uma ferramenta como o Quarto para exportar o notebook limpo para LaTeX.

```
quarto render MVP_Engenharia_de_Dados.ipynb --to latex
```

- Abra o arquivo MVP_Engenharia_de_Dados.tex em um editor de texto ou LaTeX.

- Ajuste problemas como:

	- Quebras de linha em blocos de código ou texto longo.
	
	- Formatação de caracteres especiais (ex.: subtraços _, cifrões $, etc.).
	
	- Alinhamento de tabelas ou figuras.

- Adicione pacotes LaTeX ou ajustes no preâmbulo, se necessário, para melhorar a formatação.

- Compile o arquivo .tex para gerar o PDF final:

```
xelatex MVP_Engenharia_de_Dados.tex
```               

4. Versão Final:
- Inclua as versões .tex e .pdf no repositório para referência.
         

### Observações Importantes

- Compatibilidade com Databricks:  Os scripts limpar_metadados.py e limpar_saidas.py não comprometem a compatibilidade funcional do notebook com o Databricks. No entanto, ao remover saídas, será necessário reexecutar o notebook para gerar os resultados novamente.
- Backup:  Antes de executar os scripts, faça um backup do notebook original caso precise recuperar as saídas ou metadados posteriormente.
