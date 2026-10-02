import pandas as pd

def clean_sales_data(input_file, output_file):
    #Import raw sales dataset
    print("Loading raw sales data...")
    df =pd.read_csv(input_file)
    print(f"Initial row count: {len(df)}")


#Check for initial missing values and duplicates
    print(f"Duplicate rows before cleaning: {df.duplicate().sum()}")
    print("Missing values per column:\n",df.isnull().sum())

#Duplicate based on unique transaction identifier
    if 'Order ID' in df.columns:
        df =df.drop_duplicates(subset=['Order id'])
    else:
        df = df.drop_duplicates()

#Handle missing values
#Remove records missing critical revenue/sales info
    critical_cols = [col for col in ['OrderID', 'Sales', 'Profit'] if col in df.columns]
    df = df.dropna(subset=critical_cols)

#Fill categorical nulls with fallback labesl
    text_cols =['Region', 'Category', 'Sub-Category','Segment']
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].fillna('Unassigned')

#Correct data and dates

    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
