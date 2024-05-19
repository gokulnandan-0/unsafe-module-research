# -*- coding: utf-8 -*-
"""Example2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JXxzAbhDQvKpCrhNRNFiOKmuqh18Nvpy
"""

import pandas as pd

# Ensure you've copied some data to your clipboard before running this
df = pd.read_clipboard()
print(df)

'''
Now i am pruning this method by raising an error instead'''
def safe_read_clipboard(*args, **kwargs):
  raise PermissionError("Access to clipboard is not allowed")
pd.read_clipboard = safe_read_clipboard

try:
    data = pd.read_clipboard()
except PermissionError as e:
    print(e)