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
    sorted_itemsets = sorted(all_frequent_itemsets.items(), key=lambda kv: (
        *( (len(kv[0][0]), len(kv[0][1])) if isinstance(kv[0], tuple) else (len(kv[0]), 0) ),
        *( (sorted(kv[0][0]), sorted(kv[0][1])) if isinstance(kv[0], tuple) else (sorted(kv[0]), []) )))
           
    lines.extend((f"{', '.join(sorted(itemset[0]))} => {', '.join(sorted(itemset[1]))} : {support}"
                  if isinstance(itemset, tuple) else f"{', '.join(sorted(itemset))} : {support}")
                  for itemset, support in sorted_itemsets)
    
    lines.append("\n===== SUMMARY =====")
    lines.append(f"Total number of rows    : {len(dataset)}")
    lines.append(f"Total number of columns : {len(labels)}")
    lines.append(f"Density                 : {sum(len(x) for x in dataset) / (len(dataset) * len(labels) or 1):.2%}")
    lines.append(f"Minimum support         : {minimum_support}")
    lines.append(f"Minimum support         : {minimum_confidence:.2%}")
    lines.append(f"Chosen algorithm        : {algorithm_choice}")
    lines.append(f"FIs & FCIs              : {len(all_frequent_itemsets)}")
    
    lines.append("\n--------------------------------------------------")
    return lines
