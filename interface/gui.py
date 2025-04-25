import tkinter
from tkinter import scrolledtext


class GUI(tkinter.Tk):    
    def __init__(self, create_dataset, run_algorithm, output_summary):       
        self.create_dataset = create_dataset
        self.run_algorithm = run_algorithm
        self.output_summary = output_summary
        
        super().__init__()

        self._build_gui()
        self._generate_dataset()
        self._generate_result()
        self.mainloop()


    def _build_gui(self):
        self.title("Symbolic Data Mining")
        
        self.rows = tkinter.IntVar(value=5)
        self.columns = tkinter.IntVar(value=5)
        self.density = tkinter.IntVar(value=50)
        self.minimum_support = tkinter.IntVar(value=2)
        self.algorithm_choice = tkinter.IntVar(value=1)

        frame = tkinter.Frame(self)
        frame.pack(padx=5, pady=5, anchor="w")

        left = tkinter.Frame(frame)
        right = tkinter.Frame(frame)
        left.grid(row=0, column=0, padx=(0,20))
        right.grid(row=0, column=1)

        dataset_field = [
            ("Number of Rows",    self.rows),
            ("Number of Columns", self.columns),
            ("Density",           self.density),
        ]
        for r, (lbl, var) in enumerate(dataset_field):
            tkinter.Label(left, text=lbl).grid(row=r, column=0, sticky="w", padx=2, pady=2)
            tkinter.Entry(left, textvariable=var, width=5).grid(row=r, column=1, padx=2, pady=2)
        tkinter.Button(left, text="Create Dataset", command=self._generate_dataset) \
               .grid(row=len(dataset_field), column=0, columnspan=2, pady=(10,2))

        algorithm_field = [
            ("Minimum Support", self.minimum_support),
            ("1)Apriori  |  2)Apriori-Close  |  3)Eclat", self.algorithm_choice),
            ("", None),
        ]
        for r, (lbl, var) in enumerate(algorithm_field):
            tkinter.Label(right, text=lbl).grid(row=r, column=0, sticky="w", padx=2, pady=2)
            tkinter.Entry(right, textvariable=var, width=5).grid(row=r, column=1, padx=2, pady=2)
        tkinter.Button(right, text="Run Algorithm", command=self._generate_result) \
               .grid(row=len(algorithm_field), column=0, columnspan=2, pady=(10,2))
               
        tkinter.Button(right, text="Show Notes", command=self._show_notes) \
                .grid(row=len(algorithm_field), column=2, columnspan=2, pady=(10,2))

        self.output = scrolledtext.ScrolledText(self, width=80, height=20)
        self.output.pack(fill='both', expand=True, padx=5, pady=5)


    def _generate_dataset(self):
        self.output.delete('1.0', tkinter.END)
        
        rows = self.rows.get()
        columns = self.columns.get()
        density = self.density.get()
        self.dataset, self.labels = self.create_dataset(rows, columns, density)
        
        lines = self.output_summary(self.dataset, self.labels, minimum_support=0, algorithm_choice=0, frequent_itemsets={})
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)


    def _generate_result(self):
        self.output.delete('1.0', tkinter.END)
        
        minimum_support = self.minimum_support.get()
        algorithm_choice = self.algorithm_choice.get()
        frequent_itemsets = self.run_algorithm(self.dataset, minimum_support, algorithm_choice)
        
        lines = self.output_summary(self.dataset, self.labels, minimum_support, algorithm_choice, frequent_itemsets)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)          


    def _show_notes(self):
        pdf = self.tk.call('file', 'normalize', 'notes/Notes.pdf')
        system = self.tk.call('tk', 'windowingsystem')

        if system == 'win32':
            self.tk.call('exec', 'cmd', '/c', 'start', '', pdf)
        elif system == 'aqua':
            self.tk.call('exec', 'open', pdf)
        else:
            self.tk.call('exec', 'xdg-open', pdf)
