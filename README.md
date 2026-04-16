# 🇺🇸 Converter_Numbers_To_CSV

A simple script to convert .numbers files into .csv format.

📌 Description

This script scans a folder for .numbers files and converts them into .csv files, keeping the original files unchanged.

⚙️ Requirements
Python 3.x installed
Can be executed via IDLE or terminal

▶️ Usage
Place the script in the same folder as your .numbers files.
Run the script:
Using IDLE, or

From the terminal:

```python script_name.py```
After execution, .csv files will be created in the same directory.

Original .numbers files are preserved.

📦 (Optional) Merge all CSV files

After conversion, you can merge all .csv files into a single file.

On CMD:
```copy /b *.csv all_leads.csv```
On PowerShell:
```Get-Content *.csv | Set-Content all_leads.csv```

⚠️ Notes
Make sure the .numbers files are valid.
Conversion results may vary depending on file structure.
Merging CSV files does not remove duplicate headers automatically.


# 🇧🇷 Converter_Numbers_To_CSV

Script simples para converter arquivos .numbers em .csv.

📌 Descrição

Este script percorre todos os arquivos .numbers em uma pasta e os converte para o formato .csv, mantendo os arquivos originais intactos.

⚙️ Requisitos
Python instalado (3.x)
Executar via IDLE ou terminal

▶️ Como usar
Coloque o script na mesma pasta onde estão os arquivos .numbers.
Execute o script:
Pelo IDLE (abrindo e rodando o arquivo), ou

Pelo terminal:

```python nome_do_script.py```
Após a execução, os arquivos .csv serão gerados na mesma pasta.

Os arquivos .numbers originais não são alterados.

📦 (Opcional) Unir todos os arquivos CSV

Após a conversão, você pode juntar todos os arquivos .csv em um único arquivo.

No CMD:
```copy /b *.csv todos_leads.csv```
No PowerShell:
```Get-Content *.csv | Set-Content todos_leads.csv```

⚠️ Observações
Certifique-se de que os arquivos .numbers estejam válidos.
Dependendo da estrutura do arquivo, a conversão pode variar.
A junção dos CSVs não remove cabeçalhos duplicados automaticamente.
