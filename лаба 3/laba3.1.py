def write_text_to_file():
    
    with open('user_input.txt', 'a') as file:
        text = input('Введите текст для добавления в файл: ')
        file.write(text + '\n')
    
    with open('user_input.txt', 'r') as file:
        content = file.read()
    return content

file_input = write_text_to_file()
print(file_input)

    