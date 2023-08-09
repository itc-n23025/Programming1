def pern_sequence(limit=100):
    sequence = [3, 0, 2]

    while True:
        next_num = sequence[-2] + sequence[-3]
        if next_num >= limit:
            break
        sequence.append(next_num)

    return sequence


result = pern_sequence(100)
print(result)
