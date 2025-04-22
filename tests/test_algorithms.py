import unittest
from algorithms.apriori import apriori, apriori_close
from algorithms.eclat   import eclat


class TestFrequentItemsetAlgorithms(unittest.TestCase):
    def setUp(self):
        self.dataset = [
            ['a','b','d','e'],
            ['a','c'],
            ['a','b','c','e'],
            ['b','c','e'],
            ['a','b','c','e']
        ]
        self.minimum_support = 3

        self.expected_frequent_itemsets = {
            frozenset({'a'}): 4,
            frozenset({'b'}): 4,
            frozenset({'c'}): 4,
            frozenset({'e'}): 4,
            frozenset({'a','b'}): 3,
            frozenset({'a','c'}): 3,
            frozenset({'a','e'}): 3,
            frozenset({'b','c'}): 3,
            frozenset({'b','e'}): 4,
            frozenset({'c','e'}): 3,
            frozenset({'a','b','e'}): 3,
            frozenset({'b','c','e'}): 3,
        }

        self.expected_closed_itemsets = {
            frozenset({'a'}): 4,
            frozenset({'c'}): 4,
            frozenset({'a','c'}): 3,
            frozenset({'b','e'}): 4,
            frozenset({'a','b','e'}): 3,
            frozenset({'b','c','e'}): 3,
        }

    def test_apriori(self):
        all_frequent_itemsets = apriori(self.dataset, self.minimum_support)
        self.assertDictEqual(all_frequent_itemsets, self.expected_frequent_itemsets)

    def test_eclat(self):
        all_frequent_itemsets = eclat(self.dataset, self.minimum_support)
        self.assertDictEqual(all_frequent_itemsets, self.expected_frequent_itemsets)

    def test_apriori_closed(self):
        all_closed_itemsets = apriori_close(self.dataset, self.minimum_support)
        self.assertDictEqual(all_closed_itemsets, self.expected_closed_itemsets)


if __name__ == "__main__":
    unittest.main()

# <python -m unittest -v tests/test_algorithms.py>