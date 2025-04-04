import pandas as pd
import numpy as np
from math import ceil


def dataset_dimensions(df):
    """
    Show dimensions of the dataframe.
    """
    print("Dimensions of the dataset:")
    print(f" Number of rows: {df.shape[0]}")
    print(f" Number of columns: {df.shape[1]}\n")

    return


def column_unique_values(df):
    """
    Show unique values for each column in the dataframe.
    """
    for col in df.columns:
        print(f"{col: >24}: {df[col].nunique()}")

    return


def column_missing_values(df):
    """
    Show the total number of missing values per columns, if they are present.
    """
    print("Columns with missing values:\n")

    return df.isnull().sum()[df.isnull().sum() > 0]


def numeric_categorical_data(df):
    """
    Separates numerical and categorical data and return their numbers.
    """
    numeric_data = df.select_dtypes(include=[np.number])
    categorical_data = df.select_dtypes(exclude=[np.number])

    print(f"Number of numerical variables: {numeric_data.shape[1]}\n")
    print(f"Number of categorical variables: {categorical_data.shape[1]}")

    return


def lowercase_column_name(df):
    """
    Convert feature names into lower letters.
    """
    df.columns = map(str.lower, df.columns)
    return


def column_to_datetime(df, columns):
    """
    Convert dates to datetime format.
    """
    for column_name in columns:
        df[column_name] = pd.to_datetime(df[column_name])


def number_unique_values(df):
    """
    Show the number of unique values for each feature in a four row dataframe.
    """
    n_unique_values = []
    number_of_features = len(df.columns)
    n = ceil(number_of_features / 4)
    print(f"\nTotal number of rows: {df.shape[0]:12}\n")
    print(f"Total number of features: {number_of_features}\n")

    for col in df.columns:
        n_unique_values.append(df[col].nunique())

    df_unique_values = pd.DataFrame(
        n_unique_values, df.columns, columns=["n_unique_values"]
    )

    part_1 = df_unique_values.iloc[0:n]
    part_2 = df_unique_values.iloc[n: 2 * n]
    part_3 = df_unique_values.iloc[2 * n: 3 * n]
    part_4 = df_unique_values.iloc[3 * n:]

    part_1.reset_index(level=0, inplace=True)
    part_1 = part_1.rename(columns={"index": "feature"})

    part_2.reset_index(level=0, inplace=True)
    part_2 = part_2.rename(columns={"index": "feature"})

    part_3.reset_index(level=0, inplace=True)
    part_3 = part_3.rename(columns={"index": "feature"})

    part_4.reset_index(level=0, inplace=True)
    part_4 = part_4.rename(columns={"index": "feature"})

    df_final = pd.concat([part_1, part_2, part_3, part_4], axis=1, sort=False)

    if df.isnull().values.any():
        df_final.fillna("None", inplace=True)

    return df_final


def missing_in_columns(df):
    print("Features with missing values:\n")
    return df.isnull().sum()[df.isnull().sum() > 0]


def medical_speciality():
    str1 = """1     allergy/immunology
    2        cardiac surgery            
    3  head and neck surgery      
    4        general surgery             
    5      pediatric surgery           
    6        plastic surgery              
    7          chest surgery               
    8       vascular surgery            
    9         medical clinic               
    10           dermatology                 
    11         endocrinology             
    12         gastrosurgery              
    13      gastroenterology         
    14            geriatrics                
    15            gynecology                  
    16 gynecology/obstetrics        
    17            hematology              
    18           infectology                 
    19            nephrology              
    20          neurosurgery"""

    str2 = """21 neurology
    22 ophthalmology
    23 surgical oncology
    24 clinical oncology
    25 pediatric oncology
    26 orthopedics
    27 otorhinolaryngology
    28 pediatrics
    29 pulmonology
    30 proctology
    31 radiotherapy
    32 urology
    33 mastology
    34 cutaneous oncology
    35 pelvic surgery
    36 abdominal surgery
    37 dentistry
    38 liver transplantation
    99 ignored
    """

    str3 = '''
    1 allergy/immunology        21 neurology
    2 cardiac surgery               22 ophthalmology
    3 head and neck surgery   23 surgical oncology
    4 general surgery              24 clinical oncology
    5 pediatric surgery            25 pediatric oncology
    6 plastic surgery                26 orthopedics
    7 chest surgery                  27 otorhinolaryngology
    8 vascular surgery             28 pediatrics
    9 medical clinic                  29 pulmonology
    10 dermatology                  30 proctology
    11 endocrinology                31 radiotherapy
    12 gastrosurgery                32 urology
    13 gastroenterology           33 mastology
    14 geriatrics                       34 cutaneous oncology
    15 gynecology                    35 pelvic surgery
    16 gynecology/obstetrics   36 abdominal surgery
    17 hematology                   37 dentistry
    18 infectology                    38 liver transplantation
    19 nephrology                    99 ignored
    20 neurosurgery'''

    # splt_lines = zip(str1.split("\n"), str2.split("\n"))

    # horizontal join (best for print)
    # result = "\n".join([x.strip() + "        " + y.strip() for x, y in splt_lines])
    legend_text = str3

    return legend_text


