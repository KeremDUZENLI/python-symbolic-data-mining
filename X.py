from algorithms.apriori import apriori_rare

dataset = [
            ['a','b','d','e'],
            ['a','c'],
            ['a','b','c','e'],
            ['b','c','e'],
            ['a','b','c','e']
        ]
minimum_support = 3


print(apriori_rare(dataset, minimum_support))
