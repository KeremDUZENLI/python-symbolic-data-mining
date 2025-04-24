import tkinter
from tkinter import scrolledtext


class GUI(tkinter.Tk):    
    def __init__(self, generate_dataset, run_algorithm, output_summary, algorithms):
        super().__init__()
        self.title("Symbolic Data Mining")
        
        self.generate_dataset = generate_dataset
        self.run_algorithm = run_algorithm
        self.output_summary = output_summary
        
        self.algorithms = algorithms
        
        # State
        self.rows = tkinter.IntVar(value=5)
        self.columns = tkinter.IntVar(value=5)
        self.density = tkinter.IntVar(value=50)
        self.minimum_support = tkinter.IntVar(value=2)
        self.algorithm_choice = tkinter.IntVar(value=1)

        # Input controls
        frame = tkinter.Frame(self)
        frame.pack(padx=5, pady=5)
        fields = [
                    ("Number of Rows",    self.rows),
                    ("Number of Columns", self.columns),
                    ("Density", self.density),
                    ("Minimum Support", self.minimum_support),
                    (f"Select algorithm {self.algorithms}", self.algorithm_choice),
                ]
        
        for i, (name, value) in enumerate(fields):
            tkinter.Label(frame, text=name).grid(row=0, column=i*2, padx=2)
            tkinter.Entry(frame, textvariable=value, width=5).grid(row=0, column=i*2+1)
        
        tkinter.Button(frame, text="Run", command=self._run_gui).grid(row=0, column=len(fields)*2, padx=5)

        # Output area
        self.output = scrolledtext.ScrolledText(self, width=80, height=20)
        self.output.pack(fill='both', expand=True, padx=5, pady=5)

        # Initial display
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
        frequent_itemsets = self.run_algorithm(dataset, minimum_support, self.algorithms[algorithm_choice])
        
        lines = self.output_summary(dataset, labels, minimum_support, self.algorithms[algorithm_choice], frequent_itemsets)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)
