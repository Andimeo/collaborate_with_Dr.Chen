import numpy as np
import pandas as pd

user_feature = pd.read_csv('userFeature.csv', delimiter='\t')
ad_feature = pd.read_csv('adFeature.csv', delimiter=',')
train = pd.read_csv('train.csv', delimiter=',')

df = pd.merge(train, user_feature, on='uid', how='outer')
train = pd.merge(df, ad_feature, on='aid', how='outer')

