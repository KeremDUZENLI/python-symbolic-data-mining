from algorithms.apriori import apriori, apriori_rare, apriori_close, association_rule
from algorithms.eclat   import eclat
import unittest


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
        self.minimum_confidence = 50

        self.expected_apriori = {
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
        
        self.expected_apriori_rare = {
            frozenset({'d'}): 1,
            frozenset({'a', 'b', 'c'}): 2,
            frozenset({'a', 'c', 'e'}): 2,
        }

        self.expected_apriori_close = {
            frozenset({'a'}): 4,
            frozenset({'c'}): 4,
            frozenset({'a','c'}): 3,
            frozenset({'b','e'}): 4,
            frozenset({'a','b','e'}): 3,
            frozenset({'b','c','e'}): 3,
        }
        
        self.expected_association_rule = {
            (frozenset({'a'}), frozenset({'b'})): (0.75, 3, 4), 
            (frozenset({'a'}), frozenset({'c'})): (0.75, 3, 4), 
            (frozenset({'a'}), frozenset({'e'})): (0.75, 3, 4),
            (frozenset({'b'}), frozenset({'a'})): (0.75, 3, 4), 
            (frozenset({'b'}), frozenset({'c'})): (0.75, 3, 4), 
            (frozenset({'b'}), frozenset({'e'})): (1.0, 4, 4), 
            (frozenset({'c'}), frozenset({'a'})): (0.75, 3, 4), 
            (frozenset({'c'}), frozenset({'b'})): (0.75, 3, 4), 
            (frozenset({'c'}), frozenset({'e'})): (0.75, 3, 4), 
            (frozenset({'e'}), frozenset({'a'})): (0.75, 3, 4), 
            (frozenset({'e'}), frozenset({'b'})): (1.0, 4, 4), 
            (frozenset({'e'}), frozenset({'c'})): (0.75, 3, 4), 
            
            (frozenset({'a'}), frozenset({'b', 'e'})): (0.75, 3, 4), 
            (frozenset({'b'}), frozenset({'a', 'e'})): (0.75, 3, 4), 
            (frozenset({'b'}), frozenset({'c', 'e'})): (0.75, 3, 4), 
            (frozenset({'c'}), frozenset({'b', 'e'})): (0.75, 3, 4), 
            (frozenset({'e'}), frozenset({'a', 'b'})): (0.75, 3, 4), 
            (frozenset({'e'}), frozenset({'b', 'c'})): (0.75, 3, 4), 
            
            (frozenset({'a', 'b'}), frozenset({'e'})): (1.0, 3, 3), 
            (frozenset({'a', 'e'}), frozenset({'b'})): (1.0, 3, 3), 
            (frozenset({'b', 'c'}), frozenset({'e'})): (1.0, 3, 3), 
            (frozenset({'b', 'e'}), frozenset({'a'})): (0.75, 3, 4), 
            (frozenset({'b', 'e'}), frozenset({'c'})): (0.75, 3, 4), 
            (frozenset({'c', 'e'}), frozenset({'b'})): (1.0, 3, 3),
        }


    def test_apriori(self):
        all_frequent_itemsets = apriori(self.dataset, self.minimum_support)
        self.assertDictEqual(all_frequent_itemsets, self.expected_apriori)
        
    def test_apriori_rare(self):
        all_closed_itemsets = apriori_rare(self.dataset, self.minimum_support)
        self.assertDictEqual(all_closed_itemsets, self.expected_apriori_rare)

    def test_apriori_closed(self):
        all_closed_itemsets = apriori_close(self.dataset, self.minimum_support)
        self.assertDictEqual(all_closed_itemsets, self.expected_apriori_close)
        
    def test_eclat(self):
        all_frequent_itemsets = eclat(self.dataset, self.minimum_support)
        self.assertDictEqual(all_frequent_itemsets, self.expected_apriori)
        
    def test_association_rule(self):
        all_frequent_itemsets = association_rule(self.dataset, self.minimum_support, self.minimum_confidence)
        self.assertDictEqual(all_frequent_itemsets, self.expected_association_rule)


if __name__ == "__main__":
    unittest.main()

# <python -m unittest -v tests/test_algorithms.py>