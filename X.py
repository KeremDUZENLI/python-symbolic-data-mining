from itertools import combinations
from typing import List, Dict, Tuple, FrozenSet, Union

# import your chosen mining algorithms
from algorithms.apriori import apriori, apriori_close
from algorithms.eclat import eclat
from helper.output import output_summary


def association_rules(dataset, minimum_support, minimum_confidence):
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

                confidence_AB = support_AB / support_A
                if confidence_AB >= minimum_confidence:
                    all_association_itemsets[(antecedent, consequent)] = (confidence_AB, support_AB, support_A)

    return all_association_itemsets




dataset = [
            ['a','b','d','e'],
            ['a','c'],
            ['a','b','c','e'],
            ['b','c','e'],
            ['a','b','c','e']
        ]
minimum_support = 3
minimum_confidence = 0.5

all_association_itemsets = association_rules(dataset, minimum_support, minimum_confidence)
labels = []
algorithm_choice = 0
lines = output_summary(dataset, labels, minimum_support, algorithm_choice, all_association_itemsets)
print(*lines, sep='\n')
