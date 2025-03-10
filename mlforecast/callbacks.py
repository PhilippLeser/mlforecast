# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/callbacks.ipynb.

# %% auto 0
__all__ = ['SaveFeatures']

# %% ../nbs/callbacks.ipynb 3
import pandas as pd

# %% ../nbs/callbacks.ipynb 4
class SaveFeatures:
    """Saves the features in every timestamp."""

    def __init__(self):
        self._inputs = []

    def __call__(self, new_x):
        self._inputs.append(new_x)
        return new_x

    def get_features(self):
        """Retrieves the input features for every timestep"""
        return pd.concat(self._inputs)
