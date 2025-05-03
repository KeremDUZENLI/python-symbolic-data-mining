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
    lines     = []
    
    lines.append('\n===== ITEMSETS =====')      
    sorted_itemsets = sorted(all_frequent_itemsets.items(), key=_sort_itemsets)
    
    raw_lines = [ _format_sorted_itemsets(itemset, itemset_values) for itemset, itemset_values in sorted_itemsets ]
    columns = list(zip(*raw_lines))
    maximum_widths = [max(len(item) for item in column) for column in columns]
    
    for line in raw_lines:
        if len(line) == 4:
            column_association, column_confidence, column_support_AB, column_support_A = line
            lines.append(
                f"{column_association:<{maximum_widths[0]}} : "
                f"{column_confidence:<{maximum_widths[1]}} | "
                f"{column_support_AB:<{maximum_widths[2]}} | "
                f"{column_support_A:<{maximum_widths[3]}}"
            )   
        else:
            column_association, column_support_A = line
            lines.append(
                f"{column_association:<{maximum_widths[0]}} : "
                f"{column_support_A}"
            )
    
    lines.append("\n===== SUMMARY =====")
    lines.append(f"Total number of rows    : {len(dataset)}")
    lines.append(f"Total number of columns : {len(labels)}")
    lines.append(f"Density                 : {sum(len(x) for x in dataset) / (len(dataset) * len(labels) or 1):.2%}")
    lines.append(f"Chosen algorithm        : {algorithm_choice}")
    lines.append(f"Minimum support         : {minimum_support}")
    lines.append(f"Minimum confidence      : {f'{minimum_confidence:.2f}%' if minimum_confidence is not None else ''}")
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
        A, B      = itemset
        sorted_A  = ', '.join(sorted(A))
        sorted_B  = ', '.join(sorted(B))
        sorted_AB = ''.join(sorted_A + sorted_B)
        confidence_AB, support_AB, support_A = itemset_values

        column_association = f"{sorted_A} => {sorted_B}"
        column_confidence  = f"confidence({sorted_AB})={confidence_AB:.2%}"
        column_support_AB  = f"support({sorted_AB})={support_AB}"
        column_support_A   = f"support({sorted_A})={support_A}"
        return (
            column_association,
            column_confidence,
            column_support_AB,
            column_support_A,
        )
    else:   
        sorted_A  = ', '.join(sorted(itemset))
        support_A = itemset_values
        
        column_association = f"{sorted_A}"
        column_support_A   = f"support({sorted_A})={support_A}"
        return(
            column_association,
            column_support_A,
        )
