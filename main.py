from algorithms.apriori import apriori, apriori_close
from algorithms.eclat   import eclat
from helper.dataset     import generate_dataset
from helper.print       import print_summary, prompt


ALGORITHMS = {1: "apriori", 2: "apriori_close", 3: "eclat"}

def run_algorithm(dataset, minimum_support, algorithm):
    if algorithm == "apriori":
        return apriori(dataset, minimum_support)
    if algorithm == "apriori_close":
        return apriori_close(dataset, minimum_support)
    if algorithm == "eclat":
        return eclat(dataset, minimum_support)
    raise ValueError(f"Unknown algorithm: {algorithm}")


def run_prompt():
    rows = prompt("Number of Rows", maximum=10)
    columns = prompt("Number of Columns", maximum=10)
    density = prompt("Density", maximum=100) /100
    dataset, labels = generate_dataset(rows, columns, density)
    
    minimum_support = prompt("Minimum Support", maximum=max(rows, columns))
    algorithm_choice = prompt(f"Select algorithm {ALGORITHMS}", minimum=1, maximum=3)
    frequent_itemsets = run_algorithm(dataset, minimum_support, ALGORITHMS[algorithm_choice])
    
    return dataset, labels, minimum_support, ALGORITHMS[algorithm_choice], frequent_itemsets


print_summary(*run_prompt())
