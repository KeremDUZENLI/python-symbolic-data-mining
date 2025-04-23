from algorithms.apriori import apriori, apriori_close
from algorithms.eclat import eclat
from helper.print import print_summary
from helper.dataset import generate_dataset


def run_algorithm(dataset, minimum_support, algorithm):
    if algorithm == "apriori":
        return apriori(dataset, minimum_support)
    if algorithm == "apriori_close":
        return apriori_close(dataset, minimum_support)
    if algorithm == "eclat":
        return eclat(dataset, minimum_support)

rows = 5
columns = 5
density = 0.6
minimum_support = 3
algorithm = "apriori_close"  # Options: "apriori", "apriori_close", "eclat"

dataset = generate_dataset(rows, columns, density)
frequent_itemsets = run_algorithm(dataset, minimum_support, algorithm)
print_summary(dataset, frequent_itemsets, minimum_support, algorithm)
