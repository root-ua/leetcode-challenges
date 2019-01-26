def lis(elements):

    max_length = 1
    best_end = 0
    n = len(elements)

    memory = [1] * n
    prev = [-1] * n

    for i in range(0, n-1):

        memory[i] = 1
        prev[i] = -1

        for j in range(i, 0, -1):
            print('i=%d, j=%d' % (i, j))
            if memory[j] + 1 > memory[i] and elements[j] < elements[i]:
                memory[i] = memory[j] + 1
                prev[i] = j

        if memory[i] > max_length:
            best_end = i
            max_length = memory[i]

    return max_length, best_end


if __name__ == '__main__':
    elements = [2, 6, 3, 4, 1, 2, 9, 5, 8]
    print(lis(elements))
