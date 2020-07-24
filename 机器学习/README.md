# 统计学习&机器学习

1. **机器学习**是通过编程让计算机从数据中进行学习的科学（和艺术） ♨
2. **机器学习**是让计算机具有学习的能力，无需进行明确编程。 —— 亚瑟·萨缪尔，1959 ♨
3. **机器学习**是计算机程序利用经验 E 学习任务 T，性能是 P，如果针对任务 T 的性能 P 随着经验 E 不断增长，则称为机器学习。 —— 汤姆·米切尔，1997 ♨

![](./有关机器学习.png)

---

## 统计学习

## 其他
- 机器学习的主要步骤

  - 特征工程
    - 数据清洗
      - 缺失值
      - 数据类型
      - 异常值
      - 文本编码
      - 数据分割
    - 特征提取（**数据类型**）
      -  数值衍生特征
      -  离散特征
      -  文本特征
      -  时序特征
      -  交叉特征
    - 特征选择、降维
      - 线性投影
      - 非线性投影
      - 特征筛选
    - 模型选择、训练
      - 模型选择
      - 参数选择
      - 模型训练

- 机器学习的**模型**
    - 监督学习（**任务类型**）
      -   K近邻算法(sklearn.neighbors.KNeighborsRegressor)
      - 线性回归(sklearn.linear_model.LinearRegression)
      - 逻辑回归
        -   支持向量机（SVM）
        -   决策树和随机森林
        - 神经网络
    -   半监督学习
    -   无监督学习
        -   聚类
            -   K均值
            -   层次聚类分析
            -   期望最大值
        -   降维
            -   主成分分析
            -   核主成分分析
            -   局部线性嵌入
            -   t-分布邻域嵌入算法
        -   关联性规则学习
            -   Apriori 算法
            -   Eclat 算法
    -   强化学习
    -   主动学习
    -   元学习
    -   离线学习
    -   在线学习

- 机器学习步骤
  - 交叉检验
  - 性能指标
    -   均方根误差（RMSE，通常用于回归任务）
    -   平均绝对误差（MAE）

  ## 参考资料
  1. [An Introduction to Statistical Learning with Applications in R](http://faculty.marshall.usc.edu/gareth-james/ISL/) 官网
  2. [统计学习导论-基于R应用](https://share.weiyun.com/GPwQUUXy) 书籍
  3. [《统计学习导论》R语言代码整理](https://blog.csdn.net/weixin_43761124/article/details/103666458?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param) 代码片段、思维导图
  4. [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/) 官网
  5. [ESL CN](https://esl.hohoweiya.xyz/index.html) 笔记
  6. [统计学习基础](https://share.weiyun.com/iQe5kDa3) 书籍
  7. [应用统计学与R语言实现学习笔记](https://giserdaishaoqing.gitbooks.io/note-of-applied-statistics-with-r-book/content/) 笔记
  8. [《统计学习方法》的代码实现](https://github.com/fengdu78/lihang-code) 笔记
  9. [《统计学习方法：李航》笔记 从原理到实现 基于R](https://github.com/DefTruth/statistic-learning-R-note) 笔记
  10. [CS229T/STATS231: Statistical Learning Theory](http://web.stanford.edu/class/cs229t/) 官网，[讲义](https://web.stanford.edu/class/cs229t/notes.pdf)
  11. [CS229 课程讲义中文翻译](https://kivy-cn.github.io/Stanford-CS-229-CN/#/) 讲义
  12. [YC-Coder-Chen/feature-engineering-handbook](https://nbviewer.jupyter.org/github/YC-Coder-Chen/feature-engineering-handbook/tree/master/%E4%B8%AD%E6%96%87%E7%89%88/) 代码片段