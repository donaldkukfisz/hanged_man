answer = 'Python'

shots_fired = []
chances = 5

print('Gra w odgadywanie hasła.')
while True:
    
    print()
    shot = input('Wpisz literę: ')
    shots_fired.append(shot)
    
    if shot not in answer:
        chances -= 1
    print()
    print('Twoje postępy:')
    for _ in answer:
        if _.lower() in shots_fired:
            print(f'{_} ', end= '')
        else:
            print('_ ', end = '')
    
    print()
    print(f'Pozostałe szanse: {chances}')
    
    if chances == 0:
        print('Przegrałes!')
        break
            
