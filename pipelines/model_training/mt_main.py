from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

def createPipeline:
    # Preprocessing for numerical and categorical data
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['net_sales', 'lag_1_sales', 'lag_7_sales', 'rolling_mean_7',
                                    'cumulative_sales', 'total_item_qty', 'avg_item_qty',
                                    'day_of_week', 'week_of_year', 'month', 'year',
                                    'total_store_sales', 'avg_dept_sales', 'store_size'
                                    ]),
            ('cat', OneHotEncoder(), ['store', 'item_dept', 'is_weekend'])
        ])


    # Define a list of models to try
    models = [
        ('Linear Regression', LinearRegression()),
        ('Decision Tree', DecisionTreeRegressor(random_state=42)),
        ('Random Forest', RandomForestRegressor(n_estimators=100, random_state=42)),
        ('Gradient Boosting', GradientBoostingRegressor(random_state=42)),
        ('XGBoost', XGBRegressor(random_state=42))
    ]

    # Iterate through the models and evaluate
    for name, model in models:
        model_pipeline.set_params(model=model)  # Update the model in the pipeline
        model_pipeline.fit(X_train, y_train)
        r2_score = model_pipeline.score(X_test, y_test)
        print(f'{name} R^2 score: {r2_score}')
        y_pred = model_pipeline.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        print(f'{name} RMSE: {rmse}')
        mape = mean_absolute_percentage_error(y_test, y_pred)
        print(f'{name} MAPE: {mape}')