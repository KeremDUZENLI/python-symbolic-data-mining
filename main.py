from interface.cli   import CLI
from interface.gui   import GUI

from algorithms      import ALGORITHMS, run_algorithm
from helper.dataset  import create_dataset_default, create_dataset
from helper.output   import output_dataset, output_summary


CLI(create_dataset_default, create_dataset, ALGORITHMS, run_algorithm, output_dataset, output_summary)
# GUI(create_dataset_default, create_dataset, ALGORITHMS, run_algorithm, output_dataset, output_summary)


# <./core02_assrulex.sh sample/laszlo.rcf 3 50% -alg:apriori -rule:all --names>