def count_entries_outracla(bottom, top, df, column='outracla'):
    if bottom != 1 and top != 1:
        total_count = (
            df[column]
            .value_counts(normalize=False)[((df[column]
                                             .value_counts(normalize=False) >= bottom) & (df[column]
                                                                                          .value_counts(
                normalize=False) <= top))]
        ).shape[0]
    else:
        total_count = (
            df[column]
            .value_counts(normalize=False)[(df[column]
                                            .value_counts(normalize=False) == 1)]
        ).shape[0]

    return total_count


# def separate_recnenhum(target_column, label_column, df):
#    """
#    target column: topogrup or topo
#    label column: recnenhum
#    """
#    # create two series containing cancer types with(0)/without(1) recurrence
#    recid_0 = df[target_column][df[label_column] == 0].value_counts()[
#        df[target_column][df[label_column] == 0].value_counts() > 0]
#    recid_1 = df[target_column][df[label_column] == 1].value_counts()[
#        df[target_column][df[label_column] == 1].value_counts() > 0]
#
#    # convert series to dataframes
#    df1 = recid_1.to_frame().reset_index()
#    df0 = recid_0.to_frame().reset_index()
#
#    # merge dataframes
#    # df01 = pd.merge(df1, df0, on='index')
#    df01 = df1.merge(df0, how='left', left_on='index', right_on='index')
#    df01.fillna(0, inplace=True)
#
#    if target_column == 'topogrup':
#        df01 = df01.rename(columns={'index': 'topogrup', 'topogrup_x': 'rec1_counts', 'topogrup_y': 'rec0_counts'})
#
#    if target_column == 'topo':
#        df01 = df01.rename(columns={'index': 'topo', 'topo_x': 'rec1_counts', 'topo_y': 'rec0_counts'})
#
#    return df01, target_column

def separate_recnenhum(target_column, label_column, df):
    """
    target column: topogrup or topo
    label column: recnenhum
    """
    # create two series containing cancer types with(0)/without(1) recurrence
    recid_0 = df[target_column][df[label_column] == 0].value_counts()[
        df[target_column][df[label_column] == 0].value_counts() > 0]
    recid_1 = df[target_column][df[label_column] == 1].value_counts()[
        df[target_column][df[label_column] == 1].value_counts() > 0]

    # convert series to dataframes
    df1 = recid_1.to_frame().reset_index()
    df0 = recid_0.to_frame().reset_index()
    
    # merge dataframes
    # df01 = df1.merge(df0, how='left', left_on='index', right_on='index')
    df01 = df1.merge(df0, how='left', left_on=target_column, right_on=target_column)

    df01.fillna(0, inplace=True)
    df01.rename(columns={'index': target_column, 'topo_x': 'rec1_counts', 'topo_y': 'rec0_counts'}, inplace=True)
    df01.rename(columns={'count_x': 'rec1_counts', 'count_y': 'rec0_counts'}, inplace=True)
        
    return df01, target_column

def ratio_recnenhum(df):
    # calculate recurrence percentages
    df['rec_sum'] = df['rec1_counts'] + df['rec0_counts']
    df['rec0_ratio'] = (df['rec0_counts'] / df['rec_sum']) * 100
    df['rec1_ratio'] = (df['rec1_counts'] / df['rec_sum']) * 100
    # round the percentage
    ratio = df.round(1)

    return ratio

