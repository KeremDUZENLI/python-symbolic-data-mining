class CLI():
    def __init__(self, create_dataset, ALGORITHMS, run_algorithm, output_dataset, output_summary):
        self.create_dataset = create_dataset
        self.run_algorithm = run_algorithm
        self.output_dataset = output_dataset
        self.output_summary = output_summary
        
        self._generate_dataset()
        while True:
            prompt = input("\n[q] Quit  |  [r] Regenerate Dataset  |  [Enter] Run Algorithm  ").strip().lower()
            print()
                   
            if prompt == 'q':
                break
            elif prompt == 'r':
                self._generate_dataset()
            else:
                self._generate_result()


    def _generate_dataset(self):
        self.rows   = self._input_value("Number of Rows", maximum=10)
        columns     = self._input_value("Number of Columns", maximum=10)
        density     = self._input_value("Density", maximum=100)
        
        self.dataset, self.labels = self.create_dataset(self.rows, columns, density)
        
        lines = self.output_dataset(self.dataset, self.labels)
        print(*lines, sep='\n')


    def _generate_result(self):
        algorithm_choice    = self._input_value("1)Apriori  |  2)Apriori-Close  |  3)Eclat  |  4)Association_Rule", maximum=4)
        minimum_support     = self._input_value("Minimum Support", maximum=self.rows)
        minimum_confidence  = self._input_value("Minimum Confidence", minimum=1, maximum=100) if algorithm_choice == 4 else None
        
        all_frequent_itemsets, algorithm_name = self.run_algorithm(self.dataset, algorithm_choice, minimum_support, minimum_confidence)

        lines = self.output_summary(self.dataset, self.labels, minimum_support, minimum_confidence, algorithm_name, all_frequent_itemsets)
        print(*lines, sep='\n')


    def _input_value(self, message, minimum=1, maximum=None):
        range = f"({minimum} - {maximum})"  
        while True:
            
            try:
                value = int(input(f"{message} {range}: ").strip())
            except ValueError: 
                print("❌ ONLY INTEGER VALUE ❌")
                continue
            
            if (minimum is not None and value < minimum) or (maximum is not None and value > maximum):
                print(f"❌ NOT VALID RANGE ❌")
            else:
                return value
