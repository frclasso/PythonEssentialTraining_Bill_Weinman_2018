#!/usr/bin/env python3


def main():

    # UTILIZANDO A FUNCAO 'dict'PARA CRIAR UM DICIONARIO
    animals = dict(kitten ='meow', puppy='ruff', lion='grrr',
                         giraffe='I am giraffe!', dragon='rawr')

    print()
    # print('Printing Keys!!!')
    # print()
    # for k in other_animals.keys(): print(k)
    # print('-'*30)
    # print('Printing values!!!')
    # print()
    # for v in other_animals.values():print(v)
    # print('-'*30)
    # print('Printing Keys and Values:')
    # print()

    # animals['lion'] = 'I am a Lion!!'  # Alterando o valor
    # animals['monkey'] = 'haha'

    # print('lion' in animals) # Pesquisando chave(key) utilizando operador in
    # print('Found!' if 'lion' in animals else 'Nope!') # criando uma consicao de busca
    # print('Found!' if 'godzilla' in animals else 'Nope!') # Nao encontrou a chave
    # # print(animals['godzilla'])  # KeyError: 'godzilla'
    # print(animals.get('godzilla'))  # None value 'godzilla' nao existe
    # print()
    print_dict(animals)


def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')


if __name__ == "__main__":main()