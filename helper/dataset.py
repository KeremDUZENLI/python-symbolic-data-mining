import random
from helper import create_column_labels


def create_dataset(rows, columns, density):
    labels = [create_column_labels(item) for item in range(columns)]

    total_cells = rows * columns
    occurencies = int(total_cells * (density / 100))
    flat = [1]*occurencies + [0]*(total_cells - occurencies)
    random.shuffle(flat)

    dataset = []
    for row in range(rows):
        start = row * columns
        row_bits = flat[start : start + columns]
        txn = [labels[c] for c, filled in enumerate(row_bits) if filled]
        dataset.append(txn)

    return dataset, labels


def create_dataset_default():
    dataset = [
        ['a','b','d','e'],
        ['a','c'],
        ['a','b','c','e'],
        ['b','c','e'],
        ['a','b','c','e'],
    ]
    dataset = [[item.upper() for item in txn] for txn in dataset]
    
    unique_items = sorted(set(item for txn in dataset for item in txn))
    num_columns = len(unique_items)
    labels = [create_column_labels(item) for item in range(num_columns)]

    return dataset, labels


def create_dataset_from_grid(grid):
    labels = [create_column_labels(item) for item in range(len(grid[0]))]

    dataset = []
    for row in grid:
        txn = [ labels[c] for c, filled in enumerate(row) if filled ]
        dataset.append(txn)

    return dataset, labels
