class ItemFeatures(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['total_item_qty'] = X.groupby(['store', 'item_qty'])['item_qty'].transform('sum')
        X['avg_item_qty'] = X.groupby(['store', 'item_qty'])['item_qty'].transform('mean')
        return X