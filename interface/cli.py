from helper import welcome_message


class CLI():
    def __init__(self, create_dataset, create_dataset_default, ALGORITHMS, run_algorithm, output_dataset, output_summary):
        self.create_dataset         = create_dataset
        self.create_dataset_default = create_dataset_default
        self.algorithms             = ALGORITHMS
        self.run_algorithm          = run_algorithm
        self.output_dataset         = output_dataset
        self.output_summary         = output_summary
        
        self.algorithm_names = [f"{key}) {function.__name__}" for key, function in sorted(self.algorithms.items())]
        self.dataset = None

        lines = welcome_message()
        print(*lines, sep='\n')
        while True:
            prompt = input("\n[r] Generate Dataset  |  [d] Laszlo.rcf  |  [Enter] Run Algorithm  |  [q] Quit  :  ").strip().lower()
                   
            if   prompt == 'r':
                self._generate_dataset()
            elif prompt == 'd':
                self._dataset_default()
            elif prompt == '':                
                self._generate_result()
            elif prompt == 'q':
                break
            else:
                print("!!! WRONG INPUT !!!")


    def _generate_dataset(self):
        print("\n_____INPUT DATASET VALUES_____\n")
        
        self.rows   = self._input_value("Number of Rows", maximum=10)
        columns     = self._input_value("Number of Columns", maximum=10)
        density     = self._input_value("Density", maximum=100)
        
        self.dataset, self.labels = self.create_dataset(self.rows, columns, density)
        
        lines = self.output_dataset(self.dataset, self.labels)
        print(*lines, sep='\n')


    def _dataset_default(self):
        self.dataset, self.labels = self.create_dataset_default()
    
        self.rows    = len(self.dataset)
        
        lines = self.output_dataset(self.dataset, self.labels)
        print(*lines, sep='\n')


    def _generate_result(self):
        if self.dataset is None:
            print("!!! DATASET NOT DEFINED !!!")
            return
        print("\n_____INPUT ALGORITHM VALUES_____\n")
        
        algorithm_choice    = self._input_value("  ".join(self.algorithm_names), maximum=len(self.algorithm_names))
        minimum_support     = self._input_value("Minimum Support", maximum=self.rows)
        minimum_confidence  = self._input_value("Minimum Confidence", minimum=1, maximum=100) if algorithm_choice == 5 else None
        
        all_frequent_itemsets, algorithm_name = self.run_algorithm(self.dataset, algorithm_choice, minimum_support, minimum_confidence)

        lines = self.output_summary(self.dataset, self.labels, minimum_support, minimum_confidence, algorithm_name, all_frequent_itemsets)
        print(*lines, sep='\n')


    def _input_value(self, message, minimum=1, maximum=None):
        range = f"({minimum} - {maximum})"  
        while True:
            
            try:
                value = int(input(f"{message} {range}: ").strip())
            except ValueError: 
                print("!!! ONLY INTEGER VALUE !!!")
                continue
            
            if (minimum is not None and value < minimum) or (maximum is not None and value > maximum):
                print("!!! NOT VALID RANGE !!!")
            else:
                return value
