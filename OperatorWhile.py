my_list = [2, 42, 69, 322, 13, 2, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] < 2: # вопрос - почему игнорирует 2? или 0 без разницы? почему не выводит цифры после отрицательных значений как и после 0?
        break
    if my_list[i] > 2:
        print(my_list[i])
    i += 1               # i = (i + 1)