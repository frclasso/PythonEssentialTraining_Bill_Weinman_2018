#!/usr/bin/env python3

animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    if pet == 'dog': continue  #NAO EXIBE 'dog'
    #if pet == 'velociraptor': break   # Descomente essa linha
    print(pet)
else:
    print("That's  all the animals")