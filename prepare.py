import pandas as pd
from sklearn.model_selection import train_test_split

def split(df, stratify_by=None):
    """
    Train, validate, test split
    To stratify, send in a column name
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=123)
        train, validate = train_test_split(train, test_size=.3, random_state=123)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    return train, validate, test


def telco_prep(df):
    '''
    Take in dataframe
    Return train, validate, test dfs.
    '''
    # Changing features to 0 for no and 1 for yes
    df['streaming_movies'] = df.streaming_movies.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    df['streaming_tv'] = df.streaming_tv.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    df['online_security'] = df.online_security.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    df['online_backup'] = df.online_backup.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    df['device_protection'] = df.device_protection.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    df['tech_support'] = df.tech_support.replace({'No internet service': 0, 'No': 0, 'Yes': 1})
    df['churn'] = df.churn.replace({'No': 0, 'Yes': 1})
    
    # Dropping unnecessary columns
    df = df.drop(['total_charges'],axis=1)
    
    # Prepping tenure columns
    # Renaming tenure to tenure_months before creating a tenure_years column
    df = df.rename(columns = {'tenure':'tenure_months'})
    
    # Creating a new feature, tenure in years, by dividing tenure in months by 12
    df['tenure_years'] = round(df.tenure_months / 12, 2)

    # Split data into train, validate, test dfs.
    train, validate, test = split(df, stratify_by='churn')

    return train, validate, test