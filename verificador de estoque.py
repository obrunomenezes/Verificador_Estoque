#sistema de verificação de estoque aqui vai ser exemplo uma loja de games 
#mas poderia ser qualquer coisa
import tkinter as tk

# Função para verificar o estoque e exibir uma mensagem na janela
def verificar_estoque(event=None):  # Adiciona o argumento event
    console_cliente = entrada_console.get().lower()
    console_disponiveis = ['playstation 5', 'xbox', 'nintendo']

    if console_cliente in console_disponiveis:
        mensagem_var.set('Em estoque')
    else:
        mensagem_var.set('Não temos em estoque')

# Criar a janela principal
janela = tk.Tk()
janela.title('Verificação de Estoque')

# Definir as dimensões da janela
janela.geometry("400x200")

# Rótulo e entrada para o console
rotulo_console = tk.Label(janela, text='Qual console você procura?')
rotulo_console.pack()

entrada_console = tk.Entry(janela)
entrada_console.pack()

# Botão para verificar o estoque
botao_verificar = tk.Button(janela, text='Verificar Estoque', command=verificar_estoque)
botao_verificar.pack()

# Variável para exibir a mensagem
mensagem_var = tk.StringVar()
mensagem_var.set('Aguardando verificação...')
mensagem = tk.Label(janela, textvariable=mensagem_var)
mensagem.pack()

# Associar a função verificar_estoque ao evento Enter na entrada
entrada_console.bind("<Return>", verificar_estoque)

# Iniciar o loop da interface gráfica
janela.mainloop()


