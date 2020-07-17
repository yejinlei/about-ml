# about-ml 有关机器学习

----------

## 一、数学基础

<details><summary>数学知识点汇总</summary>

![](数学基础/机器学习数学基础.png)

</details>

<details><summary>微积分</summary>

![](数学基础/微积分.png)

</details>

<details><summary>线性代数</summary>

![](数学基础/线性代数.png)

</details>

<details><summary>概率论和统计学</summary>

- 统计数据的展示

	![](数学基础/图表建议.png)

- 概率与统计思维导图

    ![](数学基础/概率与统计.png)

- 基本概率分布

    ![](数学基础/incredibly_detailed_map_of_all_univariate_distributions.png)<br>[Univariate Distribution Relationships](http://www.math.wm.edu/~leemis/chart/UDR/UDR.html)

</details>

<details><summary>最优化</summary>

</details>

## 机器学习分类

<details><summary>有监督学习</summary>

</details>

<details><summary>无监督学习</summary>

</details>

<details><summary>强化学习</summary>

</details> 

<details><summary>深度学习</summary>

</details>

<details><summary>迁移学习</summary>

</details>

</details>

<details><summary>元学习</summary>

</details>


## 机器学习领域

<details><summary>图像处理领域</summary>

</details>

<details><summary>自然语言领域</summary>

</details>

<details><summary>语音识别领域</summary>

</details>

## 机器学习ML

<details><summary>机器学习算法关系图</summary>

![](数学基础/统计机器学习.png)

</details>

<details><summary>机器学习思维导图</summary>

![](机器学习/有关机器学习.png)

</details>

## 深度学习DL

<details><summary>深度学习知识点汇总</summary>

![](深度学习/深度学习.png)

</details>

<details><summary>深度学习中的优化算法</summary>

![](深度学习/optimization/deep_optimization.gif)

</details>

## 自动化学习AutoML/AutoDL

1. > **AutoML as a CASH Problem**
    >>  **C**ombined **A**lgorithm **S**election and **H**yperparameter optimization

    <details><summary>AutoML/AutoDL思维导图</summary>

      ![](自动机器学习/自动机器学习.png)
  
    </details>

2. **自动化流程**
   1. 自动数据清洗
   2. 自动特征工程
   3. 自动数据建模
      1. 自动算法/模型选择
      2. 自动超参数优化
         - 网格搜索(Gird Search)
         - 随机搜索(Random Search)
         - 贝叶斯优化(Bayesian Optimization)
   4. 自动模型评估
      1. 模型度量
      2. 模型解释

3. **开源库评估**

  库、框架|核心组件及函数|使用与评估
  ---|---|---
  [automl_gs's github](https://github.com/minimaxir/automl-gs)、[tutorial](https://github.com/minimaxir/automl-gs/blob/master/docs/automl_gs_tutorial.ipynb)、[exampes](https://github.com/minimaxir/automl-gs-examples)|[**automl_grid_search**网格搜索策略](https://github.com/minimaxir/automl-gs/automl_gs/blob/master/automl_gs.py):<br>step1:**get_problem_config**，从[评估指标模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/metrics.yml)中获取学习类型及指标；<br>step2:**build_hp_grid函数**，使用[超参数模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/hyperparameters.yml)构建所有**超参数**；<br>step3:**render_model函数**，在script目录下的[model模型模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/templates/scripts/model)和[pipeline函数模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/templates/scripts/pipeline)中填入超参数，生成可执行的脚本；<br>step4:**train_generated_model函数**，训练模型；<br>step5:显示结果|
  [auto-sklearn's github](https://github.com/automl/auto-sklearn)、[文档](https://automl.github.io/auto-sklearn/master/)||
  [h2o-3's github](https://github.com/h2oai/h2o-3)、[文档](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/index.html)|<details><summary>h2o on spark</summary>![](自动机器学习/h2o/H2O.png)</details><br>|

## 参考资料
  
- 文档
  - 
  - [scikit-learn (sklearn) 官方文档中文版](https://sklearn.apachecn.org/)
  - [H2O.ai文档](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/index.html)

- 论文
  - 元学习
    - [floodsung/Meta-Learning-Papers](https://github.com/floodsung/Meta-Learning-Papers)

- 文章
  - [An Overview of AutoML Libraries Used in Industry](https://www.shangyexinzhi.com/article/313707.html)
  - [自动机器学习：最近进展研究综述](https://www.leiphone.com/news/201908/cM4vkvgmXinZ1Cky.htmlhttps://baijiahao.baidu.com/s?id=1641540911794101828&wfr=spider&for=pc)
  - [机器学习平台建设](https://blog.csdn.net/SoftwareTeacher/article/details/82692184)
  - [使用 Hyperopt 进行参数调优（译）](https://www.jianshu.com/p/35eed1567463)