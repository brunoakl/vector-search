import tkinter as tk
import random
from tkinter import messagebox

class VetorDinamico:
    def sort(self):
        """ Ordena o vetor em ordem crescente """
        self.dados[:self.tamanho] = sorted(self.dados[:self.tamanho])

    #Inicializa o vetor
    def __init__(self, capacidade_inicial=1):
        self.capacidade = capacidade_inicial
        self.tamanho = 0
        self.dados = [None] * capacidade_inicial

    
    def append(self, valor, nome=None):
        if self.tamanho == self.capacidade:
            self._redimensionar(2 * self.capacidade)
        self.dados[self.tamanho] = (valor, nome)
        self.tamanho += 1

    #Muda o tamanho do vetor de acordo com a necessidade
    def _redimensionar(self, nova_capacidade):
        nova_lista = [None] * nova_capacidade
        for i in range(self.tamanho):
            nova_lista[i] = self.dados[i]
        self.dados = nova_lista
        self.capacidade = nova_capacidade
    
    def vincular_nome(self, valor, nome):
        for i in range(self.tamanho):
            num, _ = self.dados[i]
            if num == valor:
                self.dados[i] = (valor, nome)
                return
        raise ValueError(f"Valor {valor} não encontrado no vetor.")
    
    def remove(self, valor=None, nome=None):
        if valor is None and nome is None:
            messagebox.showerror("Erro","Forneça um número e/ou nome para remover.")
            return
        
        if valor is None and nome:
            for i in range(self.tamanho):
                num, nome_atual = self.dados[i]
                if nome_atual == nome:
                    self.dados[i] = (num, None)
                    return

        i = 0
        while i < self.tamanho:
            num, nome_atual = self.dados[i]
            if ((valor is not None and num == valor) or
                (nome is not None and nome_atual == nome)):
                for j in range(i, self.tamanho-1):
                    self.dados[j] = self.dados[j+1]
                self.tamanho -= 1
            else:
                i += 1
    
    def clear(self):
        self.tamanho = 0
        self.dados = [None] * self.capacidade

    #Junta nome e número no vetor
    def __str__(self):
        return ', '.join(map(str, self.dados[:self.tamanho]))
    
    #Busca ordenada
    def busca_ordenada(self, valor):
       inicio = 0
       fim = self.tamanho - 1

       while inicio <= fim:
           meio = (inicio + fim) // 2
           num_atual, _ = self.dados[meio]

           if num_atual == valor:
               return meio
           elif num_atual < valor:
               inicio = meio + 1
           else:
               fim = meio - 1
       return None
    
    #Pesquisa pelo elemento máximo
    def max_element(self):
        """ Retorna o maior elemento do vetor e seu nome associado (se houver). """
        if self.tamanho == 0:
            return None, None

        max_num, max_nome = self.dados[0]
        for i in range(1, self.tamanho):
            num, nome = self.dados[i]
            if num > max_num:
                max_num, max_nome = num, nome
        return max_num, max_nome

