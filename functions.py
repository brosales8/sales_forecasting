import pandas as pd
import numpy as np
import calendar
import matplotlib.pyplot as plt

def clean_sales(df_sales, target_items):
    '''
    This function is intended to perform cleaning, formating and 
    filtering operations to sales transaction datasets.
    
    Parameters:
    'df_sales' : (Pandas DataFrame) Dataset contains sales transactions
    'target_items': (Dictionary) Contains the items of interest for the analysis    
    '''
    df = df_sales.copy()
    # Rename Columns
    column_names = ['del1',
                'type',
                'date',
                'inv_num',
                'item_name',
                'customer',
                'item_description',
                'quantity',
                'price',
                'amount',
                'del2'
               ]
    df.columns = column_names
    
    df.drop(['del1','del2'], axis = 1, inplace = True) # drop unuseful columns 
    df.dropna(axis = 0, thresh=5, inplace = True) # Drop rows with NaN values
    
    # Filter all transaction different than Samples
    df = df[~df['customer'].str.lower().str.contains('sample')]
    
    # Extract item_code from item_description
    df['item_code'] = df['item_description'].str.split(expand=True)[0]
    df.drop(['item_description',
             'type',
             'inv_num',
             'customer',
             'amount',
             'item_name'
            ], axis = 1, inplace = True) # Drop columns no interesting for the Analysis
    df = df[df['item_code'].isin(target_items)] # Filter interesting items for Analysis
    
    df['date'] = pd.to_datetime(df['date'], format= '%m/%d/%Y')
    df['month'] = df.date.dt.month # Create a column for months
    df['year'] = df.date.dt.year # Create a column for year
    df.drop('date', inplace = True, axis=1) # Drop column date   
    
    print('Final Dataset Shape: {}'.format(df.shape))
    
    # Assign float32 type for numeric features
    df.quantity = df.quantity.astype(np.float32)
    df.price = df.price.astype(np.float32)
    
    return df

def extract_temperature(df_temperature, new_colum_name):
    '''
    Return a DataFrame time series containing a monthly temperature data point per each row.
    The function performs some transformations since the original csv file is containing the
    data points by columns by years.
    
    Parameters:
    "df_temperature": Pandas DataFrame with temperatures points
    "new_column_name": Name of column with temp points to be returned with the final DataFrame
    '''
    # Create an empty dataframe to storage temperatures
    df_to_return = pd.DataFrame({ 'date': [], new_colum_name:[] })    
    
    df_temperature_transposed = df_temperature.T # Transpose temperature DF to iter on it
    str_month_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
    years = df_temperature_transposed.iloc[0].tolist() # Create a list with the years
    
    for index, row in df_temperature_transposed.iterrows():    
        if index != 'Year':
            month = str(str_month_to_num[index])
            for j, year in enumerate(years):
                date = str(year) + '-' + month + '-' + '01'
                temp = row[j]
                new_row = {'date': date, new_colum_name: temp }
                df_to_return = df_to_return.append(new_row, ignore_index=True)
    
    df_to_return['date'] = pd.to_datetime(df_to_return['date']) # Convert date to datetime type
    
    return df_to_return

def plot_item(data_frame, item_codes, item_names, color_symbol):
    '''
    Function to plot every time series in a grid of plots using original
    Dataset.
    Parameters:
    data_frame: (Pandas Dataframe) contains the data point for each Time Series
    item_codes: (List) Storage item codes for each product
    item_names: (List) Storage item names for each product
    color_symbol: (List) Contains color and chart options for each plot
    '''    
    fig, ax = plt.subplots(3, 2, figsize=(20,25))
    
    r = 0 # Denote the row for the Subplot
    c = 0 # Denote the col for the Subplot
    
    for index, item in enumerate(item_codes):
        item_set = data_frame[data_frame['item_code']==item]
        ax[r][c].plot(item_set['date'], item_set['quantity'], color_symbol[index])
        
        ax[r][c].set_xlabel('Year-Month')
        ax[r][c].set_ylabel('Sold Btls')
        ax[r][c].set_title(item_names[index])
        c += 1
        if c == 2:
            c = 0
            r += 1
        
    plt.show()
    