from sklearn.datasets import *
from sklearn import tree
from dtreeviz.trees import *

#
# 回归树
#
regr = tree.DecisionTreeRegressor(max_depth=2)
boston = load_boston()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(boston.data,boston.target,random_state=33,test_size=0.25)
regr.fit(x_train,y_train)
print(regr.score(x_test,y_test))
regr.fit(boston.data, boston.target)

# 可视化
#viz = dtreeviz(regr, boston.data, boston.target, target_name='price', feature_names=boston.feature_names)
#viz.view()

#
# 使用auto-sklearn，选择max_depth
#
from sklearn.ensemble import RandomForestClassifier


#
# 随机森林回归
#
from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor()
print(x_test.shape)
rfr.fit(x_train,y_train)
print(rfr.score(x_test,y_test))

#from sklearn.datasets import load_boston
#from sklearn.model_selection import cross_val_score
#from sklearn.tree import DecisionTreeRegressor
#boston = load_boston()
#print(boston)
#regressor = DecisionTreeRegressor(random_state=0)
#print(cross_val_score(regressor, boston.data, boston.target, cv=1, scoring = "neg_mean_squared_error"))

#####################################################
##                 auto-sklearn                    ##
#####################################################
#from sklearn.datasets import load_boston
#from autosklearn.regression import AutoSklearnRegressor

# 导入数据集
#boston = load_boston()  # 加载数据集

# 限制算法搜索最大时间，更快得到结果
#auto_model = AutoSklearnRegressor(
#    time_left_for_this_task=120, per_run_time_limit=10)
#auto_model.fit(boston.data, boston.target)

# 查看模型效果，用R方来看
#auto_model.score(boston.data, boston.target)