# about-ml 有关机器学习

----------

## 一、数学基础

<details><summary>I 数学知识点汇总</summary>

![](数学基础/机器学习数学基础.png)

</details>

<details><summary>II 微积分</summary>

![](数学基础/微积分.png)

</details>

<details><summary>III 线性代数</summary>

![](数学基础/线性代数.png)

</details>

<details><summary>IV 概率论和统计学</summary>

- 统计数据的展示

	![](数学基础/图表建议.png)

- 概率与统计思维导图

    ![](数学基础/概率与统计.png)

- 基本概率分布

    ![](pic/分布表格.jpg)

</details>

<details><summary>V 最优化</summary>

</details>

## 二、Python/R/Octave语言

<details><summary>I Python语言</summary>

- [Python学习笔记](http://nbviewer.jupyter.org/github/yejinlei/about-python)
- Ananconda[配置](./tools/.condarc)及pip[配置](./tools/pip.ini)
- [Scikit-learn 0.21.x 中文文档](http://sklearn.apachecn.org)

</details>

<details><summary>II R语言</summary>

</details>

<details><summary>III Octave</summary>

- [octave online](https://octave-online.net/)

</details>

## 机器学习分类

<details><summary>I 有监督学习</summary>

</details>

<details><summary>II 无监督学习</summary>

</details>

<details><summary>III 强化学习</summary>

</details> 

<details><summary>IV 深度学习</summary>

</details>

<details><summary>V 迁移学习</summary>

</details>

## 机器学习领域

<details><summary>I 图像处理领域</summary>

</details>

<details><summary>II 自然语言领域</summary>

</details>

<details><summary>III 语音识别领域</summary>

</details>

## 统计学习和机器学习

<details><summary>I 机器学习算法关系图</summary>

![](数学基础/统计机器学习.png)

</details>

<details><summary>II 机器学习思维导图</summary>

![](机器学习/有关机器学习.png)

</details>

## 深度学习

<details><summary>I 深度学习知识点汇总</summary>

![](深度学习/深度学习.png)

</details>

<details><summary>II 深度学习中的优化算法</summary>

![](深度学习/optimization/deep_optimization.gif)

</details>

## AutoML/AutoDL

<details><summary>AutoML/AutoDL流程图</summary>

![](自动机器学习/自动机器学习.png)

</details>

库、框架|核心组件及函数|使用与评估
---|---|---
[automl_gs](https://github.com/minimaxir/automl-gs)|[**automl_grid_search**网格搜索策略](https://github.com/minimaxir/automl-gs/automl_gs/blob/master/automl_gs.py)<br>step1:**get_problem_config**，从[评估指标模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/metrics.yml)中获取学习类型及指标<br>step2:**build_hp_grid函数**，使用[超参数模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/hyperparameters.yml)构建所有**超参数**<br>step3:**render_model函数**，在script目录下的[model模型模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/templates/scripts/model)和[pipeline函数模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/templates/scripts/pipeline)中填入超参数，生成可执行的脚本<br>step4:**train_generated_model函数**，训练模型<br>step5:显示结果|
[auto-sklearn](https://github.com/automl/auto-sklearn)、[文档](https://automl.github.io/auto-sklearn/master/)||

### 传统自动机器学习AutoML-autosklearn
- SMAC算法
- 扩展数据预处理
  1. autosklearn.pipeline.components.feature_preprocessing.add_preprocessor
- 扩展回归
  1. autosklearn.pipeline.components.regression.add_regressor
- 扩展分类
  1. autosklearn.pipeline.components.classification.add_classifier

## 参考资料
  
* 课程
* 开源项目
* 文章