import sys

word = 'python'

allready_used_letters = []
user_answers = []
chances = 5

for letter in word:
    user_answers.append('_')

def find_index(word, letter):
    
    indexes = []
    
    for index, letter_in_answer in enumerate(word):
        if letter == letter_in_answer:
            indexes.append(index)
    return indexes



print('Gra w odgadywanie hasła.')
while True:
    
    print()
    letter = input('Wpisz literę: ')
    
    if letter in allready_used_letters:
        print('Litera już wykorzystana, spróbuj ponownie!')
        continue
    
    allready_used_letters.append(letter)
    
    indexes = find_index(word, letter)
    
    
    if len(find_index(word, letter)) == 0:
        print('Nie ma takiej litery!')
        chances -= 1
        print(f'Pozostałe szanse: {chances}')
        
        if chances == 0:
            print('Koniec gry, przegrałes!')
            sys.exit(0)
            
    else:
        
        for index in indexes:
            user_answers[index] = letter
        
        if ''.join(user_answers) == word:
            print('Gratulacje, odgadłes słowo!')
            sys.exit(0)
    
    print(user_answers)
            