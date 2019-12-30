# GN算法实现
## 实验环境
- Windows 10 企业版
- Python 3.7.4
## 使用的包
1. [NetworkX](https://networkx.github.io/)<br>
用来解析数据得到图<br>
2. [Matplotlib]()<br>
用来画出图<br>
## 代码说明
1. main.py<br>
算法实现的部分
2. file_io.py<br>
负责文件的读取和写入
3. draw_nx.py<br>
负责把结果画出来，用的是NetworkX内的画图API
4. gml.py<br>
把结果文件导出成gml格式
## 文件内容
Data文件夹按照每个测试例子各自一个文件夹，每个文件夹的文件如下：<br>

- nodes.csv 图上的节点
- edge.csv 图上的边的集合
- result.txt 算法结果，每行一个社区
- recode.txt 算法运行过程中目标函数值的记录
- graph.gml 图的GML文件，本来要在Netdraw里面画图的，但是找了半天没找到怎么导入自己的社区
## 数据集来源
- simple<br>
就是上课的时候的那个简单的样例，用来DEBUG
- karate<br>
Zachary 网络是通过对一个美国大学空手道俱乐部进行观测而构建出的一个社会网络。网络包含 34 个节点和 78 条边，其中个体表示俱乐部中的成员，而边表示成员之间存在的友谊关系。[源地址](http://www-personal.umich.edu/~mejn/netdata/karate.zip)
- football<br>
College Football 网络 Newman 根据美国大学生足球联赛而创建的一个复杂的社会网络。该网络包含 115个节点和 616 条边,其中网络中的结点代表足球队，两个结点之间的边表示两只球队之间进行过一场比赛。参赛的115支大学生代表队被分为12个联盟。比赛的流程是联盟内部的球队先进行小组赛,然后再是联盟之间球队的比赛。这表明联盟内部的球队之间进行的比赛次数多于联盟之间的球队之间进行的比赛的次数。联盟即可表示为该网络的真实社区结构。[源地址](http://www-personal.umich.edu/~mejn/netdata/football.zip)
- dolphins<br>
Dolphin 数据集是 D.Lusseau 等人使用长达7年的时间观察新西兰Doubtful Sound海峡62只海豚群体的交流情况而得到的海豚社会关系网络。这个网络具有62个节点，159条边。节点表示海豚，而边表示海豚间的频繁接触。[源地址](http://www-personal.umich.edu/~mejn/netdata/dolphins.zip)<br>
- PS: 之前还找了更大的数据集，但是电脑内存不够，没跑出来
## 结果的图的样例
统一社区采用相同颜色，图上的样例是上课的时候的样例<br>
![Figure_1](./Figure_1.png)
