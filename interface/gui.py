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
        
        self.label_minimum_support.config(text=f"Minimum Support ({self.rules['minimum_support'][0]} - {rows})")


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

        self.rows                     = tkinter.IntVar(value=self.rules['rows'][0])
        self.columns                  = tkinter.IntVar(value=self.rules['columns'][0])
        self.density                  = tkinter.IntVar(value=self.rules['density'][0])
        self.algorithm_choice         = tkinter.IntVar(value=self.rules['algorithm_choice'][0])
        self.minimum_support          = tkinter.IntVar(value=self.rules['minimum_support'][0])
        self.minimum_confidence       = tkinter.IntVar(value=self.rules['minimum_confidence'][0])

        label_rows                    = tkinter.Label(frame, text=f"Number of Rows ({self.rules['rows'][0]} - {self.rules['rows'][1]})", anchor='w', justify='left')            
        label_columns                 = tkinter.Label(frame, text=f"Number of Columns ({self.rules['columns'][0]} - {self.rules['columns'][1]})", anchor='w', justify='left')
        label_density                 = tkinter.Label(frame, text=f"Density ({self.rules['density'][0]} - {self.rules['density'][1]})", anchor='w', justify='left')             
        label_algorithm_choice        = tkinter.Label(frame, text=f"1)Apriori  |  2)Apriori-Close\n3)Eclat  |  4)Association_Rule", anchor='w', justify='left')        
        self.label_minimum_support    = tkinter.Label(frame, text=f"Minimum Support ({self.rules['minimum_support'][0]} - {self.rules['minimum_support'][1]})", anchor='w', justify='left')
        label_minimum_confidence      = tkinter.Label(frame, text=f"Minimum Confidence ({self.rules['minimum_confidence'][0]} - {self.rules['minimum_confidence'][1]})", anchor='w', justify='left')
                 
        entry_rows                    = tkinter.Entry(frame, textvariable=self.rows, validate='key')                                                                            
        entry_columns                 = tkinter.Entry(frame, textvariable=self.columns, validate='key')
        entry_density                 = tkinter.Entry(frame, textvariable=self.density, validate='key')                                                                        
        entry_algorithm_choice        = tkinter.Entry(frame, textvariable=self.algorithm_choice, validate='key')                                                                
        entry_minimum_support         = tkinter.Entry(frame, textvariable=self.minimum_support, validate='key')                                                                 
        entry_minimum_confidence      = tkinter.Entry(frame, textvariable=self.minimum_confidence, validate='key')    
        
        button_generate_dataset       = tkinter.Button(frame, text="Generate Dataset", command=self._generate_dataset)                                                          
        button_generate_result        = tkinter.Button(frame, text="Generate Result",  command=self._generate_result)                                                              
        button_generate_clean_output  = tkinter.Button(frame, text="Clean Output", command=self._generate_clean_output)                                                         
        button_generate_notes         = tkinter.Button(frame, text="Show Notes", command=self._generate_notes)     
                                                                     
        self.output                   = scrolledtext.ScrolledText(frame)

        label_rows                    .place(x=0,   y=0,    width=190, height=25)
        label_columns                 .place(x=0,   y=50,   width=190, height=25)
        label_density                 .place(x=0,   y=100,  width=190, height=25)
        label_algorithm_choice        .place(x=300, y=0,    width=190, height=25)
        self.label_minimum_support    .place(x=300, y=50,   width=190, height=25)
        label_minimum_confidence      .place(x=300, y=100,  width=190, height=25)
        
        entry_rows                    .place(x=200, y=0,    width=50,  height=25)
        entry_columns                 .place(x=200, y=50,   width=50,  height=25)
        entry_density                 .place(x=200, y=100,  width=50,  height=25)
        entry_algorithm_choice        .place(x=500, y=0,    width=50,  height=25)
        entry_minimum_support         .place(x=500, y=50,   width=50,  height=25)
        entry_minimum_confidence      .place(x=500, y=100,  width=50,  height=25)
                                   
        button_generate_dataset       .place(x=0,  y=150, width=250, height=25)
        button_generate_result        .place(x=300, y=150, width=250, height=25)
        button_generate_clean_output  .place(x=75, y=200, width=100, height=25)
        button_generate_notes         .place(x=375, y=200, width=100, height=25)

        self.output                   .place(x=0, y=250, width=550, height=300)
