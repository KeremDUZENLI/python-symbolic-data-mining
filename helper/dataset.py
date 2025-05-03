import random


def create_dataset_default():
    dataset = [
        ['a','b','d','e'],
        ['a','c'],
        ['a','b','c','e'],
        ['b','c','e'],
        ['a','b','c','e']
    ]
    labels = sorted({item for rows in dataset for item in rows})
    return dataset, labels


def create_dataset(rows, columns, density):
    def col_label(i):
        label = ""
        while True:
            label = chr(ord('a') + (i % 26)) + label
            i = i // 26 - 1
            if i < 0:
                break
        return label

    labels = [col_label(i) for i in range(columns)]

    total_cells = rows * columns
    occurencies = int(total_cells * (density / 100))
    flat = [1]*occurencies + [0]*(total_cells - occurencies)
    random.shuffle(flat)

    dataset = []
    for r in range(rows):
        start = r * columns
        row_bits = flat[start : start + columns]
        txn = [labels[c] for c, bit in enumerate(row_bits) if bit]
        dataset.append(txn)

    return dataset, labels
