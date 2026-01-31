print('Enter a string:')

text = input()
print(f'You entered: {text}')

uniquque_chars = set(text)
print(f'Unique characters: {uniquque_chars}')

if len(uniquque_chars) > 10:
    print('True')
else:
    print('False')
