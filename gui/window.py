import tkinter
from tkinter import scrolledtext


class GUI(tkinter.Tk):    
    def __init__(self, generate_dataset, run_algorithm, output_summary):       
        self.generate_dataset = generate_dataset
        self.run_algorithm = run_algorithm
        self.output_summary = output_summary
        
        super().__init__()

        self._build_gui()
        self._run_gui()
        self.mainloop()

    def _run_gui(self):
        self.output.delete('1.0', tkinter.END)
        
        rows = self.rows.get()
        columns = self.columns.get()
        density = self.density.get()
        dataset, labels = self.generate_dataset(rows, columns, density)
        
        minimum_support = self.minimum_support.get()
        algorithm_choice = self.algorithm_choice.get()
        frequent_itemsets = self.run_algorithm(dataset, minimum_support, algorithm_choice)
        
        lines = self.output_summary(dataset, labels, minimum_support, algorithm_choice, frequent_itemsets)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)

    def _build_gui(self):
        self.title("Symbolic Data Mining")
        
        self.rows = tkinter.IntVar(value=5)
        self.columns = tkinter.IntVar(value=5)
        self.density = tkinter.IntVar(value=50)
        self.minimum_support = tkinter.IntVar(value=2)
        self.algorithm_choice = tkinter.IntVar(value=1)

        frame = tkinter.Frame(self)
        frame.pack(padx=5, pady=5, anchor="w")
        fields = [
                    ("Number of Rows",    self.rows),
                    ("Number of Columns", self.columns),
                    ("Density", self.density),
                    ("Minimum Support", self.minimum_support),
                    ("1)Apriori  |  2)Apriori-Close  |  3)Eclat", self.algorithm_choice),
                ]      
        
        # Lay out each field on its own row
        for row_id, (label, value) in enumerate(fields):
            tkinter.Label(frame, text=label).grid(row=row_id, column=0, sticky="w", padx=2, pady=2)
            tkinter.Entry(frame, textvariable=value, width=5).grid(row=row_id, column=1, padx=2, pady=2)

        # Run button on the next row
        run_row = len(fields)
        tkinter.Button(frame, text="Run", command=self._run_gui).grid(row=run_row, column=0, columnspan=2, pady=(10,2))

        # Output area
        self.output = scrolledtext.ScrolledText(self, width=80, height=20)
        self.output.pack(fill='both', expand=True, padx=5, pady=5)
