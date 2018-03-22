#!/usr/bin/env python3


def main():
    game = ['Rock', 'Paper','Scissors','Lizard', 'Spock']  # list
    # game = ('Rock', 'Paper','Scissors','Lizard', 'Spock')  # tuple


    #print(game[1])  # Paper
    #print_list(game[1:3])  # Paper, Scissors
    #print_list(game[1:5:2])  # Paper ,Lizard

    game.append('Computer')  # Add Computer a lista

    game.insert(0, 'Hotel')  # Insere Hotel no inicio da lista

    # game.remove('Paper')  # Remove Paper da lista

    # game.pop() # Remove o ultimo elemento da lista

    # x = game.pop()
    # print(x)

    # game.pop(3)  # Remove Lizard

    # del game[3]   # Remove Lizard
    # del game[1:3]   # Remove Rock e Paper
    # del game[1:5:2]   # Remove Rock,Paper e Lizard

    print(len(game))
    print(', '.join(game))
    print(print_list(game))


def print_list(o):
    print('-'*50)
    for i in o: print(i, end=" ", flush=True)
    print()


if __name__ == "__main__": main()