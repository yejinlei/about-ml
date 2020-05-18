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

    ![](pic/分布表格.jpg)

</details>

<details><summary>最优化</summary>

</details>

## 二、Python/R/Octave语言

<details><summary>Python语言</summary>

- [Python学习笔记](http://nbviewer.jupyter.org/github/yejinlei/about-python)
- Ananconda[配置](./tools/.condarc)及pip[配置](./tools/pip.ini)
- [Scikit-learn 0.21.x 中文文档](http://sklearn.apachecn.org)

</details>

<details><summary>R语言</summary>

</details>

<details><summary>Octave</summary>

- [octave online](https://octave-online.net/)

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

## 统计学习和机器学习

<details><summary>机器学习算法关系图</summary>

![](数学基础/统计机器学习.png)

</details>

<details><summary>机器学习思维导图</summary>

![](机器学习/有关机器学习.png)

</details>

## 深度学习

<details><summary>深度学习知识点汇总</summary>

![](深度学习/深度学习.png)

</details>

<details><summary>深度学习中的优化算法</summary>

![](深度学习/optimization/deep_optimization.gif)

</details>

## AutoML/AutoDL

> AutoML as a CASH Problem
>>  **C**ombined **A**lgorithm **S**election and **H**yperparameter optimization

<details><summary>AutoML/AutoDL流程图</summary>

![](自动机器学习/自动机器学习.png)

</details>

库、框架|核心组件及函数|使用与评估
---|---|---
[automl_gs](https://github.com/minimaxir/automl-gs)|[**automl_grid_search**网格搜索策略](https://github.com/minimaxir/automl-gs/automl_gs/blob/master/automl_gs.py):<br>step1:**get_problem_config**，从[评估指标模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/metrics.yml)中获取学习类型及指标；<br>step2:**build_hp_grid函数**，使用[超参数模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/hyperparameters.yml)构建所有**超参数**；<br>step3:**render_model函数**，在script目录下的[model模型模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/templates/scripts/model)和[pipeline函数模板](https://github.com/minimaxir/automl-gs/blob/master/automl_gs/templates/scripts/pipeline)中填入超参数，生成可执行的脚本；<br>step4:**train_generated_model函数**，训练模型；<br>step5:显示结果|
[auto-sklearn](https://github.com/automl/auto-sklearn)、[文档](https://automl.github.io/auto-sklearn/master/)||
[h2o-3](https://github.com/h2oai/h2o-3)、[文档](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/index.html)|<details><summary>h2o on spark</summary>![](自动机器学习/h2o/H2O.png)</details><br>|

## 参考资料
  
- 文档
1. [scikit-learn (sklearn) 官方文档中文版](https://sklearn.apachecn.org/)
2. [H2O.ai文档](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/index.html)

- 论文
  - 元学习
    - [floodsung/Meta-Learning-Papers](https://github.com/floodsung/Meta-Learning-Papers)

- 文章
1. [An Overview of AutoML Libraries Used in Industry](https://www.shangyexinzhi.com/article/313707.html)
2. [自动机器学习：最近进展研究综述](https://www.leiphone.com/news/201908/cM4vkvgmXinZ1Cky.htmlhttps://baijiahao.baidu.com/s?id=1641540911794101828&wfr=spider&for=pc)
3. [机器学习平台建设](https://blog.csdn.net/SoftwareTeacher/article/details/82692184)