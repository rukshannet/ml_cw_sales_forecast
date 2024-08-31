class SalesFeatures(BaseEstimator, TransformerMixin):
    # Creates sales-related features
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['lag_1_sales'] = X.groupby(['store', 'item_dept'])['net_sales'].shift(1).fillna(0)
        X['lag_7_sales'] = X.groupby(['store', 'item_dept'])['net_sales'].shift(7).fillna(0)
        X['rolling_mean_7'] = X.groupby(['store', 'item_dept'])['net_sales'].transform(lambda x: x.rolling(7).mean()).fillna(0)
        X['cumulative_sales'] = X.groupby(['store', 'item_dept'])['net_sales'].cumsum()
        return X