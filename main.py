import pandas as pd
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess  # Para abrir o arquivo em diferentes sistemas operacionais

def listar_arquivos_pasta(pasta):
    arquivos = []
    for root, dirs, files in os.walk(pasta):
        for file in files:
            arquivos.append(os.path.join(root, file))
    return arquivos

def exportar_para_excel(arquivos, caminho_completo):
    if not arquivos:
        messagebox.showwarning("Aviso", "Nenhum arquivo encontrado para exportar!")
        return

    df = pd.DataFrame(arquivos, columns=['Arquivo'])
    df.to_excel(caminho_completo, index=False)
    messagebox.showinfo("Sucesso", f"Arquivo Excel criado com sucesso em:\n{caminho_completo}")

    # Pergunta se o usuário deseja abrir o arquivo
    abrir = messagebox.askyesno("Abrir Arquivo?", "Deseja abrir o arquivo Excel agora?")
    if abrir:
        try:
            if os.name == 'nt':  # Windows
                os.startfile(caminho_completo)
            elif os.name == 'posix':  # macOS ou Linux
                comando = 'open' if sys.platform == 'darwin' else 'xdg-open'
                subprocess.call([comando, caminho_completo])
        except Exception as e:
            messagebox.showwarning("Aviso", f"Arquivo criado, mas não foi possível abri-lo automaticamente.\nErro: {e}")

def selecionar_pasta(titulo):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title=titulo)

def selecionar_arquivo_saida(titulo):
    root = tk.Tk()
    root.withdraw()
    return filedialog.asksaveasfilename(title=titulo, defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])

def executar_levantamento():
    pasta = selecionar_pasta("Selecione a pasta de origem")
    if not pasta:
        messagebox.showerror("Erro", "Seleção de pasta de origem cancelada.")
        return

    caminho_completo = selecionar_arquivo_saida("Escolha o nome e o local do arquivo de saída")
    if not caminho_completo:
        messagebox.showerror("Erro", "Seleção do arquivo de saída cancelada.")
        return

    arquivos = listar_arquivos_pasta(pasta)
    exportar_para_excel(arquivos, caminho_completo)

def main():
    executar_levantamento()

if __name__ == "__main__":
    main()
