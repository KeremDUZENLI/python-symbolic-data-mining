def output_dataset(dataset, labels):      
    rows = len(dataset)
    pad = len(str(rows))
    sep = " | "

    lines = []
    lines.append('\n===== DATASET =====')
    lines.append(" " * (pad + 1) + sep.join(labels))

    for idx, symbol_X in enumerate(dataset, start=1):
        cells = ["X" if column in symbol_X else " " for column in labels]
        lines.append(f"{idx:>{pad}} " + sep.join(cells))

    lines.append("\n--------------------------------------------------")
    return lines


def output_summary(dataset, labels, minimum_support, algorithm_choice, frequent_itemsets):
    lines = []
    lines.append('\n===== ITEMSETS =====')
    lines.extend(output_itemsets(frequent_itemsets))
    
    lines.append("\n===== SUMMARY =====")
    lines.append(f"Total number of rows    : {len(dataset)}")
    lines.append(f"Total number of columns : {len(labels)}")
    lines.append(f"Density                 : {sum(len(x) for x in dataset) / (len(dataset) * len(labels) or 1):.2%}")
    lines.append(f"Minimum support         : {minimum_support}")
    lines.append(f"Chosen algorithm        : {algorithm_choice}")
    lines.append(f"FIs & FCIs              : {len(frequent_itemsets)}")
    
    lines.append("\n--------------------------------------------------")
    return lines


def output_itemsets(itemsets):
    sorted_itemsets = sorted(itemsets.items(), key=lambda kv: (len(kv[0]), sorted(kv[0])))
    return [f"{sorted(itemset)} : {support}" for itemset, support in sorted_itemsets]
