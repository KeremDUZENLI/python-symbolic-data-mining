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


def output_summary(dataset, labels, minimum_support, minimum_confidence, algorithm_choice, all_frequent_itemsets):
    lines = []
    
    lines.append('\n===== ITEMSETS =====')      
    sorted_itemsets = sorted(all_frequent_itemsets.items(), key=_sort_itemsets)
    for itemset, itemset_values in sorted_itemsets:
        line = _format_sorted_itemsets(itemset, itemset_values)
        lines.append(line)      
    
    lines.append("\n===== SUMMARY =====")
    lines.append(f"Total number of rows    : {len(dataset)}")
    lines.append(f"Total number of columns : {len(labels)}")
    lines.append(f"Density                 : {sum(len(x) for x in dataset) / (len(dataset) * len(labels) or 1):.2%}")
    lines.append(f"Chosen algorithm        : {algorithm_choice}")
    lines.append(f"Minimum support         : {minimum_support}")
    lines.append(f"Minimum confidence      : {(minimum_confidence / 100):.2%}")
    lines.append(f"FIs & FCIs              : {len(all_frequent_itemsets)}")
    
    lines.append("\n--------------------------------------------------")
    return lines


def _sort_itemsets(key_and_value):
    itemset, _ = key_and_value
    if isinstance(itemset, tuple):
        lhs, rhs = itemset
        return (len(lhs), len(rhs), sorted(lhs), sorted(rhs))
    else:
        return (len(itemset), 0, sorted(itemset), [])
    
    
def _format_sorted_itemsets(itemset, itemset_values):
    if isinstance(itemset, tuple):
        A, B = itemset
        sorted_A = sorted(A)
        sorted_B = sorted(B)
        AB = ''.join(sorted_A + sorted_B)
        confidence, support_AB, support_A = itemset_values
        return(
            f"{', '.join(sorted_A)} => {', '.join(sorted_B)} : "
            f"(confidence({AB})={confidence:.2f}% | "
            f"support({AB})={support_AB} | "
            f"support({''.join(sorted_B)})={support_A})"
        )
    else:
        sorted_itemset = sorted(itemset)
        support = itemset_values
        return(
            f"{', '.join(sorted_itemset)} : support({''.join(sorted_itemset)})={support}"
        )
