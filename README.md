# ICLR_2025_Submission_10435
ICLR 2025 Submission Number 10435

The folder "Step_1_SingleObj" contains the code to train M0 Catboost model, the Random Selection AutoGeTS code, Sliding Window AutoGeTS code, Hierarchical Sliding Window AutoGeTS code, and Genetic Algorithm AutoGeTS code. It also contains the code of using traditional data augmentation method, the Easy Data Augmentation (EDA) tool, to generate synthtic samples for experiments.

The folder "Step_2_Pathway" contains information on our ensemble algorithm experiment. The folder ending with "A" is the ensemble algorithm, the folder ending with "C" is the random sequence, the "Naive-SW" is the "Stack SW", the "Hierarchical-SW" is the "Stach HSW", and the "NSGA-II_Retraining" is the "Stack GA".
The 3 example selection strategies (SW, HSW, GA), and the 4 objectives (maximising CR, CBA, OBA, OF1) are also shown in these codes. The same functions were used in Experiments in Section 4.

The folder "AutoGeTS" contains the original model M0 and the code used to train M0. The synthetic data would be disclosed later after the approval of the data provider. Sorry that the original data "tickets_topics.csv" is owned by the company so we are not allowed to disclose it. Thus, we have removed confidential information and placed others in "Train_PCA_YZ_withPred_0".

The PDF "ICLR_AutoGeTS_Appendix F_TREC-6 Results.pdf" presents the results of experiments conducted on TREC-6, an additional dataset, to assess the generalizability of our proposed AutoGeTS workflow.

The PDF "KDD_2025_AutoGeTS_Submission" contains the submitted draft of the revised AutoGeTS paper to KDD 2025.

Required packages: 
pip install catboost==1.2.5 inspyred==1.0.2 joblib==1.1.0 matplotlib==3.4.3 matplotlib-inline==0.1.7 numpy==1.26.4 "nvidia-ml-py==12.555.43" pandas==2.2.2 plotly==5.22.0 psutil==5.8.0 scikit-learn==0.24.2 openpyxl
