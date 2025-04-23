from helper.dataset     import generate_dataset
from helper.print       import print_summary, prompt
from helper.selector    import run_algorithm


ALGORITHMS = {1: "apriori", 2: "apriori_close", 3: "eclat"}


rows = prompt("Number of Rows", maximum=10)
columns = prompt("Number of Columns", maximum=10)
density = prompt("Density", maximum=100) /100
minimum_support = prompt("Minimum Support", maximum=int(rows*columns*density)+1)
algorithm_choice = prompt(f"Select algorithm {ALGORITHMS}", minimum=1, maximum=3)
dataset, labels = generate_dataset(rows, columns, density)
frequent_itemsets = run_algorithm(dataset, minimum_support, ALGORITHMS[algorithm_choice])

print_summary(dataset, labels, frequent_itemsets, minimum_support, ALGORITHMS[algorithm_choice])
