from nbclient import NotebookClient
import nbformat

def run_notebook_via_client(path):
    nb = nbformat.read(open(path), as_version=4)
    client = NotebookClient(nb, kernel_name='python3')
    client.execute()
    nbformat.write(nb, open(path, 'w'))

# Phase 1
# Improve T12 CR
run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/Hierarchical-SW_Retraining_T12Ensemble_A(itr1).ipynb')

run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/NSGA-ii_Retraining_New_T12Ensemble_A(itr2).ipynb')

run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/Naive-SW_Retraining_T12Ensemble_A(itr3).ipynb')

# Improve T7 CR
run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/Naive-SW_Retraining_T7Ensemble_A(itr4).ipynb')

run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/Hierarchical-SW_Retraining_T7Ensemble_A(itr5).ipynb')

run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/NSGA-ii_Retraining_New_T7Ensemble_A(itr6).ipynb')

# Phase 2
# Improve T12 CR
run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/Hierarchical-SW_Retraining_T12Ensemble_A(itr7).ipynb')

run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/NSGA-ii_Retraining_New_T12Ensemble_A(itr8).ipynb')

run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/Naive-SW_Retraining_T12Ensemble_A(itr9).ipynb')

# Improve T7 CR
run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/Naive-SW_Retraining_T7Ensemble_A(itr10).ipynb')

run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/Hierarchical-SW_Retraining_T7Ensemble_A(itr11).ipynb')

run_notebook_via_client('/mnt/Ensemble_Multi_Objective/MultiObj_Ensemble_C12C7_CR_A/NSGA-ii_Retraining_New_T7Ensemble_A(itr12).ipynb')
