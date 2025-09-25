from algorithms.apriori import apriori, apriori_rare, apriori_close, association_rule
from algorithms.eclat   import eclat


ALGORITHMS = {
    1: apriori,
    2: apriori_rare,
    3: apriori_close,
    4: eclat,
    5: association_rule,
}


def run_algorithm(dataset, algorithm_choice, minimum_support, minimum_confidence):
    algorithm = ALGORITHMS.get(algorithm_choice)
    
    if algorithm_choice == 5:
        return algorithm(dataset, minimum_support, minimum_confidence), algorithm.__name__
    else:
        return algorithm(dataset, minimum_support), algorithm.__name__
