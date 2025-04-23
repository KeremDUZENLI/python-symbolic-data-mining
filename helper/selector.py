from algorithms.apriori import apriori, apriori_close
from algorithms.eclat import eclat


def run_algorithm(dataset, minimum_support, algorithm):
    if algorithm == "apriori":
        return apriori(dataset, minimum_support)
    if algorithm == "apriori_close":
        return apriori_close(dataset, minimum_support)
    if algorithm == "eclat":
        return eclat(dataset, minimum_support)
    raise ValueError(f"Unknown algorithm: {algorithm}")
