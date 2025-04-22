def eclat(dataset, minimum_support):
    tidsets = transpose_dataset(dataset)
    items = [(itemset, tids) for itemset, tids in tidsets.items() if len(tids) >= minimum_support]
    all_frequent_itemsets = {}
    create_supersets_recursive(frozenset(), items, minimum_support, all_frequent_itemsets)
    return all_frequent_itemsets


def create_supersets_recursive(prefix, items, minimum_support, frequent_itemsets):
    for i, (itemset_i, tidset_i) in enumerate(items):
        support = len(tidset_i)
        if support < minimum_support:
            continue

        new_prefix = prefix | itemset_i
        frequent_itemsets[new_prefix] = support

        extensions = [
            (itemset_j, tidset_i & tidset_j)
            for itemset_j, tidset_j in items[i+1:]
            if len(tidset_i & tidset_j) >= minimum_support
        ]

        if extensions:
            create_supersets_recursive(new_prefix, extensions, minimum_support, frequent_itemsets)


def transpose_dataset(dataset):
    tidsets = {}
    for tid, transaction in enumerate(dataset):
        for item in transaction:
            tidsets.setdefault(frozenset([item]), set()).add(tid)
    return tidsets
