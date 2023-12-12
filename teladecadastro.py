import tkinter as tk
from tkinter import ttk, messagebox


album_lista = []

def cadastrar_album():
    nome_album = entry_nome_album.get()
    ano_lancamento = entry_ano_lancamento.get()
    nome_banda_artista = entry_nome_banda_artista.get()
    lancamento_artista = var_lancamento_artista.get()

    if nome_album and ano_lancamento and nome_banda_artista:
        album = {
            "Nome do Álbum": nome_album,
            "Ano de Lançamento": ano_lancamento,
            "Nome da Banda/Artista": nome_banda_artista,
            "Álbum Lançamento do Artista": "Sim" if lancamento_artista == 1 else "Não"
        }
        album_lista.append(album)

        entry_nome_album.delete(0, tk.END)
        entry_ano_lancamento.delete(0, tk.END)
        entry_nome_banda_artista.delete(0, tk.END)
        var_lancamento_artista.set(0)

        messagebox.showinfo("Cadastro", "Álbum cadastrado com sucesso!")

        salvar_no_arquivo(album)
    else:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")

def salvar_no_arquivo(album):
    with open("base_de_dados.txt", "a", encoding='utf-8') as file:
        file.write(f"Nome do Álbum: {album['Nome do Álbum']}\n")
        file.write(f"Ano de Lançamento: {album['Ano de Lançamento']}\n")
        file.write(f"Nome da Banda/Artista: {album['Nome da Banda/Artista']}\n")
        file.write(f"Álbum Lançamento do Artista: {album['Álbum Lançamento do Artista']}\n")
        file.write("\n")

def listar_albums():
    listagem = "\n".join([f"{album['Nome do Álbum']} ({album['Ano de Lançamento']}), {album['Nome da Banda/Artista']}, Lançamento do Artista: {album['Álbum Lançamento do Artista']}" for album in album_lista])

    if listagem:
        messagebox.showinfo("Álbuns Cadastrados", listagem)
    else:
        messagebox.showinfo("Álbuns Cadastrados", "Nenhum álbum cadastrado ainda.")

def buscar_por_artista():
    nome_artista = entry_busca_artista.get().lower()
    resultados = []

    for album in album_lista:
        if nome_artista in album["Nome da Banda/Artista"].lower():
            resultados.append(album)

    mostrar_resultados(resultados)

def buscar_por_ano():
    tipo_busca = var_tipo_busca.get()
    ano_selecionado = combo_anos.get()

    resultados = []

    for album in album_lista:
        ano_album = int(album["Ano de Lançamento"])
        if tipo_busca == "Anterior a" and ano_album <= int(ano_selecionado):
            resultados.append(album)
        elif tipo_busca == "Posterior a" and ano_album >= int(ano_selecionado):
            resultados.append(album)
        elif tipo_busca == "Igual a" and ano_album == int(ano_selecionado):
            resultados.append(album)

    mostrar_resultados(resultados)

def mostrar_resultados(resultados):
    if resultados:
        listagem = "\n".join([f"{album['Nome do Álbum']} ({album['Ano de Lançamento']}), {album['Nome da Banda/Artista']}, Lançamento do Artista: {album['Álbum Lançamento do Artista']}" for album in resultados])
        messagebox.showinfo("Resultados da Busca", listagem)
    else:
        messagebox.showinfo("Resultados da Busca", "Nenhum álbum encontrado.")

root = tk.Tk()
root.title("Cadastro e Busca de Álbuns")

root.geometry("500x500")

label_nome_album = tk.Label(root, text="Nome do Álbum:")
entry_nome_album = tk.Entry(root)

label_ano_lancamento = tk.Label(root, text="Ano de Lançamento:")
entry_ano_lancamento = tk.Entry(root)

label_nome_banda_artista = tk.Label(root, text="Nome da Banda/Artista:")
entry_nome_banda_artista = tk.Entry(root)

label_lancamento_artista = tk.Label(root, text="Álbum Lançamento do Artista:")
var_lancamento_artista = tk.IntVar()
radio_sim = tk.Radiobutton(root, text="Sim", variable=var_lancamento_artista, value=1)
radio_nao = tk.Radiobutton(root, text="Não", variable=var_lancamento_artista, value=0)

btn_cadastrar = tk.Button(root, text="Cadastrar Álbum", command=cadastrar_album)
btn_listar = tk.Button(root, text="Listar Álbuns Cadastrados", command=listar_albums)

label_busca_artista = tk.Label(root, text="Buscar por Nome do Artista:")
entry_busca_artista = tk.Entry(root)
btn_buscar_artista = tk.Button(root, text="Buscar", command=buscar_por_artista)

label_busca_ano = tk.Label(root, text="Buscar por Ano do Álbum:")
var_tipo_busca = tk.StringVar()
tipo_busca_options = ["Anterior a", "Posterior a", "Igual a"]
combo_tipo_busca = ttk.Combobox(root, textvariable=var_tipo_busca, values=tipo_busca_options)
combo_tipo_busca.set(tipo_busca_options[0])

label_ano = tk.Label(root, text="Ano:")
anos_disponiveis = [str(ano) for ano in range(1900, 2101)]
combo_anos = ttk.Combobox(root, values=anos_disponiveis)

btn_buscar_ano = tk.Button(root, text="Buscar", command=buscar_por_ano)

label_nome_album.pack(pady=5)
entry_nome_album.pack(pady=5)

label_ano_lancamento.pack(pady=5)
entry_ano_lancamento.pack(pady=5)

label_nome_banda_artista.pack(pady=5)
entry_nome_banda_artista.pack(pady=5)

label_lancamento_artista.pack(pady=5)
radio_sim.pack()
radio_nao.pack()

btn_cadastrar.pack(pady=10)
btn_listar.pack(pady=10)

label_busca_artista.pack(pady=5)
entry_busca_artista.pack(pady=5)
btn_buscar_artista.pack(pady=5)

label_busca_ano.pack(pady=5)
combo_tipo_busca.pack(pady=5)
label_ano.pack(pady=5)
combo_anos.pack(pady=5)
btn_buscar_ano.pack(pady=5)

root.mainloop()
