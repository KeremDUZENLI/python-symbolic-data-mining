from algorithms.apriori import apriori, apriori_close, association_rule
from algorithms.eclat   import eclat


ALGORITHMS = {
    1: apriori,
    2: apriori_close,
    3: eclat,
    4: association_rule,
}


def run_algorithm(dataset, algorithm_choice, minimum_support, minimum_confidence):
    algorithm = ALGORITHMS.get(algorithm_choice)
    
    if algorithm_choice == 1:
        return algorithm(dataset, minimum_support), algorithm.__name__
    if algorithm_choice == 2:
        return algorithm(dataset, minimum_support), algorithm.__name__
    if algorithm_choice == 3:
        return algorithm(dataset, minimum_support), algorithm.__name__
    if algorithm_choice == 4:
        return algorithm(dataset, minimum_support, minimum_confidence), algorithm.__name__
