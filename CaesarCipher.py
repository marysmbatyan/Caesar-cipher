def cesar(direction, language, step, text):
    if language == 'русский':
        alphabet_len = 32
        lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif language == 'английский':
        alphabet_len = 26
        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
    new_text = ''

    for i in range(len(text)):
        if text[i].isalpha() and text[i].isupper():
            place = upper_alphabet.find(text[i])
            if direction == 'шифровать':
                step_nt_pl = place + int(step)
                while step_nt_pl > alphabet_len:
                    step_nt_pl -= alphabet_len
                new_text += upper_alphabet[step_nt_pl]
            elif direction == 'дешифровать':
                step_nt_mi = place - int(step)
                while step_nt_mi < 0:
                    step_nt_mi += alphabet_len
                new_text += upper_alphabet[step_nt_mi]
        elif text[i].isalpha() and text[i].islower():
            place = lower_alphabet.find(text[i])
            if direction == 'шифровать':
                step_nt_pl = place + int(step)
                while step_nt_pl > alphabet_len:
                    step_nt_pl -= alphabet_len
                new_text += lower_alphabet[step_nt_pl]
            elif direction == 'дешифровать':
                step_nt_mi = place - int(step)
                while step_nt_mi < 0:
                    step_nt_mi += alphabet_len
                new_text += lower_alphabet[step_nt_mi]
        else:
            new_text += text[i]
            
    return new_text


whats_direction = input('Что мы должны сделать: шифровать или дешифровать? \n').lower()
while whats_direction != 'шифровать' and whats_direction != 'дешифровать':
    whats_direction = input('Что-то не то ты ввёл. Напиши "шифровать" либо "дешифровать". \n').lower()

whats_language = input('Какой нужен язык: русский или английский? \n').lower()
while whats_language != 'русский' and whats_language != 'английский':
    whats_language = input('Что-то не то ты ввёл. Напиши "русский" либо "английский". \n').lower()

whats_step = input('На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. \n')
while whats_step.isdigit() != True:
    whats_step = input('Что-то не то ты ввёл. Напиши число. \n')
    
whats_text = input('Какой текст нужно использовать сейчас? \n')
while whats_text.isspace() == True:
    whats_text = input('Что-то не то ты ввёл. Введи текст. \n')
    
print(cesar(whats_direction, whats_language, whats_step, whats_text))
