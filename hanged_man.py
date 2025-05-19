import sys
import string
import random
from words_to_guess import english_words, polish_words

chances = 0

def find_index(word, letter):
    
    indexes = []
    
    for index, letter_in_answer in enumerate(word):
        if letter == letter_in_answer:
            indexes.append(index)
    return indexes

def choose_difficulty():
    
        
    level = input('Wybierz poziom trudnosci: 1. ŁATWY, 2.ŚREDNI, 3.TRUDNY: ')
    
    if level == '1':
        chances = 10
        msg = f'Wybrano poziom ŁATWY. Masz {chances} prób odgadnięcia!'
    elif level == '2':
        chances = 5
        msg = f'Wybrano poziom ŚREDNI. Masz {chances} prób odgadnięcia!'
    elif level == '3':
        chances = 3
        msg = f'Wybrano poziom TRUDNY. Masz {chances} prób odgadnięcia!'
        
    return chances, msg
    

print('Gra w odgadywanie słów!')


while True:
    
    chances = 0
    chances, msg = choose_difficulty()
    print(msg)
    
    language = input('Wybierz język w jakim chcesz odgadnąc słowo: 1. Polski, 2. Angielski: ')

    if language not in ('1', '2'):
        print('Błąd, wybierz poprawny język:')
        continue
    if language == '1':
        word = random.choice(polish_words)
    elif language == '2':
        word = random.choice(english_words)
    
    allready_used_letters = []
    user_answers = []
    
    for letter in word:
        user_answers.append('_')
    
    print('Słowo zostało wylosowane!')
    
    while True:
        
        print()
        letter = input('Odgadnij literę i zatwierdz ENTEREM: ')
        
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
                print(f'Koniec gry, przegrałes! Hasło brzmiało: {word.upper()}')
                print()
                end = input('Czy chcesz zagrać jeszcze raz? T/N: ')
                if end.lower() == 't':
                    break
                
                else:
                    print('Koniec gry, do zobaczenia!')
                    sys.exit(0)
        else:
            
            for index in indexes:
                user_answers[index] = letter
            
            if ''.join(user_answers) == word:
                print(f'GRATULACJE! Odgadłes słowo! Odpowiedź brzmi: {word.upper()}')
                sys.exit(0)
        
        print(user_answers)
    
    
 