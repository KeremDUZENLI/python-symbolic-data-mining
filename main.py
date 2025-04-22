from algorithms.apriori import apriori, apriori_close
from algorithms.eclat import eclat
from helper.print import print_summary


def run_algorithm(dataset, minimum_support, algorithm):
    if algorithm == "apriori":
        return apriori(dataset, minimum_support)
    if algorithm == "apriori_closed":
        return apriori_close(dataset, minimum_support)
    if algorithm == "eclat":
        return eclat(dataset, minimum_support)

dataset = [
    ['a', 'b', 'd', 'e'],
    ['a', 'c'],
    ['a', 'b', 'c', 'e'],
    ['b', 'c', 'e'],
    ['a', 'b', 'c', 'e']
]
minimum_support = 3
algorithm = "eclat"  # Options: "apriori", "apriori_closed", "eclat"

frequent_itemsets = run_algorithm(dataset, minimum_support, algorithm)
print_summary(dataset, frequent_itemsets, minimum_support, algorithm)