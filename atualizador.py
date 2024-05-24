nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joana', 'Maria', 'Mariana', 'João','Mariana',
               'Giscard','Michelle','Giscard','Frederico','Márcia','Carla','Clarissa']

indice = int(input('Informe o índice que deseja alterar: '))
indice -= 1

nomes_lista[indice] = input('Informe o novo nome: ')

for nome in nomes_lista:
    print(nome)
    