import random

def generate_dataset(rows, columns, density):
    def col_label(i):
        label = ""
        while True:
            label = chr(ord('a') + (i % 26)) + label
            i = i // 26 - 1
            if i < 0:
                break
        return label

    labels = [col_label(i) for i in range(columns)]

    total = rows * columns
    ones = int(total * density)
    flat = [1]*ones + [0]*(total - ones)
    random.shuffle(flat)

    transactions = []
    for r in range(rows):
        start = r * columns
        row_bits = flat[start : start + columns]
        txn = [labels[c] for c, bit in enumerate(row_bits) if bit]
        transactions.append(txn)

    return transactions
