import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.inspection import permutation_importance
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

path = os.getcwd()
path = path + '/data/'

wine = pd.read_csv(path+'wine.csv')

data = wine[['alcohol','sugar','pH']].to_numpy()
target = wine['class'].to_numpy()

train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)
rf = RandomForestClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']),np.mean(scores['test_score']))
rf.fit(train_input, train_target)
print(rf.feature_importances_)

rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
rf.fit(train_input, train_target)
print(rf.oob_score_)

et = ExtraTreesClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(et, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']),np.mean(scores['test_score']))
et.fit(train_input,train_target)
print(et.feature_importances_)

# GradientBoosting : 경사하강법 ...
gb = GradientBoostingClassifier(random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']),np.mean(scores['test_score']))

# learning_rate 가 커지면 커질 수록 update 크기 가 커짐 ..
gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2, random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']),np.mean(scores['test_score']))
gb.fit(train_input,train_target)
print(gb.feature_importances_)

hsg = HistGradientBoostingClassifier(max_iter=100, random_state=42)
scores = cross_validate(hsg, train_input, train_target, return_train_score=True)
print(np.mean(scores['train_score']),np.mean(scores['test_score']))

hsg.fit(train_input, train_target)
result = permutation_importance(hsg, train_input, train_target, n_repeats=10, random_state=42, n_jobs=-1)
print(result.importances_mean)

result = permutation_importance(hsg, test_input, test_target, n_repeats=10, random_state=42, n_jobs=-1)
print(result.importances_mean)

hsg.score(test_input, test_target)

xgb = XGBClassifier(tree_method='hist', random_state=42)
scores = cross_validate(xgb, train_input, train_target,return_train_score=True)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

lgb =  LGBMClassifier(random_state=42)
scores=cross_validate(lgb, train_input, train_target,return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))