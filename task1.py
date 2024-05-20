def sorted_merge(list_a: list[int], list_b: list[int]) -> list[int]:
    """Функия принимает два отсротированных списка(по возрастанию) длиной  a и b
    и возвращает отсротированный(по убыванию) результирующий список,
    Сортировка слиянием"""

    res = []
    a = len(list_a)
    b = len(list_b)
    index_a, index_b = a - 1, b - 1

    while index_a > -1 and index_b > -1:
        if list_a[index_a] > list_b[index_b]:
            res.append(list_a[index_a])
            index_a -= 1
        else:
            res.append(list_b[index_b])
            index_b -= 1

    if index_a == -1:
        while index_b > -1:
            res.append(list_b[index_b])
            index_b -= 1
    else:
        while index_a > -1:
            res.append(list_a[index_a])
            index_a -= 1

    return res


lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]
result = sorted_merge(lst1, lst2)
print(*result)
