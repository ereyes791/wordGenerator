import random
import string

# Definimos una función que generará una palabra aleatoria de longitud n
def generate_word(n):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

# Creamos un arreglo vacío
word_array = []

# Generamos 5 palabras aleatorias de longitud 10 y las guardamos en el arreglo
for i in range(5):
    word = generate_word(random.randint(2, 7))
    word_array.append(word)

# Imprimimos el arreglo resultante
print(word_array)