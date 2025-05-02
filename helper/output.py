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
    
    lines.append("\n===== ITEMSETS =====")
    info_list = [_extract_itemset_info(itemset, vals) for itemset, vals in sorted(all_frequent_itemsets.items(), key=_sort_itemsets)]
    max_width = max((len(info["group"]) for info in info_list), default=0)

    for info in info_list:
        label = info["group"].ljust(max_width)
        if "support" in info:
            key = info["group"].replace(", ", "")
            lines.append(f"{label} : support({key}) = {info['support']}")
        else:
            lines.append(
                f"{label} : "
                f"(confidence({info['AB']}) = {info['confidence']:.2%} | "
                f"support({info['AB']}) = {info['support_AB']} | "
                f"support({''.join(info['group'].split(', ')[:-1])}) = {info['support_A']})"
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


def _extract_itemset_info(itemset, itemset_values):
    if isinstance(itemset, tuple):
        A, B  = itemset
        group = f"{', '.join(sorted(A))} => {', '.join(sorted(B))}"
        AB    = ''.join(sorted(A) + sorted(B))
        confidence, support_AB, support_A = itemset_values
        return {
            "group"      : group,
            "AB"         : AB,
            "confidence" : confidence,
            "support_AB" : support_AB,
            "support_A"  : support_A,
        }
    else:
        group   = ", ".join(sorted(itemset))
        support = itemset_values
        return {
            "group"   : group,
            "support" : support
        }
