Numbers = 34, 58, 33, 578, 1, 9
x = int(input('Введите число:'))
array = list(Numbers) + [x]
if x < min(list(Numbers)) or x > max(list(Numbers)):
    print("Элемент за пределами списка, поиск индекса невозможен")
    raise Exception


print(array)


for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
    m = min(array)


print(array)


def binary_search(array, element, left, right):

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = x


print('Индекс элемента, описанного в условии, равен:', binary_search(array, element, 0, len(array)-1)-1)

