# 有关TensorFlow #

![](深度学习/tensors_flowing.gif)

## 概念 ##
- **Graph**，Tensorflow的数据流图是由节点和边组成的无向环图DAG；
- **Node**，节点又称算子，代表一个操作；
- **Tensor**，张量即数据，由数据流图中的边来表示；
- **Variables**，变量是一种特殊的数据，它有固定的位置不像Tensor在图中流动；
- **Feed和Fetch**，在执行图时，传入一些Tensor，这个过程叫feed；返回的结果类型根据输入的类型而定，这个过程叫fetch；
- **Session**，图执行的过程，一个会话可能有多个图，会话可以修改图的结构，也可以往图中注入数据进行计算；

## 步骤 ##
