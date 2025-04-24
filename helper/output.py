def output_summary(dataset, labels, minimum_support, algorithm_choice, frequent_itemsets):
    number_rows = len(dataset)
    unique_items = {item for txt in dataset for item in txt}
    number_columns = len(unique_items)

    total_occurrences = sum(len(txn) for txn in dataset)
    total_cells = number_rows * number_columns or 1
    density = total_occurrences / total_cells

    lines = []
    
    lines.append("\n===== SUMMARY =====")
    lines.append(f"Total number of rows    : {number_rows}")
    lines.append(f"Total number of columns : {number_columns}")
    lines.append(f"Density                 : {density:.2%}")
    lines.append(f"Minimum support         : {minimum_support}")
    lines.append(f"Chosen algorithm        : {algorithm_choice}")
    lines.append(f"FIs & FCIs              : {len(frequent_itemsets)}")
  
    lines.append('\n===== DATASET =====')
    lines.extend(draw_dataset(dataset, labels))

    lines.append('\n===== ITEMSETS =====')
    lines.extend(sort_itemset(frequent_itemsets))
    
    return lines


def draw_dataset(dataset, labels):      
    rows = len(dataset)
    pad = len(str(rows))
    sep = " | "

    header = " " * (pad + 1) + sep.join(labels)
    lines = []
    lines.append(header)

    for idx, symbol_X in enumerate(dataset, start=1):
        cells = ["X" if column in symbol_X else " " for column in labels]
        lines.append(f"{idx:>{pad}} " + sep.join(cells))

    return lines


def sort_itemset(itemsets):
    sorted_itemsets = sorted(itemsets.items(), key=lambda kv: (len(kv[0]), sorted(kv[0])))
    return [f"{sorted(itemset)} : {support}" for itemset, support in sorted_itemsets]
