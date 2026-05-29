def bubble_sort(data):

    n = len(data)

    for i in range(n):

        for j in range(0, n - i - 1):

            if data[j].suara < data[j + 1].suara:

                data[j], data[j + 1] = data[j + 1], data[j]

    return data