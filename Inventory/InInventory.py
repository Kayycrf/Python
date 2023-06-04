inventory = ['Hatchet',  #A generic inventory
             'Eggs',
             'Estatue',
              'PopCorn']

option = input('Do you want to take this piece of cake?\n').title(). #Asking player if they want to take a piece of cake

inventory.append('Piece of cake') if option == 'Yes' else ''  #condition. If they say yes, the piece of cake will be add to their inventory, else it wont

print('Your inventory:', ', '.join(inventory)) #using join to separate the items with comma and one space after
