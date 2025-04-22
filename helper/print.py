def print_summary(dataset, frequent_itemsets, minimum_support, algorithm):
    number_rows = len(dataset)
    columns = set()
    for transaction in dataset:
        for item in transaction:
            columns.add(item)
    number_columns = len(columns)
    
    total_occurrences = sum(len(txn) for txn in dataset)
    total_cells = number_rows * number_columns if number_rows * number_columns else 1
    density = total_occurrences / total_cells

    print("\n===== SUMMARY =====")
    print(f"Total number of rows    : {number_rows}")
    print(f"Total number of columns : {number_columns}")
    print(f"Density                 : {density:.2%}")
    print(f"Minimum support         : {minimum_support}")
    print(f"Chosen algorithm        : {algorithm}")
    print(f"{'FCIs' if algorithm == 'apriori_closed' else 'FIs':24}: {len(frequent_itemsets)}")
    
    print("\n===== FREQUENT ITEMSETS =====")
    print_sorted_itemsets(frequent_itemsets)


def print_sorted_itemsets(itemsets):
    sorted_itemsets = sorted(itemsets.items(), key=lambda kv: (len(kv[0]), sorted(kv[0])))
    for itemset, support in sorted_itemsets:
        print(f"{sorted(itemset)} : {support}")
