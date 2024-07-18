#  As cores em Python podem ser representadas de diversas maneiras, dependendo do que é preciso.

# Usando String
print('Cores em Strings')
cor_azul = "#0000FF"
print(cor_azul)

# Usando Tuplas para representar cores RGB, você pode usar tuplas com três valores inteiros, cada um variando de 0 a 255
print('Cores em Tuplas')
cor_red = (255, 0, 0)
print(cor_red)

# Usando Libs para manipulação avançada, lib ex(PIL (Pillow) ou matplotlib)
# ---> A biblioteca Pillow permite trabalhar com imagens e cores de forma fácil

from PIL import Image, ImageColor
print('Cores lib externa Pillow')
azul_rgb = ImageColor.getrgb('#0000FF')
print(azul_rgb)

# ---> A biblioteca matplotlib oferece muitas funcionalidades para trabalhar com cores, especialmente criando gráficos
import matplotlib.pyplot as plt
print('Cores lib externa matplotlib')
# Exemplo de gráfico com cores personalizadas
plt.plot([1, 2, 3], [4, 5, 6], color='#FF0000')  # Cor vermelha em hexadecimal
plt.show()

# Conversão de cores
print('Conversão de cores')
def hex_para_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

cor_azul_rgb = hex_para_rgb("#0000FF")
print(cor_azul_rgb)  # Saída: (0, 0, 255)

# Usando cores em Interface Gráficas
import tkinter as tk
print('Conversão de cores')
root = tk.Tk()
root.configure(bg='#FF0000')  # Configurando o fundo da janela para vermelho
root.mainloop()

