# IPPV534-K2 Symbolic Data Mining

A Python toolkit for mining symbolic transactional data. Supports:

- **Frequent‐itemset mining**: Apriori, Apriori-Close, Apriori-Rare, Eclat  
- **Association rules**: Confidence‐based rule generation  

Two user interfaces:

1. **CLI** – interactive console  
2. **GUI** – Tkinter desktop app (draw your own dataset!)  


## Features

- **Default dataset** (“Laszlo.rcf”) plus random‐generation by rows/cols/density  
- **Draw mode**: click-to-fill cells on a grid and auto-compute density  
- **Sort & format**: clear, aligned output of itemsets & rules  
- **Cross-platform packing**: ready for Windows, macOS & Linux  


## Usage

### CLI

* `[r]` generate a random dataset
* `[d]` load default “Laszlo.rcf” dataset
* `[Enter]` choose algorithm & support/confidence, then run
* `[q]` quit

### GUI

1. Set **Rows**, **Columns**, **Density**
2. Click **Draw Dataset** to manually fill cells (or **Laszlo.rcf** to load default)
3. Select **Algorithm** and (if Association Rule) **Min. Confidence**
4. **Generate Dataset** → **Generate Result**


## Algorithms

| ID | Name               | Output                                      |
| -- | ------------------ | ------------------------------------------- |
| 1  | `apriori`          | all frequent itemsets by support threshold  |
| 2  | `apriori_close`    | closed frequent itemsets only               |
| 3  | `apriori_rare`     | rare itemsets below support threshold       |
| 4  | `eclat`            | vertical‐format frequent itemsets           |
| 5  | `association_rule` | association rules (antecedent ⇒ consequent) |


## Project Tree

```bash
├── algorithms
│   ├── __init__.py
│   ├── apriori.py
│   └── eclat.py
├── helper
│   ├── __init__.py
│   ├── dataset.py
│   └── output.py
├── interface
│   ├── cli.py
│   └── gui.py
├── notes
│   └── Notes_Kerem.pdf
├── tests
│   └── test_algorithms.py
├── main.py
├── LICENSE
├── README.md
```


## Acknowledgments

This project is based on the **Symbolic Data Mining** course at the **University of Debrecen**

- **Dr. László Szathmáry** – Instructor of Symbolic Data Mining Course

  - _Department of Information Technology, Faculty of Informatics, University of Debrecen_
  - Email: [szathmary.laszlo@inf.unideb.hu](mailto:szathmary.laszlo@inf.unideb.hu)


- **Kerem Düzenli** – PhD Candidate, University of Debrecen

  - _Creator and maintainer of this repository_
  - Email: [kerem.duzenli@inf.unideb.hu](mailto:kerem.duzenli@inf.unideb.hu)


## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. This means you are free to:

- **Share** – Copy and redistribute the material in any medium or format.
- **Adapt** – Remix, transform, and build upon the material.

However, **you may not use the material for commercial purposes**.

For details, see the [LICENSE](LICENSE) file or read more at [Creative Commons](https://creativecommons.org/licenses/by-nc/4.0/).


## Disclaimer

This repository is intended **only for educational and research purposes**. The authors and contributors assume no responsibility for misuse of the code or any implications arising from its use.


## Support My Projects

If you find this resource valuable and would like to help support my education and doctoral research, please consider treating me to a cup of coffee (or tea) via Revolut.

<div align="center">
  <a href="https://revolut.me/krmdznl" target="_blank">
    <img src="https://img.shields.io/badge/Support%20My%20Projects-Donate%20via%20Revolut-orange?style=for-the-badge" alt="Support my projects via Revolut" />
  </a>
</div> <br>
