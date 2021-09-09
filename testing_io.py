file = open('dados/contatos.csv', encoding='latin_1')

content = file.buffer.read()
print(content)
