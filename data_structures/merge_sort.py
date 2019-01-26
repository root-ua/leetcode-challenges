def merge_sort(elements):

    if len(elements) <= 1:
        return elements
    else:

        midpoint = len(elements) // 2

        left_array = merge_sort(elements[:midpoint])
        right_array = merge_sort(elements[midpoint:])

        return merge_halves(left_array, right_array)


def merge_halves(left_array, right_array):

    output = []

    idx_left, idx_right = 0, 0

    while idx_left < len(left_array) and idx_right < len(right_array):
        if left_array[idx_left] <= right_array[idx_right]:
            output.append(left_array[idx_left])
            idx_left += 1
        else:
            output.append(right_array[idx_right])
            idx_right += 1

    output.extend(left_array[idx_left:])
    output.extend(right_array[idx_right:])

    return output


if __name__ == '__main__':

    cases = [
        {
            'input':  [10, 5, 1, 4, 22, 7, 15, 11],
            'output': [1, 4, 5, 7, 10, 11, 15, 22],
        },
        {
            'input':  [12, 11, 13, 5, 6, 7],
            'output': [5, 6, 7, 11, 12, 13],
        },
        {
            'input':  [5, 9, 1, 2, 7, 0],
            'output': [0, 1, 2, 5, 7, 9],
        },
        {
            'input':  [3, 1, 5, 3, 2, 5, 8, 2, 9, 6, 12, 53, 75, 22, 83, 123, 12123],
            'output': [1, 2, 2, 3, 3, 5, 5, 6, 8, 9, 12, 22, 53, 75, 83, 123, 12123],
        },
    ]

    for case in cases:
        output = merge_sort(case['input'])
        matched = True if output == case['output'] else False
        print('input: %s, output: %s, matched: %s' % (case['input'], output, matched))
