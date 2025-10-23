# src/feature_engineering.py
from sklearn.base import BaseEstimator, TransformerMixin


class FeatureEngineer(BaseEstimator, TransformerMixin):
    """
    Custom transformer for feature engineering in house price prediction.

    Creates engineered features:
    - TotalSF: Total square footage
    - TotalBath: Total bathrooms
    - HouseAge: Age of house
    - YearsSinceRemod: Years since remodeling
    - WasRemodeled: Binary indicator for remodeling
    """

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Create a copy to avoid modifying original data
        X_copy = X.copy()

        # Total square footage
        X_copy['TotalSF'] = X_copy['1stFlrSF'] + X_copy['2ndFlrSF'] + X_copy['TotalBsmtSF']

        # Total bathrooms
        X_copy['TotalBath'] = (X_copy['FullBath'] +
                               0.5 * X_copy['HalfBath'] +
                               X_copy['BsmtFullBath'] +
                               0.5 * X_copy['BsmtHalfBath'])

        # House age (assuming current year is 2023)
        X_copy['HouseAge'] = 2023 - X_copy['YearBuilt']

        # Years since remodel
        X_copy['YearsSinceRemod'] = 2023 - X_copy['YearRemodAdd']

        # Was remodeled (binary)
        X_copy['WasRemodeled'] = (X_copy['YearBuilt'] != X_copy['YearRemodAdd']).astype(int)

        return X_copy
