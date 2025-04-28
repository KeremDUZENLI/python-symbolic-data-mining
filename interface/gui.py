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
        self.mainloop()


    def _generate_dataset(self):
        self.output.delete('1.0', tkinter.END)
        
        rows    = self._input_value(self.rows,      1, 10)
        columns = self._input_value(self.columns,   1, 10)
        density = self._input_value(self.density,   1, 100)
        self.dataset, self.labels = self.create_dataset(rows, columns, density)
        
        lines = self.output_dataset(self.dataset, self.labels)
        self._print_result(lines)


    def _generate_result(self):
        minimum_support  = self._input_value(self.minimum_support, 1, self.rows.get())
        algorithm_choice = self._input_value(self.algorithm_choice, 1, 3)
        frequent_itemsets = self.run_algorithm(self.dataset, minimum_support, algorithm_choice)
        
        lines = self.output_summary(self.dataset, self.labels, minimum_support, algorithm_choice, frequent_itemsets)
        self._print_result(lines)
        
    
    def _input_value(self, value, minimum=1, maximum=None):            
        try:
            value_int = int(value.get())
        except:
            value_int = minimum
        
        if (minimum is not None and value_int < minimum):
            value_int = minimum
        if (maximum is not None and value_int > maximum):
            value_int = maximum
        
        value.set(value_int)
        return value_int


    def _build_gui(self):
        frame = tkinter.Frame(self)
        frame.pack(padx=5, pady=5, anchor="w")
        
        self.title("Symbolic Data Mining")
        self.rows             = tkinter.IntVar()
        self.columns          = tkinter.IntVar()
        self.density          = tkinter.IntVar()
        self.minimum_support  = tkinter.IntVar()
        self.algorithm_choice = tkinter.IntVar()

        tkinter.Label(frame, text="Number of Rows")                                         .grid(row=0, column=0, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.rows, width=5, validate='key')               .grid(row=0, column=1, sticky="w", padx=2, pady=2)
        
        tkinter.Label(frame, text="Number of Columns")                                      .grid(row=1, column=0, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.columns, width=5, validate='key')            .grid(row=1, column=1, sticky="w", padx=2, pady=2)
        
        tkinter.Label(frame, text="Density")                                                .grid(row=2, column=0, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.density, width=5, validate='key')            .grid(row=2, column=1, sticky="w", padx=2, pady=2)
        
        tkinter.Label(frame, text="Minimum Support")                                        .grid(row=0, column=5, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.minimum_support, width=5, validate='key')    .grid(row=0, column=6, sticky="w", padx=2, pady=2)
        
        tkinter.Label(frame, text="Confidence")                                             .grid(row=1, column=5, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=None, width=5, validate='key')                    .grid(row=1, column=6, sticky="w", padx=2, pady=2)
        
        tkinter.Label(frame, text="1)Apriori  |  2)Apriori-Close  |  3)Eclat")              .grid(row=2, column=5, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.algorithm_choice, width=5, validate='key')   .grid(row=2, column=6, sticky="w", padx=2, pady=2)

        tkinter.Button(frame, text="Generate Dataset", command=self._generate_dataset)      .grid(row=3, column=0, sticky="w", padx=2, pady=2)
        tkinter.Button(frame, text="Generate Result", command=self._generate_result)        .grid(row=3, column=4, sticky="w", padx=2, pady=2)
        tkinter.Button(frame, text="Show Notes", command=self._show_notes)                  .grid(row=3, column=7, sticky="w", padx=2, pady=2)
        
        self.output = scrolledtext.ScrolledText(self, width=80, height=20)
        self.output.pack(fill='both', expand=True, padx=5, pady=5)
    
    
    def _print_result(self, lines):
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
