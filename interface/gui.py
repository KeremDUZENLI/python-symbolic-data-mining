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
            "rows"               : (5, 10),
            "columns"            : (5, 10),
            "density"            : (50, 100),
            "minimum_support"    : None,
            "minimum_confidence" : (1, 100),
            "algorithm_choice"   : (1, 4),
        }
        self.rules["minimum_support"] = 1, self.rules["rows"][1]
        
        self._build_gui()
        self.mainloop()


    def _generate_dataset(self):        
        rows    = self._input_value(self.rows,      "rows")
        columns = self._input_value(self.columns,   "columns")
        density = self._input_value(self.density,   "density")
        
        self.dataset, self.labels = self.create_dataset(rows, columns, density)
        
        lines = self.output_dataset(self.dataset, self.labels)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)
        
        self.minimum_support_dynamic_label.config(text=f"Minimum Support ({self.rules['minimum_support'][0]} - {rows})")


    def _generate_result(self):
        algorithm_choice    = self._input_value(self.algorithm_choice,   "algorithm_choice")
        minimum_support     = self._input_value(self.minimum_support,    "minimum_support")
        minimum_confidence  = self._input_value(self.minimum_confidence, "minimum_confidence")
        
        all_frequent_itemsets = self.run_algorithm(self.dataset, minimum_support, minimum_confidence, algorithm_choice)
        
        lines = self.output_summary(self.dataset, self.labels, minimum_support, minimum_confidence, algorithm_choice, all_frequent_itemsets)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)


    def _generate_clean_output(self):
        self.output.delete('1.0', tkinter.END)


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
        frame = tkinter.Frame(self, width=600, height=600)
        frame.place(x=25, y=25)
        
        self.geometry("600x600")
        self.title("Symbolic Data Mining")
        self.rows               = tkinter.IntVar(value=self.rules['rows'][0])
        self.columns            = tkinter.IntVar(value=self.rules['columns'][0])
        self.density            = tkinter.IntVar(value=self.rules['density'][0])
        self.minimum_support    = tkinter.IntVar(value=self.rules['minimum_support'][0])
        self.minimum_confidence = tkinter.IntVar(value=self.rules['minimum_confidence'][0])
        self.algorithm_choice   = tkinter.IntVar(value=self.rules['algorithm_choice'][0])

        tkinter.Label(frame, text=f"Number of Rows ({self.rules['rows'][0]} - {self.rules['rows'][1]})")            .place(x=0, y=0, width=190, height=25)
        tkinter.Entry(frame, textvariable=self.rows, width=5, validate='key')                                       .place(x=200, y=0, width=50, height=25)

        tkinter.Label(frame, text=f"Number of Columns ({self.rules['columns'][0]} - {self.rules['columns'][1]})")   .place(x=0, y=50, width=190, height=25)
        tkinter.Entry(frame, textvariable=self.columns, width=5, validate='key')                                    .place(x=200, y=50, width=50, height=25)

        tkinter.Label(frame, text=f"Density ({self.rules['density'][0]} - {self.rules['density'][1]})")             .place(x=0, y=100, width=190, height=25)
        tkinter.Entry(frame, textvariable=self.density, width=5, validate='key')                                    .place(x=200, y=100, width=50, height=25)


        tkinter.Label(frame, text=f"1)Apriori  |  2)Apriori-Close\n3)Eclat  |  4)Association_Rule")                 .place(x=300, y=0, width=190, height=25)
        tkinter.Entry(frame, textvariable=self.algorithm_choice, width=5, validate='key')                           .place(x=500, y=0, width=50, height=25)

        self.minimum_support_dynamic_label = tkinter.Label(frame, text=f"Minimum Support ({self.rules['minimum_support'][0]} - {self.rules['minimum_support'][1]})")
        self.minimum_support_dynamic_label                                                                          .place(x=300, y=50, width=190, height=25)
        tkinter.Entry(frame, textvariable=self.minimum_support, width=5, validate='key')                            .place(x=500, y=50, width=50, height=25)

        self.minimum_confidence_label = tkinter.Label(frame, text=f"Minimum Confidence ({self.rules['minimum_confidence'][0]} - {self.rules['minimum_confidence'][1]})")
        self.minimum_confidence_label                                                                               .place(x=300, y=100, width=190, height=25)
        tkinter.Entry(frame, textvariable=self.minimum_confidence, width=5, validate='key')                         .place(x=500, y=100, width=50, height=25)


        tkinter.Button(frame, text="Generate Dataset", command=self._generate_dataset)                              .place(x=0,  y=150, width=250, height=25)
        tkinter.Button(frame, text="Generate Result", command=self._generate_result)                                .place(x=300, y=150, width=250, height=25)
        
        tkinter.Button(frame, text="Clean Output", command=self._generate_clean_output)                             .place(x=75, y=200, width=100, height=25)
        tkinter.Button(frame, text="Show Notes", command=self._generate_notes)                                      .place(x=375, y=200, width=100, height=25)

        self.output = scrolledtext.ScrolledText(frame)
        self.output.place(x=0, y=250, width=550, height=300)
