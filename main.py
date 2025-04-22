from algorithms.apriori import apriori, apriori_close
from algorithms.eclat import eclat


def run_algorithm(dataset, minimum_support, algorithm):
    if algorithm == "apriori":
        return apriori(dataset, minimum_support)
    if algorithm == "apriori_closed":
        return apriori_close(dataset, minimum_support)
    if algorithm == "eclat":
        return eclat(dataset, minimum_support)


def print_sorted_itemsets(itemsets):
    sorted_itemsets = sorted(itemsets.items(), key=lambda kv: (len(kv[0]), sorted(kv[0])))
    for itemset, support in sorted_itemsets:
        print(f"  {sorted(itemset)} : {support}")


dataset = [
    ['a', 'b', 'd', 'e'],
    ['a', 'c'],
    ['a', 'b', 'c', 'e'],
    ['b', 'c', 'e'],
    ['a', 'b', 'c', 'e']
]
minimum_support = 3
algorithm = "apriori_closed"  # Options: "apriori", "apriori_closed", "eclat"

frequent_itemsets = run_algorithm(dataset, minimum_support, algorithm)
print_sorted_itemsets(frequent_itemsets)