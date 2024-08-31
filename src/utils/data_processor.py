from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer

# Custom Transformer for Processing Data Sources
class DataProcessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        # No fitting necessary, return self
        return self

    def transform(self, X):
        # Drop columns 'item' and 'invoice_num' if they exist
        X = X.drop(['item', 'invoice_num'], axis=1, errors='ignore')

        # Drop rows with missing values in 'date_id', 'item_dept', or 'item_qty' columns
        X.dropna(subset=['date_id', 'item_dept', 'item_qty'], inplace=True)

        # Drop rows with negative item_qty or net_sales
        X = X[(X['item_qty'] > 0) & (X['net_sales'] > 0)]

        # Convert 'store', 'item_dept', and 'date_id' columns to categorical data types
        X['store'] = X['store'].astype('category')
        X['item_dept'] = X['item_dept'].astype('category')
        X['date_id'] = X['date_id'].astype('category')

        # Group the data by 'store', 'item_dept', and 'date_id' and aggregate 'item_qty' and 'net_sales' by summing them
        X = X.groupby(['store', 'item_dept', 'date_id']).agg({
            'item_qty': 'sum',
            'net_sales': 'sum'
        }).reset_index()

        # Create a new column 'primary_key' by concatenating 'store', 'item_dept', and 'date_id' as strings
        X['primary_key'] = X['store'].astype(str) + '_' + X['item_dept'].astype(str) + '_' + X['date_id'].astype(str)

        # Sort the DataFrame by 'store', 'item_dept', and 'date_id'
        X.sort_values(by=['store', 'item_dept', 'date_id'], inplace=True)

        # Reorder the columns to have 'primary_key' first followed by the other columns
        X = X[['primary_key', 'store', 'item_dept', 'date_id', 'item_qty', 'net_sales']]

        # Return the transformed DataFrame
        return X