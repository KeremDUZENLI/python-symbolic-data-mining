from algorithms.apriori import apriori, apriori_close, association_rule
from algorithms.eclat   import eclat

from interface.cli         import CLI
from interface.gui         import GUI

from helper.dataset     import create_dataset
from helper.output      import output_dataset, output_summary


def run_algorithm(dataset, minimum_support, minimum_confidence, algorithm_choice):
    ALGORITHMS = {1: "apriori", 2: "apriori_close", 3: "eclat", 4: "association_rule"}
    
    if ALGORITHMS[algorithm_choice] == "apriori":
        return apriori(dataset, minimum_support)
    if ALGORITHMS[algorithm_choice] == "apriori_close":
        return apriori_close(dataset, minimum_support)
    if ALGORITHMS[algorithm_choice] == "eclat":
        return eclat(dataset, minimum_support)
    if ALGORITHMS[algorithm_choice] == "association_rule":
        return association_rule(dataset, minimum_support, minimum_confidence)

    raise ValueError(f"Unknown algorithm: {algorithm_choice}")


CLI(create_dataset, run_algorithm, output_dataset, output_summary)
GUI(create_dataset, run_algorithm, output_dataset, output_summary)


# <./core02_assrulex.sh sample/laszlo.rcf 3 50% -alg:apriori -rule:all --names>
