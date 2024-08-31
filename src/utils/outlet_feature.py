# Custom Transformer for Outlet-Related Features
class OutletFeatures(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['total_store_sales'] = X.groupby('store')['net_sales'].transform('sum')
        X['avg_dept_sales'] = X.groupby(['store', 'item_dept'])['net_sales'].transform('mean')
        X['store_size'] = X.groupby('store')['item_dept'].transform('nunique')
        return X