from algorithms.apriori import apriori, apriori_close
from algorithms.eclat   import eclat

from interface.cli         import CLI
from interface.gui         import GUI

from helper.dataset     import create_dataset
from helper.output      import output_summary


def run_algorithm(dataset, minimum_support, algorithm_choice):
    ALGORITHMS = {1: "apriori", 2: "apriori_close", 3: "eclat"}
    
    if ALGORITHMS[algorithm_choice] == "apriori":
        return apriori(dataset, minimum_support)
    if ALGORITHMS[algorithm_choice] == "apriori_close":
        return apriori_close(dataset, minimum_support)
    if ALGORITHMS[algorithm_choice] == "eclat":
        return eclat(dataset, minimum_support)
    raise ValueError(f"Unknown algorithm: {algorithm_choice}")


CLI(create_dataset, run_algorithm, output_summary)
GUI(create_dataset, run_algorithm, output_summary)
