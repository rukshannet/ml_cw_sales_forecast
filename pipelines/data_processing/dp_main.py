from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer

def createPipeline:
    # Define the pipeline
    pipeline = Pipeline(steps=[
        ('data_processing', DataProcessor()),
        ('sales_features', SalesFeatures()),
        ('item_features', ItemFeatures()),
        ('time_features', TimeFeatures()),
        ('outlet_features', OutletFeatures()),
    ])


    # Run the pipeline
    processed_df_train = pipeline.fit_transform(df_data)
    processed_df_test = pipeline.fit_transform(test_data)

return processed_df_train,processed_df_test