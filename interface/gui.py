import tkinter
from tkinter import scrolledtext

from helper import create_column_labels, open_pdf, open_url, welcome_message


class GUI(tkinter.Tk):    
    def __init__(self, create_dataset, create_dataset_default, create_dataset_from_grid, ALGORITHMS, run_algorithm, output_dataset, output_summary):       
        self.create_dataset           = create_dataset
        self.create_dataset_default   = create_dataset_default
        self.create_dataset_from_grid = create_dataset_from_grid
        self.algorithms               = ALGORITHMS
        self.run_algorithm            = run_algorithm
        self.output_dataset           = output_dataset
        self.output_summary           = output_summary

        self.rules = {
            "rows"               : (1, 10),
            "columns"            : (1, 10),
            "density"            : (0, 100),
            "minimum_support"    : None,
            "minimum_confidence" : (0, 100),
        }
        self.rules["minimum_support"] = 1, self.rules["rows"][1]

        self.algorithm_names          = [ self.algorithms[key].__name__ for key in sorted(self.algorithms.keys()) ]
        self.algorithm_names2keys     = { function.__name__: key for key, function in self.algorithms.items() }
        self.dataset = None

        super().__init__()
        self._build_gui()
        self.mainloop()


    def _build_gui(self):       
        frame = tkinter.Frame(self, width=600, height=600)
        frame.place(x=25, y=25)
        
        self.geometry("600x600")
        self.title("Symbolic Data Mining")

        self.rows                     = tkinter.IntVar(value=5)
        self.columns                  = tkinter.IntVar(value=5)
        self.density                  = tkinter.IntVar(value=0)
        self.algorithm_choice         = tkinter.StringVar(value=self.algorithm_names[0])
        self.minimum_support          = tkinter.IntVar(value=3)
        self.minimum_confidence       = tkinter.IntVar(value=0)
        
        label_rows                    = tkinter.Label(frame, text=f"Number of Rows ({self.rules['rows'][0]} - {self.rules['rows'][1]})", anchor='w', justify='left')            
        label_columns                 = tkinter.Label(frame, text=f"Number of Columns ({self.rules['columns'][0]} - {self.rules['columns'][1]})", anchor='w', justify='left')
        label_density                 = tkinter.Label(frame, text=f"Density ({self.rules['density'][0]} - {self.rules['density'][1]})", anchor='w', justify='left')             
        label_algorithm_choice        = tkinter.Label(frame, text=f"Algorithm", anchor='w', justify='left')        
        self.label_minimum_support    = tkinter.Label(frame, text=f"Minimum Support ({self.rules['minimum_support'][0]} - {self.rules['minimum_support'][1]})", anchor='w', justify='left')
        label_minimum_confidence      = tkinter.Label(frame, text=f"Minimum Confidence ({self.rules['minimum_confidence'][0]} - {self.rules['minimum_confidence'][1]})", anchor='w', justify='left')
        
        entry_rows                    = tkinter.Entry(frame, textvariable=self.rows,               validate='key')                                                                            
        entry_columns                 = tkinter.Entry(frame, textvariable=self.columns,            validate='key')
        entry_density                 = tkinter.Entry(frame, textvariable=self.density,            validate='key')                                                             
        entry_algorithm_choice        = tkinter.OptionMenu(frame, self.algorithm_choice, *self.algorithm_names)
        entry_minimum_support         = tkinter.Entry(frame, textvariable=self.minimum_support,    validate='key')                                                                 
        self.entry_minimum_confidence = tkinter.Entry(frame, textvariable=self.minimum_confidence, validate='key')
        
        button_generate_dataset       = tkinter.Button(frame, text="Generate Dataset", command=self._generate_dataset)
        button_dataset_default        = tkinter.Button(frame, text="Default Dataset",  command=self._dataset_default)
        button_draw_dataset           = tkinter.Button(frame, text="Draw Dataset",     command=self._draw_dataset)
        button_clear_output           = tkinter.Button(frame, text="Clear Output",     command=self._clear_output)
        button_show_notes             = tkinter.Button(frame, text="Show Notes",       command=lambda: open_pdf("notes/Notes_Kerem.pdf"))
        button_generate_result        = tkinter.Button(frame, text="Generate Result",  command=self._generate_result)
        
        label_footer                  = tkinter.Label (self, text="Developed by Kerem Düzenli", fg="gray")
        button_repository             = tkinter.Button(self, text="Repository", command=lambda: open_url("https://github.com/KeremDUZENLI/python-symbolic-data-mining"))
        button_donate                 = tkinter.Button(self, text="Support"   , command=lambda: open_url("https://revolut.me/krmdznl"))
        
        self.output                   = scrolledtext.ScrolledText(frame, wrap=tkinter.NONE)
        x_scroll                      = tkinter.Scrollbar(frame, orient='horizontal', command=self.output.xview)
        
        label_rows                    .place(x=0,    y=0,    width=190, height=25)
        label_columns                 .place(x=0,    y=50,   width=190, height=25)
        label_density                 .place(x=0,    y=100,  width=190, height=25)
        label_algorithm_choice        .place(x=300,  y=0,    width=90,  height=25)
        self.label_minimum_support    .place(x=300,  y=50,   width=190, height=25)
        label_minimum_confidence      .place(x=300,  y=100,  width=190, height=25)

        entry_rows                    .place(x=200,  y=0,    width=50,  height=25)
        entry_columns                 .place(x=200,  y=50,   width=50,  height=25)
        entry_density                 .place(x=200,  y=100,  width=50,  height=25)
        entry_algorithm_choice        .place(x=400,  y=0,    width=150, height=25)
        entry_minimum_support         .place(x=500,  y=50,   width=50,  height=25)
        self.entry_minimum_confidence .place(x=500,  y=100,  width=50,  height=25)

        button_generate_dataset       .place(x=0,    y=150,  width=110, height=25)
        button_dataset_default        .place(x=140,  y=150,  width=110, height=25)
        button_draw_dataset           .place(x=0,    y=200,  width=250, height=25)
        button_clear_output           .place(x=300,  y=150,  width=110, height=25)
        button_show_notes             .place(x=440,  y=150,  width=110, height=25)
        button_generate_result        .place(x=300,  y=200,  width=250, height=25)
        
        label_footer                  .place(x=200, y=577.5, width=200, height=20)
        button_repository             .place(x=100, y=577.5, width=100, height=20)
        button_donate                 .place(x=400, y=577.5, width=100, height=20)

        self.output                   .place(x=0,    y=250,  width=550, height=300)
        x_scroll                      .place(x=0,    y=530,  width=550)
        
        lines = welcome_message()
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)

        self.entry_minimum_confidence .config(state="disabled")
        self.algorithm_choice         .trace_add("write", lambda *args: self.entry_minimum_confidence.config(state="normal" if self.algorithm_choice.get() == "association_rule" else "disabled"))
        self.output                   .config(xscrollcommand=x_scroll.set)


    def _generate_dataset(self):        
        rows    = self._input_value(self.rows,    "rows")
        columns = self._input_value(self.columns, "columns")
        density = self._input_value(self.density, "density")
        
        self.dataset, self.labels = self.create_dataset(rows, columns, density)
        self._show_dataset()
        
        self.label_minimum_support.config(text=f"Minimum Support ({self.rules['minimum_support'][0]} - {rows})")


    def _dataset_default(self):
        self.dataset, self.labels = self.create_dataset_default()
        self._show_dataset()
        
        number_rows    = len(self.dataset)
        number_columns = len(self.labels)
        
        filled_cells   = sum(len(txn) for txn in self.dataset)       
        new_density    = int((filled_cells / (number_rows * number_columns)) * 100) if (number_rows * number_columns) else 0
        
        self.rows      .set(number_rows)
        self.columns   .set(number_columns)
        self.density   .set(new_density)
        
        self.label_minimum_support.config(text=f"Minimum Support ({self.rules['minimum_support'][0]} - {number_rows})")


    def _draw_dataset(self):
        rows    = self._input_value(self.rows,    "rows")
        columns = self._input_value(self.columns, "columns")
        size    = 50

        header_height = size * 0.5
        header_width  = size * 0.5
        canvas_height = header_height + rows    * size
        canvas_width  = header_width  + columns * size
        
        self._window = tkinter.Toplevel(self)
        self._canvas = tkinter.Canvas(self._window, height=canvas_height, width=canvas_width, bg="white")
        self._canvas.pack()

        labels = [create_column_labels(item) for item in range(columns)]

        for cell, label in enumerate(labels):
            position_x = header_width + cell*size + size/2
            position_y = header_height/2
            self._canvas.create_text(position_x, position_y, text=label, anchor="center")

        for row in range(rows):
            position_x = header_width/2
            position_y = header_height + row*size + size/2
            self._canvas.create_text(position_x, position_y, text=str(row+1), anchor="center")

        self._grid_data       = [[False]*columns for _ in range(rows)]
        self._cell_rectangles = {}        
        
        for r in range(rows):
            for c in range(columns):
                x0 = header_width + c*size
                y0 = header_height + r*size
                x1 = x0 + size
                y1 = y0 + size

                rect_id = self._canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
                self._cell_rectangles[(r,c)] = rect_id
                self._canvas.tag_bind(rect_id, "<Button-1>", lambda e, r=r, c=c: self._toggle_cell(r, c))

        tkinter.Button(self._window, text="Done", command=self._dataset_from_grid).pack(pady=5)


    def _toggle_cell(self, rows, columns):
        self._grid_data[rows][columns] = not self._grid_data[rows][columns]
        color = "black" if self._grid_data[rows][columns] else "white"
        self._canvas.itemconfig(self._cell_rectangles[(rows,columns)], fill=color)


    def _dataset_from_grid(self):
        self.dataset, self.labels = self.create_dataset_from_grid(self._grid_data)
        self._show_dataset()

        filled_cells = sum(1 for row in self._grid_data for filled in row if filled)
        total_cells  = len(self._grid_data) * (len(self._grid_data[0]) if self._grid_data else 0)
        new_density  = int((filled_cells / total_cells) * 100) if total_cells else 0
        
        self.density.set(new_density)
        self.label_minimum_support.config(text=f"Minimum Support ({self.rules['minimum_support'][0]} - {self.rows.get()})")
        
        self._window.destroy()


    def _show_dataset(self):
        lines = self.output_dataset(self.dataset, self.labels)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)


    def _clear_output(self):
        self.output.delete('1.0', tkinter.END)       
        self._show_dataset() if self.dataset else None


    def _generate_result(self):
        if self.dataset is None:
            self.output.insert(tkinter.END, ("!!! DATASET NOT DEFINED !!!") + "\n")
            self.output.see(tkinter.END)
            return

        algorithm_choice    = self.algorithm_names2keys[self.algorithm_choice.get()]
        minimum_support     = self._input_value(self.minimum_support,    "minimum_support")
        minimum_confidence  = self._input_value(self.minimum_confidence, "minimum_confidence")
        minimum_confidence  = self._input_value(self.minimum_confidence, "minimum_confidence") if self.algorithm_choice.get() == "association_rule" else None
        
        all_frequent_itemsets, algorithm_name = self.run_algorithm(self.dataset, algorithm_choice, minimum_support, minimum_confidence)
        
        lines = self.output_summary(self.dataset, self.labels, minimum_support, minimum_confidence, algorithm_name, all_frequent_itemsets)
        self.output.insert(tkinter.END, "\n".join(lines) + "\n")
        self.output.see(tkinter.END)


    def _input_value(self, value, label_name):      
        minimum, maximum = self.rules.get(label_name, (None, None))
        maximum          = self.rows.get() if label_name == "minimum_support" else maximum
  
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
