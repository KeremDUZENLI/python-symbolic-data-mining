from interface.cli import CLI
from interface.gui import GUI

from algorithms     import ALGORITHMS, run_algorithm
from helper.dataset import create_dataset, create_dataset_default
from helper.output  import output_dataset, output_summary


if __name__ == "__main__":
    CLI(create_dataset, create_dataset_default, ALGORITHMS, run_algorithm, output_dataset, output_summary)
    GUI(create_dataset, create_dataset_default, ALGORITHMS, run_algorithm, output_dataset, output_summary)
