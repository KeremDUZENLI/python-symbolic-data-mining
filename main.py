from interface.cli import CLI
from interface.gui import GUI

from algorithms     import ALGORITHMS, run_algorithm
from helper.dataset import create_dataset, create_dataset_default, create_dataset_from_grid
from helper.output  import output_dataset, output_summary


def run(parameter):
    if parameter == "CLI":
        CLI(create_dataset, create_dataset_default, ALGORITHMS, run_algorithm, output_dataset, output_summary)
    if parameter == "GUI":
        GUI(create_dataset, create_dataset_default, create_dataset_from_grid, ALGORITHMS, run_algorithm, output_dataset, output_summary)


if __name__ == "__main__":
    run("GUI")
