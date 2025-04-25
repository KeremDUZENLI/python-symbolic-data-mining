import tkinter
from tkinter import scrolledtext


class GUI(tkinter.Tk):    
    def __init__(self, create_dataset, run_algorithm, output_dataset, output_summary):       
        self.create_dataset = create_dataset
        self.run_algorithm = run_algorithm
        self.output_dataset = output_dataset
        self.output_summary = output_summary
        
        super().__init__()
        self._build_gui()
        self._generate_dataset()
        self._generate_result()
        self.mainloop()


    def _generate_dataset(self):
        self.output.delete('1.0', tkinter.END)
        
        rows = self.rows.get()
        columns = self.columns.get()
        density = self.density.get()
        self.dataset, self.labels = self.create_dataset(rows, columns, density)
        
        lines = self.output_dataset(self.dataset, self.labels)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)


    def _generate_result(self):       
        minimum_support = self.minimum_support.get()
        algorithm_choice = self.algorithm_choice.get()
        frequent_itemsets = self.run_algorithm(self.dataset, minimum_support, algorithm_choice)
        
        lines = self.output_summary(self.dataset, self.labels, minimum_support, algorithm_choice, frequent_itemsets)
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
        left  = tkinter.Frame(frame); left.grid(row=0, column=0, padx=(0,20))
        right = tkinter.Frame(frame); right.grid(row=0, column=1, padx=(0,20))

        dataset_fields = [
            ("Number of Rows",    self.rows,    1, 10),
            ("Number of Columns", self.columns, 1, 10),
            ("Density",           self.density, 1, 100),
        ]
        algorithm_fields = [
            ("Minimum Support",                             self.minimum_support,   1, self.rows.get()),
            ("1)Apriori  |  2)Apriori-Close  |  3)Eclat",   self.algorithm_choice,  1, 3),
            ("Confidence",                                  None,                   0, 0),
        ]
        
        for row, parameters in enumerate(dataset_fields):
            self._add_field(left, row, *parameters)
        tkinter.Button(left, text="Create Dataset", command=self._generate_dataset).grid(row=len(dataset_fields), column=0, columnspan=2, pady=(10,2))

        for row, parameters in enumerate(algorithm_fields):
            self._add_field(right, row, *parameters)
        tkinter.Button(right, text="Run Algorithm", command=self._generate_result).grid(row=len(algorithm_fields), column=0, columnspan=2, pady=(10,2))

        tkinter.Button(right, text="Show Notes", command=self._show_notes).grid(row=len(algorithm_fields), column=2, columnspan=2, pady=(10,2))

        self.output = scrolledtext.ScrolledText(self, width=80, height=20)
        self.output.pack(fill='both', expand=True, padx=5, pady=5)


    def _add_field(self, position, row, label, value, minimum, maximum):
        tkinter.Label(position, text=label).grid(row=row, column=0, sticky="w", padx=2, pady=2)
        validator = (self.register(lambda P, lo=minimum, hi=maximum: self._validate(P, lo, hi)), '%P')
        tkinter.Entry(position, textvariable=value, width=5, validate='key', validatecommand=validator).grid(row=row, column=1, padx=2, pady=2)


    def _validate(self, proposed: str, minimum: int, maximum: int) -> bool:
        return proposed == "" or (proposed.isdigit() and minimum <= int(proposed) <= maximum)


    def _show_notes(self):
        pdf = self.tk.call('file', 'normalize', 'notes/Notes.pdf')
        system = self.tk.call('tk', 'windowingsystem')

        if system == 'win32':
            self.tk.call('exec', 'cmd', '/c', 'start', '', pdf)
        elif system == 'aqua':
            self.tk.call('exec', 'open', pdf)
        else:
            self.tk.call('exec', 'xdg-open', pdf)
