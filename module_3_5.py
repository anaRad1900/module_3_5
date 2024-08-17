def get_multiplied_digits(number):
    """Функция для рекурсивного умножения цифр в числе."""
    str_number = str(number)  # Преобразуем число в строку

    # Проверяем, есть ли хотя бы одна цифра
    if len(str_number) > 1:
        first = int(str_number[0])  # Первая цифра
        # Умножаем первую цифру на результат функции, передавая оставшиеся цифры
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)  # Возвращаем оставшуюся цифру

# Пример вызова функции
result = get_multiplied_digits(40203)
print(result)