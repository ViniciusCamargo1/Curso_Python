import tkinter as tk

def enviar_dados():
    """Captura os dados inseridos nos campos e os imprime no console."""
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    celular = entry_celular.get()
    cep = entry_cep.get()
    cidade = entry_cidade.get()
    cursos = entry_cursos.get()

    print("\n" + "="*30)
    print(" NOVO CLIENTE CADASTRADO")
    print("="*30)
    print(f"Nome:     {nome}")
    print(f"Idade:    {idade}")
    print(f"E-mail:   {email}")
    print(f"Endereço: {endereco}")
    print(f"Celular:  {celular}")
    print(f"CEP:      {cep}")
    print(f"Cidade:   {cidade}")
    print(f"Cursos:   {cursos}")
    print("="*30 + "\n")

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_cep.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_cursos.delete(0, tk.END)

janela = tk.Tk()
janela.title("Sistema de Cadastro de Clientes")

janela.geometry("1700x750") 

janela.configure(padx=50, pady=50) 

tk.Label(janela, text="Preencha os dados do cliente:", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="w")

fonte_padrao = ("Arial", 12)


tk.Label(janela, text="Nome:", font=fonte_padrao).grid(row=1, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(janela, width=50, font=fonte_padrao)
entry_nome.grid(row=1, column=1, pady=5, padx=10)

tk.Label(janela, text="Idade:", font=fonte_padrao).grid(row=2, column=0, sticky="w", pady=5)
entry_idade = tk.Entry(janela, width=50, font=fonte_padrao)
entry_idade.grid(row=2, column=1, pady=5, padx=10)

tk.Label(janela, text="E-mail:", font=fonte_padrao).grid(row=3, column=0, sticky="w", pady=5)
entry_email = tk.Entry(janela, width=50, font=fonte_padrao)
entry_email.grid(row=3, column=1, pady=5, padx=10)

tk.Label(janela, text="Endereço:", font=fonte_padrao).grid(row=4, column=0, sticky="w", pady=5)
entry_endereco = tk.Entry(janela, width=50, font=fonte_padrao)
entry_endereco.grid(row=4, column=1, pady=5, padx=10)

tk.Label(janela, text="Celular:", font=fonte_padrao).grid(row=5, column=0, sticky="w", pady=5)
entry_celular = tk.Entry(janela, width=50, font=fonte_padrao)
entry_celular.grid(row=5, column=1, pady=5, padx=10)

tk.Label(janela, text="Cep:", font=fonte_padrao).grid(row=6, column=0, sticky="w", pady=5)
entry_cep = tk.Entry(janela, width=50, font=fonte_padrao)
entry_cep.grid(row=6, column=1, pady=5, padx=10)

tk.Label(janela, text="Cidade:", font=fonte_padrao).grid(row=7, column=0, sticky="w", pady=5)
entry_cidade = tk.Entry(janela, width=50, font=fonte_padrao)
entry_cidade.grid(row=7, column=1, pady=5, padx=10)

tk.Label(janela, text="Cursos:", font=fonte_padrao).grid(row=8, column=0, sticky="w", pady=5)
entry_cursos = tk.Entry(janela, width=50, font=fonte_padrao)
entry_cursos.grid(row=8, column=1, pady=5, padx=10)

btn_enviar = tk.Button(janela, text="Enviar", command=enviar_dados, font=("Arial", 12, "bold"), bg="#0078D7", fg="white", width=20)
btn_enviar.grid(row=9, column=0, columnspan=2, pady=30)

janela.mainloop()