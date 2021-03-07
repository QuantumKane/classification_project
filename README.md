# **Predicting Telco Churn**

## Planning the project
### Goals
The goal of this project is to determine drivers that indicate if customers from Telco are more likely to leave the company and to construct a Machine Learning classification model that most accurately predicts customer churn.

>Deliverables will include:
> - Final model created to predict if a customer will churn
> - This repo containing: 
>   - A Jupyter [Notebook]() detailing the process to create this model
>   - Files that hold functions to acquire and prep the data
>   - This Readme.md detailing project planning and exection, as well as instructions for project recreation
> - CSV file with customer_id, probability of churn, and prediction of churn

### Some Context
Why is customer loyalty important? What is the cost of churn over time?
According to Patrick Campbell from [ProfitWell](https://www.profitwell.com/customer-churn/analysis),
>"Even seemingly small, single-figure increases in churn rate 
>can quickly have a major negative effect on your company’s ability 
>to grow. What’s more, high churn rates are more likely to compound 
>over time."

### Data Dictionary


## Inital Questions and Hypotheses
### Questions
- Are customers more likely to churn as they stay longer?
- Does a customer having a streaming service cause them to be more loyal, more invested?
### Hypotheses
Does length of tenure  affect churn?  
`Null Hypothesis: Churn is independent of tenure length.`  
`Alternative Hypothesis: Customers who stay longer are more likely to churn.`  

Does a streaming service type increase customer loyalty?   
`Null Hypothesis: Churn is independent of having streaming services.`  
`Alternative Hypothesis: Customers with streaming services are less likely to churn.`  

****
# **Project Steps**
## Acquire & Prepare
### acquire.py
Data is acquired from the company SQL database, with credentials required. Functions are stored in the acquire file, which allows quick access to the data. Once the acquire file is imported, it can be used each time to access the data.
### prepare.py


## Explore
- Finding which features have the highest correlation to churn
- Testing hypothesis with Chi-Squared Contigency and T-test
- Visualizing churn with plots


## Model
After splitting and exploring the data, we progress to modeling.  
With the train data set, try four different classification models, determining which data features and model parameters create better predictions.


Evaluate the 3 top models on the validate data set
Evaluate the best model on the test data set
## Conclusion


# **How to Reproduce**
- Read this README.md
- Download the aquire.py, prepare.py, and project_report.ipynb into your working directory
- Run the project_report.ipynb notebook
