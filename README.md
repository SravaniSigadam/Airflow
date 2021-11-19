# Implementation of Apache Airflow

In order to understand how to automatically evolve models, generate reports and how datapipelines can be automated, I have implemented Airflow.

Apache Airflow is an open-source job scheduler that can organize, execute, and monitor any workflow across any periodic time interval.

- Firstly, I have built a Random Forest Classifier on a sample blob of data to train the model and saved it using joblib. 
- The model is then loaded in another file, and is used to predict the dependent variable on a scoring dataset in another file.
- Scheduled both the training and scoring tasks by creating my own Directed Acyclic Graphs (DAGs) on web browser using default port localhost:8080
- The DAG is specified with a DAG python file that specifies the nodes and dependencies between the nodes.
- Status of the tasks can be verified using logs.
