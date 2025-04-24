from algorithms.apriori import apriori, apriori_close
from algorithms.eclat   import eclat

from cli.prompt         import PROMPT
from gui.window         import GUI

from helper.dataset     import generate_dataset
from helper.output      import output_summary


ALGORITHMS = {1: "apriori", 2: "apriori_close", 3: "eclat"}


def run_algorithm(dataset, minimum_support, algorithm):
    if algorithm == "apriori":
        return apriori(dataset, minimum_support)
    if algorithm == "apriori_close":
        return apriori_close(dataset, minimum_support)
    if algorithm == "eclat":
        return eclat(dataset, minimum_support)
    raise ValueError(f"Unknown algorithm: {algorithm}")



# PROMPT(generate_dataset, run_algorithm, output_summary, ALGORITHMS)

GUI(generate_dataset, run_algorithm, output_summary, ALGORITHMS)

