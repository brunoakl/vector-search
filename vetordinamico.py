import tkinter as tk
import random
from tkinter import messagebox

class VetorDinamico:
    def sort(self):
        """ Ordena o vetor em ordem crescente """
        self.dados[:self.tamanho] = sorted(self.dados[:self.tamanho])

    def __init__(self, capacidade_inicial=1):
        self.capacidade = capacidade_inicial
        self.tamanho = 0
        self.dados = [None] * capacidade_inicial

    def append(self, valor, nome=None):
        if self.tamanho == self.capacidade:
            self._redimensionar(2 * self.capacidade)
        self.dados[self.tamanho] = (valor, nome)
        self.tamanho += 1

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

    def __str__(self):
        return ', '.join(f"{num}({nome})" if nome else str(num) for num, nome in self.dados[:self.tamanho])
    
    def remove(self, valor):
        indice = -1
        for i in range(self.tamanho):
            if self.dados[i] == valor:
                indice = i
                break
        if indice == -1:
            raise ValueError(f"Valor {valor} não encontrado no vetor.")
        
        for i in range(indice, self.tamanho-1):
            self.dados[i] = self.dados[i+1]
        self.tamanho -= 1

    def __str__(self):
        return ', '.join(map(str, self.dados[:self.tamanho]))

class App:
    def __init__(self, root):
        self.vetor = VetorDinamico()

        self.lblId = tk.Label(root, text="ID:")
        self.lblId.pack(pady=10, side=tk.LEFT)
        self.entryNumber = tk.Entry(root)
        self.entryNumber.pack(pady=10)

        self.lblName = tk.Label(root, text="Usuário:")
        self.lblName.pack(pady=10, side=tk.LEFT)
        self.entryName = tk.Entry(root)
        self.entryName.pack(pady=10)

        self.btnAdd = tk.Button(root, text="Adicionar Número", command=self.adicionar)
        self.btnAdd.pack()

        self.btnLink = tk.Button(root, text="Vincular Nome", command=self.vincular)
        self.btnLink.pack()

       

        self.btnRandom = tk.Button(root, text="Gerar Vetor Aleatório", command=self.gerar_aleatorio)
        self.btnRandom.pack(pady=10)

        self.btnSort = tk.Button(root, text="Ordenar", command=self.ordenar)
        self.btnSort.pack(pady=10)

        self.output = tk.Label(root, text="", font=("Arial", 12))
        self.output.pack(pady=20)

    def adicionar(self):
        try:
            valor = int(self.entryNumber.get())  # Corrigido aqui
            self.vetor.append(valor)
            self.update_display()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    

    
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


    def update_display(self):
        self.output['text'] = str(self.vetor)

    

root = tk.Tk()
root.title("Vetor Dinâmico")
app = App(root)
root.mainloop()
