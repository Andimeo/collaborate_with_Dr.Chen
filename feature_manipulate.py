from sklearn.base import BaseEstimator, TransformerMixin

import numpy as np
import pandas as pd
import os

if not os.path.exists('features.csv'):
    user_feature = pd.read_csv('userFeature.csv', delimiter='\t')
    ad_feature = pd.read_csv('adFeature.csv', delimiter=',')
    train = pd.read_csv('train.csv', delimiter=',')

    df = pd.merge(train, user_feature, on='uid', how='outer')
    train = pd.merge(df, ad_feature, on='aid', how='outer')
    train.to_csv('features.csv', index=False)
    del user_feature, ad_feature, df
else:
    train = pd.read_csv('features.csv')
print("load features complete!")

one_hot_attribs = ['LBS','age','carrier','consumptionAbility','education','gender','house','os','ct','marriageStatus','advertiserId','campaignId', 'creativeId', 'adCategoryId', 'productId', 'productType']
vector_attribs = ['appIdAction','appIdInstall','interest1','interest2','interest3','interest4','interest5','kw1','kw2','kw3','topic1','topic2','topic3']

class DataFrameSelector(BaseEsitimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values


class VectorizerTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        for column in X:
            value_set = set()
            value_list = []
            for i in range(df.shape[0]):
                v = df.iloc[i][column]
                if v not in value_set:
                    value_list.append(v)
                    value_set.add(v)
            print("for %s num: %d" % (column, len(set)))
        return self

    def transform(self, X):
        return X

vt = VectorizerTransformer()
vt.fit(train)
