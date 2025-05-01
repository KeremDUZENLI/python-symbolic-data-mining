from itertools import combinations


def apriori(dataset, minimum_support):
    candidate_itemsets = {frozenset([item]) for transaction in dataset for item in transaction}
    itemset_size = 1
    all_frequent_itemsets = {}

    while candidate_itemsets:
        frequent_itemsets = find_frequent_itemsets(dataset, candidate_itemsets, minimum_support)
        if not frequent_itemsets:
            break
        all_frequent_itemsets.update(frequent_itemsets)
        itemset_size += 1
        candidate_itemsets = create_supersets(set(frequent_itemsets.keys()), itemset_size)

    return all_frequent_itemsets


def apriori_close(dataset, minimum_support):
    all_frequent_itemsets = apriori(dataset, minimum_support)
    all_closed_itemsets = find_closed_itemsets(all_frequent_itemsets)
    return all_closed_itemsets


def association_rule(dataset, minimum_support, minimum_confidence):
    all_frequent_itemsets = apriori(dataset, minimum_support)
    all_association_itemsets = {}

    for itemset, support_AB in all_frequent_itemsets.items():
        if len(itemset) < 2:
            continue
        for each_range in range(1, len(itemset)):
            for antecedent in combinations(itemset, each_range):
                antecedent = frozenset(antecedent)
                consequent = itemset - antecedent
                support_A = all_frequent_itemsets.get(antecedent, 0)

                if support_A == 0:
                    continue

                confidence_AB = (support_AB / support_A) * 100
                if confidence_AB >= minimum_confidence:
                    all_association_itemsets[(antecedent, consequent)] = (confidence_AB, support_AB, support_A)

    return all_association_itemsets


def find_frequent_itemsets(dataset, prev_itemsets, minimum_support):
    each_itemset_frequency = {itemset: 0 for itemset in prev_itemsets}
    for row in dataset:
        row_set = set(row)
        for itemset in prev_itemsets:
            if itemset.issubset(row_set):
                each_itemset_frequency[itemset] += 1
    return {itemset: freq for itemset, freq in each_itemset_frequency.items() if freq >= minimum_support}


def find_closed_itemsets(dataset):
    closed_itemsets = {}
    items = list(dataset.items())
    for i, (I, support_I) in enumerate(items):
        is_closed = True
        for J, support_J in items:
            if I < J and support_I == support_J:
                is_closed = False
                break
        if is_closed:
            closed_itemsets[I] = support_I
    return closed_itemsets


def create_supersets(prev_itemsets, itemset_size):
    supersets = set()
    itemsets_list = list(prev_itemsets)
    for i in range(len(itemsets_list)):
        for j in range(i + 1, len(itemsets_list)):
            candidate = itemsets_list[i] | itemsets_list[j]
            if len(candidate) == itemset_size:
                supersets.add(candidate)
    return supersets
