import sys
import string
import random
from words_to_guess import english_words, polish_words


word = random.choice(english_words)

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

print('Gra w odgadywanie słów. Wybierz w jakim języku chcesz odgadywać słowo:')
while True:
    
    language = input('1. Polski, 2. Angielski: ')
    if language not in ('1', '2'):
        print('Błąd, wybierz poprawny język:')
        continue
    if language == 1:
        word = random.choice(polish_words)
    elif language == 2:
        word = random.choice(english_words)

    while True:
        
        print()
        letter = input('Wpisz literę: ')
        
        if letter not in (string.ascii_letters):
            print('To nie jest pojedyncza litera, spróbuj jeszcze raz!')
            continue
        elif letter in allready_used_letters:
            print('Litera już wykorzystana, spróbuj ponownie!')
            continue
        
        allready_used_letters.append(letter)
        
        indexes = find_index(word, letter)
        
        
        if len(find_index(word, letter)) == 0:
            print('Nie ma takiej litery!')
            chances -= 1
            print(f'Pozostałe szanse: {chances}')
            
            if chances == 0:
                print('Koniec gry, przegrałes! Hasło brzmiało: ', word)
                sys.exit(0)
                
        else:
            
            for index in indexes:
                user_answers[index] = letter
            
            if ''.join(user_answers) == word:
                print('Gratulacje, odgadłes słowo! Odpowiedź brzmi: ', word)
                sys.exit(0)
        
        print(user_answers)
    
    
 