class App:
    def __init__(self, root):
        self.vetor = VetorDinamico()

        #Organizando campos de texto
        self.inputFrame = tk.Frame(root)
        self.inputFrame.grid(row=0, column=0, sticky="nsew", pady=20, padx=100)
        
        root.grid_rowconfigure(0, weight=1)  # Permite que a linha 0 se estique conforme necessário
        root.grid_columnconfigure(0, weight=1)
        
        #Campos de entrada e seus labels
        self.lblId = tk.Label(self.inputFrame, text="ID:")
        self.lblId.grid(row=0, column=0, sticky=tk.E, padx=(0,5))
        
        self.entryNumber = tk.Entry(self.inputFrame, width=20)
        self.entryNumber.grid(row=0, column=1, sticky=tk.W)

        self.lblName = tk.Label(self.inputFrame, text="Usuário:")
        self.lblName.grid(row=1, column=0, sticky=tk.E, padx=(0,5))
        
        self.entryName = tk.Entry(self.inputFrame, width=20)
        self.entryName.grid(row=1, column=1, sticky=tk.W)
        
        
        #Botões
        #Adiciona ao vetor
        self.btnAdd = tk.Button(root, text="Adicionar Número", command=self.adicionar)
        self.btnAdd.grid(row=1, column=0, pady=5, padx=10, columnspan=2)

        #Vincula o nome ao número indicado do vetor
        self.btnLink = tk.Button(root, text="Vincular Nome", command=self.vincular)
        self.btnLink.grid(row=2, column=0, pady=5, padx=10, columnspan=2)
        
        #Adiciona 5 a 15 números ao vetor, de 1 a 100
        self.btnRandom = tk.Button(root, text="Gerar Vetor Aleatório", command=self.gerar_aleatorio)
        self.btnRandom.grid(row=3, column=0, pady=5, padx=10, columnspan=2)

        #Ordena o vetor a partir dos números, em ordem crescente
        self.btnSort = tk.Button(root, text="Ordenar", command=self.ordenar)
        self.btnSort.grid(row=4, column=0, pady=5, padx=10, columnspan=2)
        
        #Remove dados do vetor
        self.btnRemove = tk.Button(root, text="Remover", command=self.remover)
        self.btnRemove.grid(row=5, column=0, pady=5, padx=10, columnspan=2)

        #Widget que exibe o vetor
        self.output = tk.Text(root, height=10, width=50, font=("Arial", 12))
        self.scrollbar = tk.Scrollbar(root, command=self.output.yview)
        self.output.config(yscrollcommand=self.scrollbar.set)
        self.output.grid(row=6, column=0, pady=20, padx=10, columnspan=2)

        #Botão limpar
        self.btnClear = tk.Button(root, text="Limpar Vetor", command=self.limpar_vetor)
        self.btnClear.grid(row=7, column=0, pady=5, padx=10, columnspan=2)

        #Botão de busca ordenada
        self.btnSearch = tk.Button(root, text="Busca ordenada", command=self.realizar_busca)
        self.btnSearch.grid(row=8, column=0, pady=5, padx=10, columnspan=2)

        # Botão para encontrar o maxElemento
        self.btnMaxElement = tk.Button(root, text="Encontrar Máximo", command=self.find_max)
        self.btnMaxElement.grid(row=9, column=0, pady=5, padx=10, columnspan=2)
    

    #Funções de manipulação do vetor
    #Autoexplicativas
    def adicionar(self):
        try:
            valor = int(self.entryNumber.get())  # Corrigido aqui
            self.vetor.append(valor)
            self.update_display()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")
    
    def remover(self):
        valor = self.entryNumber.get()
        nome = self.entryName.get()
        
        if not valor and not nome:
            messagebox.showerror("Erro","Forneça dados para remoção")
            return
        
        try:
            int_valor = int(valor) if valor else None
            str_nome = nome if nome else None
            self.vetor.remove(int_valor, str_nome)
            self.update_display()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
    
    def gerar_aleatorio(self):
        tamanho = random.randint(5, 15)  # Gera um tamanho aleatório entre 5 e 15
        for _ in range(tamanho):
            self.vetor.append(random.randint(1, 100))  # Adiciona um número aleatório entre 1 e 100
        self.update_display()

    def ordenar(self):
        self.vetor.sort()
        self.update_display()

    def vincular(self):
        try:
            valor = int(self.entryNumber.get())
            nome = self.entryName.get()
            if not nome:
                messagebox.showerror("Erro", "Por favor, insira um nome válido.")
                return
            self.vetor.vincular_nome(valor, nome)
            self.update_display()
        except ValueError:
            messagebox.showerror("Erro", f"Valor {valor} não encontrado no vetor.")

    #Atualiza o widget do vetor com os dados que foram adicionados ou apagados
    def update_display(self):
        self.output.delete(1.0, tk.END)  # Limpar o widget Text
        self.output.insert(tk.END, str(self.vetor))

    #Limpa o vetor
    def limpar_vetor(self):
        self.vetor.clear()
        self.update_display()

    #Requisita uma busca ordenada
    def realizar_busca(self):
        try:
            valor = int(self.entryNumber.get())
            indice = self.vetor.busca_ordenada(valor)
            if indice is not None:
                _, nome = self.vetor.dados[indice]
                if nome:
                    messagebox.showinfo("Resultado da Busca", f"O valor {valor} foi encontrado com o nome associado: {nome}")
                else:
                    messagebox.showinfo("Resultado da Busca", f"O valor {valor} foi encontrado, mas sem nome associado.")
            else:
                messagebox.showerror("Erro", f"O valor {valor} não foi encontrado no vetor.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    #Encontra o valor máximo
    def find_max(self):
        max_num, max_nome = self.vetor.max_element()
        if max_num is None:
            messagebox.showinfo("Resultado", "O vetor está vazio.")
        elif max_nome:
            messagebox.showinfo("Resultado", f"O maior valor é {max_num} com o nome associado: {max_nome}")
        else:
            messagebox.showinfo("Resultado", f"O maior valor é {max_num} mas não tem nome associado.")


    
#Especificações da janela do app
root = tk.Tk()
root.title("Vetor Dinâmico")
root.geometry("500x550")
app = App(root)
root.mainloop()