class CLI():
    def __init__(self, create_dataset, run_algorithm, output_dataset, output_summary):
        self.create_dataset = create_dataset
        self.run_algorithm = run_algorithm
        self.output_dataset = output_dataset
        self.output_summary = output_summary
        
        self._generate_dataset()
        while True:
            self._generate_result()


    def _generate_dataset(self):
        self.rows = self._prompt("Number of Rows", maximum=10)
        columns = self._prompt("Number of Columns", maximum=10)
        density = self._prompt("Density", maximum=100)
        self.dataset, self.labels = self.create_dataset(self.rows, columns, density)
        
        lines = self.output_dataset(self.dataset, self.labels)
        print(*lines, sep='\n')


    def _generate_result(self):
        minimum_support = self._prompt("Minimum Support", maximum=self.rows)
        algorithm_choice = self._prompt("1)Apriori  |  2)Apriori-Close  |  3)Eclat", maximum=3)
        frequent_itemsets = self.run_algorithm(self.dataset, minimum_support, algorithm_choice)

        lines = self.output_summary(self.dataset, self.labels, minimum_support, algorithm_choice, frequent_itemsets)
        print(*lines, sep='\n')


    def _prompt(self, message, minimum=1, maximum=None):
        range = f"({minimum} - {maximum})"  
        while True:
            value = int(input(f"{message} {range}: ").strip())
            if (minimum is not None and value < minimum) or (maximum is not None and value > maximum):
                print(f"❌ NOT VALID RANGE ❌")
            else:
                return value
