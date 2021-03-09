# **Predicting Telco Churn**

## Planning the project
### Goals
The goal of this project is to determine drivers that indicate if customers from Telco are more likely to leave the company and to construct a Machine Learning classification model that most accurately predicts customer churn.

>Deliverables will include:
> - This repo containing: 
>   - A Jupyter Notebook detailing the process to create this model
>   - Files that hold functions to acquire and prep the data
>   - This Readme.md detailing project planning and exection, as well as instructions for project recreation
> - Final model created to predict if a customer will churn
> - CSV file with customer_id, probability of churn, and prediction of churn

### Some Context
Why is customer loyalty important? What is the cost of churn over time?
According to Patrick Campbell from [ProfitWell](https://www.profitwell.com/customer-churn/analysis),
>"Even seemingly small, single-figure increases in churn rate 
>can quickly have a major negative effect on your company’s ability 
>to grow. What’s more, high churn rates are more likely to compound 
>over time."

### Data Dictionary

After prepping the dataframe, the variables are the following:

| Feature                       | Definition                            | Data Type                          |
|-------------------------------|---------------------------------------|------------------------------------|
|contract_type_id               |monthly, year, or two-year             |int - (0-2)                         |
|payment_type_id                |type of payment                        |int - (0-2)                         |
|customer_id                    |unique identifier                      |object                              |
|partner                        |has partner or not                     |int - boolean                       |
|dependents                     |has dependents or not                  |int - boolean                       |
|phone_service                  |one or multiple lines, or no service   |int - (0-2)                         |
|multiple lines                 |multiple lines or not                  |object                              |
|internet_service_type          |DSL, fiber optic, or no service        |object                              |
|online_security_1              |security or not                        |int - boolean                       |
|online_backup                  |backup or not                          |int - boolean                       |
|device_protection              |protection or not                      |int - boolean                       |
|tech_support_1                 |support or not                         |int - boolean                       |
|streaming_tv                   |streaming or not                       |int - boolean                       |
|streaming_movies               |streaming or not                       |int - boolean                       |
|contract_type                  |monthy, 1 year, 2 year                 |object                              |
|paperless_billing              |paperless or mailed bills              |int - boolean                       |
|monthly charges                |in USD                                 |float                               |
|churn                          |customer has left the company or not   |int - boolean                       |
|tenure (months or years)       |length the customer has remained       |int for months, float for years     |
|internet_service_type_id_orig  |DSL, fiber optic, or no service        |int - (0-2)                         |
|tech_support_orig              |tech support or not                    |int - boolean                       |
|internet_service_type_2        |DSL or not                             |int - boolean                       |                 
|internet_service_type_3        |Fiber Optic or not                     |int - boolean                       |
|payment type                   |check or bank transfer                 |object                              |
|online_security_orig           |security or not                        |int - boolean                       |



## Inital Questions and Hypotheses
### Questions
- Are customers more likely to churn if they have fiber optic?
- If customers have both fiber and tech support, would they stay?
### Hypotheses
Is there a difference between the means of monthly_charges for fiber customers who churn and those who don't? 
`Null Hypothesis: There is no difference between monthly charges for fiber customers who churn and those who do not`
`Alternate Hypothesis: There is a difference between monthly charges for fiber customers who churn and those who do not`

Is there a difference between the means of monthly_charges for fiber customers who have tech support and those who don't? 
`Null Hypothesis: There is no difference between the means of monthly charges for fiber customers who have tech support and those who don't`
`Alternate Hypothesis: There is a difference between the means of monthly_charges for fiber customers who have tech support and those who don't`

****
# **Project Steps**
## Acquire & Prepare
### acquire.py
Data is acquired from the company SQL database, with credentials required. Functions are stored in the acquire file, which allows quick access to the data. Once the acquire file is imported, it can be used each time to access the data

### prepare.py
- Converted select values of "No" and "Yes" to 0 and 1
- Dropped "total_charges" as it was redundant, "gender" and "senior_citizen" because they were not significant
- Created "tenure_months" and "tenure_years" columns, both calculated from tenure
- Created dummy variables from 'internet_service_type_id', 'online_security', and 'tech_support' columns

## Explore
- Finding which features have the highest correlation to churn
- Testing hypothesis with T-test
- Visualizing churn with plots

## Model
After splitting and exploring the data, we progress to modeling.  
With the train data set, try four different classification models, determining which data features and model parameters create better predictions.
- 2 different Logistic Regression Models
- Decision Tree
- Random Forest

Evaluate the best model on the test data set
### Outcome
- The first Logistic Regression Model had the best reults, if only slightly
- That model performed even better on the test data

# **How to Reproduce**
- Read this README.md
- Download the aquire.py, prepare.py, and project_report.ipynb into your working directory
- Run the project_report.ipynb notebook
