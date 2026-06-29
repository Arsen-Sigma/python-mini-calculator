first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
operation = input("Введите операцию: ")

if operation == "+":
    print("Ответ", first_number + second_number)
elif operation == "-":
    print("Ответ", first_number - second_number)
elif operation == "*":
    print("Ответ", first_number * second_number)
elif operation == "/":
    print("Ответ", first_number / second_number)
elif operation == "//":
    print("Ответ", first_number // second_number)
elif operation == "**":
    print("Ответ", first_number ** second_number)
else:
    print("Неизвестная операция")
