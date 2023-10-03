def display_line(length, direction, character):
    if direction == 'горизонтальна':
        line = character * length
        print(line)
    elif direction == 'вертикальна':
        for _ in range(length):
            print(character)
    else:
        print("Неправильний напрямок. Використовуйте 'горизонтальна' або 'вертикальна'.")


display_line(10, 'горизонтальна', '*')


display_line(5, 'вертикальна', '?')







