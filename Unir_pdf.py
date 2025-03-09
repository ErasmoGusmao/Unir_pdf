#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para unir arquivos PDF de um diretório específico.

Modo de uso:
1. Especificando os arquivos:
   python unir_pdfs.py arquivo_saida.pdf arquivo1.pdf arquivo2.pdf ...

2. Sem argumentos (exceto o nome do script): 
   O script procura pelo diretório "Entrada", mescla todos os PDFs encontrados e gera um arquivo "unido.pdf".
"""

import os
import sys
from PyPDF2 import PdfMerger

def unir_pdfs(arquivos, arquivo_saida):
    merger = PdfMerger()
    for pdf in arquivos:
        print(f"Adicionando {pdf}...")
        merger.append(pdf)
    with open(arquivo_saida, 'wb') as f_out:
        merger.write(f_out)
    merger.close()
    print(f"\nArquivo '{arquivo_saida}' criado com sucesso com {len(arquivos)} arquivos mesclados.")

def main():
    # Se o usuário passar mais de 2 argumentos, o primeiro é o arquivo de saída
    # e os demais são os PDFs a serem mesclados.
    if len(sys.argv) > 2:
        arquivo_saida = sys.argv[1]
        arquivos = sys.argv[2:]
    else:
        # Mescla todos os PDFs que estão no diretório "Entrada"
        diretorio_entrada = "Entrada"
        arquivo_saida = "unido.pdf"
        
        if not os.path.isdir(diretorio_entrada):
            print(f"Diretório '{diretorio_entrada}' não encontrado.")
            sys.exit(1)
        
        arquivos = [
            os.path.join(diretorio_entrada, f)
            for f in os.listdir(diretorio_entrada)
            if f.lower().endswith('.pdf')
        ]
        
        if not arquivos:
            print(f"Nenhum arquivo PDF encontrado no diretório '{diretorio_entrada}'.")
            sys.exit(1)
    
    unir_pdfs(arquivos, arquivo_saida)

if __name__ == "__main__":
    main()
