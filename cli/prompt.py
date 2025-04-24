class PROMPT():
    def __init__(self, generate_dataset, run_algorithm, output_summary, algorithms):
        self.generate_dataset = generate_dataset
        self.run_algorithm = run_algorithm
        self.output_summary = output_summary
        
        self.algorithms = algorithms
        
        self._run_prompt()
    
    def _run_prompt(self):
        rows = self._prompt("Number of Rows", maximum=10)
        columns = self._prompt("Number of Columns", maximum=10)
        density = self._prompt("Density", maximum=100)
        dataset, labels = self.generate_dataset(rows, columns, density)

        minimum_support = self._prompt("Minimum Support", maximum=rows)
        algorithm_choice = self._prompt(f"Select algorithm {self.algorithms}", minimum=1, maximum=3)
        frequent_itemsets = self.run_algorithm(dataset, minimum_support, self.algorithms[algorithm_choice])
        
        lines = self.output_summary(dataset, labels, minimum_support, algorithm_choice, frequent_itemsets)
        print(*lines, sep='\n')


    def _prompt(self, message, minimum=1, maximum=None):
        range = f"({minimum} - {maximum})"  
        while True:
            value = int(input(f"{message} {range}: ").strip())
            if (minimum is not None and value < minimum) or (maximum is not None and value > maximum):
                print(f"❌ Valid Range = {range}")
            else:
                return value
