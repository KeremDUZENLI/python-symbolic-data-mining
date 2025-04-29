import tkinter
from tkinter import scrolledtext


class GUI(tkinter.Tk):    
    def __init__(self, create_dataset, run_algorithm, output_dataset, output_summary):       
        self.create_dataset = create_dataset
        self.run_algorithm = run_algorithm
        self.output_dataset = output_dataset
        self.output_summary = output_summary
        super().__init__()

        self.rules = {
            "rows"              : (1, 10),
            "columns"           : (1, 10),
            "density"           : (1, 100),
            "minimum_support"   : None,
            "confidence"        : (1, 10),
            "algorithm_choice"  : (1, 3),
        }
        self.rules["minimum_support"] = self.rules["rows"][0], self.rules["rows"][1]
        
        self._build_gui()
        self.mainloop()


    def _generate_dataset(self):
        self.output.delete('1.0', tkinter.END)
        
        rows    = self._input_value(self.rows,      "rows")
        columns = self._input_value(self.columns,   "columns")
        density = self._input_value(self.density,   "density")
        self.dataset, self.labels = self.create_dataset(rows, columns, density)
        
        lines = self.output_dataset(self.dataset, self.labels)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)
        
        self.minimum_support_dynamic_label.config(text=f"Minimum Support ({self.rules['minimum_support'][0]} - {rows})")


    def _generate_result(self):
        minimum_support  = self._input_value(self.minimum_support,  "minimum_support")
        algorithm_choice = self._input_value(self.algorithm_choice, "algorithm_choice")
        frequent_itemsets = self.run_algorithm(self.dataset, minimum_support, algorithm_choice)
        
        lines = self.output_summary(self.dataset, self.labels, minimum_support, algorithm_choice, frequent_itemsets)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)
        
        
    def _generate_notes(self):
        pdf = self.tk.call('file', 'normalize', 'notes/Notes.pdf')
        system = self.tk.call('tk', 'windowingsystem')

        if system == 'win32':
            self.tk.call('exec', 'cmd', '/c', 'start', '', pdf)
        elif system == 'aqua':
            self.tk.call('exec', 'open', pdf)
        else:
            self.tk.call('exec', 'xdg-open', pdf)
        
    
    def _input_value(self, value, label_name):      
        minimum, maximum = self.rules.get(label_name, (None, None))
        maximum = self.rows.get() if label_name == "minimum_support" else maximum
  
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
        self.rows             = tkinter.IntVar(value=self.rules['rows'][0])
        self.columns          = tkinter.IntVar(value=self.rules['columns'][0])
        self.density          = tkinter.IntVar(value=self.rules['density'][0])
        self.minimum_support  = tkinter.IntVar(value=self.rules['minimum_support'][0])
        self.algorithm_choice = tkinter.IntVar(value=self.rules['algorithm_choice'][0])

        self.minimum_support_dynamic_label = tkinter.Label(frame, text=f"Minimum Support ({self.rules['minimum_support'][0]} - {self.rules['minimum_support'][1]})")
        
        tkinter.Label(frame, text=f"Number of Rows ({self.rules['rows'][0]} - {self.rules['rows'][1]})")            .grid(row=0, column=0, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.rows, width=5, validate='key')                                       .grid(row=0, column=1, sticky="w", padx=2, pady=2)

        tkinter.Label(frame, text=f"Number of Columns ({self.rules['columns'][0]} - {self.rules['columns'][1]})")   .grid(row=1, column=0, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.columns, width=5, validate='key')                                    .grid(row=1, column=1, sticky="w", padx=2, pady=2)

        tkinter.Label(frame, text=f"Density ({self.rules['density'][0]} - {self.rules['density'][1]})")             .grid(row=2, column=0, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.density, width=5, validate='key')                                    .grid(row=2, column=1, sticky="w", padx=2, pady=2)
        
        self.minimum_support_dynamic_label                                                                          .grid(row=0, column=5, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.minimum_support, width=5, validate='key')                            .grid(row=0, column=6, sticky="w", padx=2, pady=2)
        
        tkinter.Label(frame, text=f"Confidence ({self.rules['confidence'][0]} - {self.rules['confidence'][1]})")    .grid(row=1, column=5, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=None, width=5, validate='key')                                            .grid(row=1, column=6, sticky="w", padx=2, pady=2)
        
        tkinter.Label(frame, text=f"1)Apriori | 2)Apriori-Close | 3)Eclat ")                                        .grid(row=2, column=5, sticky="w", padx=2, pady=2)
        tkinter.Entry(frame, textvariable=self.algorithm_choice, width=5, validate='key')                           .grid(row=2, column=6, sticky="w", padx=2, pady=2)

        tkinter.Button(frame, text="Generate Dataset", command=self._generate_dataset)                              .grid(row=3, column=0, sticky="w", padx=2, pady=2)
        tkinter.Button(frame, text="Generate Result", command=self._generate_result)                                .grid(row=3, column=4, sticky="w", padx=2, pady=2)
        tkinter.Button(frame, text="Show Notes", command=self._generate_notes)                                      .grid(row=3, column=7, sticky="w", padx=2, pady=2)
        
        self.output = scrolledtext.ScrolledText(self, width=80, height=20)
        self.output.pack(fill='both', expand=True, padx=5, pady=5)
