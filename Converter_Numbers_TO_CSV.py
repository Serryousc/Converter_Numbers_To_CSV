import glob
import csv
from numbers_parser import Document

for arquivo in glob.glob("*.numbers"):

    doc = Document(arquivo)

    for sheet in doc.sheets:
        for table in sheet.tables:
 
            nome_saida = arquivo.replace(".numbers", ".csv")

            with open(nome_saida, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=';')

                for row in table.rows():

                    linha = []
                    for cell in row:
                        if cell is None:
                            linha.append("")
                        else:
                            linha.append(cell.value)

                    writer.writerow(linha)
 
