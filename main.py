from interface.cli   import CLI
from interface.gui   import GUI

from algorithms      import ALGORITHMS, run_algorithm
from helper.dataset  import create_dataset, create_dataset_default, create_dataset_from_grid
from helper.output   import output_dataset, output_summary


# CLI(create_dataset, create_dataset_default, create_dataset_from_grid, ALGORITHMS, run_algorithm, output_dataset, output_summary)
GUI(create_dataset, create_dataset_default, create_dataset_from_grid, ALGORITHMS, run_algorithm, output_dataset, output_summary)
