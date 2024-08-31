# Custom Transformer for Time-Related Features
class TimeFeatures(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['day_of_week'] = X['date_id'].dt.dayofweek
        X['is_weekend'] = X['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
        X['week_of_year'] = X['date_id'].dt.isocalendar().week
        X['month'] = X['date_id'].dt.month
        X['year'] = X['date_id'].dt.year
        return X