def load_data():
    import pandas as pd
    df_data = pd.read_csv('C:\Users\me\OneDrive\Attachments\Desktop\NIBM\ML\ML_CW_Project\ml_cw_sales_forecast\data\training_data.csv', parse_dates=['date_id'])
    test_data = pd.read_csv('C:\Users\me\OneDrive\Attachments\Desktop\NIBM\ML\ML_CW_Project\ml_cw_sales_forecast\data\test_data.csv', parse_dates=['date_id'])

    return df_data,test_data