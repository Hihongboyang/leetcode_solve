# 编程题



## 约瑟夫环--剑指offer--45题

约瑟夫问题是个著名的问题：N个人围成一圈，第一个人从1开始报数，报M的将被杀掉，下一个人接着从1开始报。如此反复，最后剩下一个，求最后的胜利者。

相当于这样一个问题，10个人围城一圈，然后报数，报数为4（1，2，3，4）的人出列。第一轮中3，7都没了。下来接着转。

```
0 1 2 3 4 5 6 7 8 9

0 1 2   4 5 6   8 9
```

每次有人出列之后会有空位，使整个序列不连续，那怎么消除这个空位的影响呢？

办法就是剩下的人重新排列成新的序列。

```
原来 0 1 2 3 4 5 6 7 8 9
移除 0 1 2   4 5 6 7 8 9
重排 6 7 8   0 1 2 3 4 5
```

下来如何映射**重新排列的序列**和**原来的序列**的关系呢，或者说新的序列和原来序列的关系？

```
移除 0 1 2   4 5 6 7 8 9
                   ^
重排 6 7 8   0 1 2 3 4 5
                   ^
```

上面显示了下一个要出列的人的编号。如何从新序列的3推导出旧序列的7呢？新序列是由（旧序列中的编号 - 最大的报数4）% 旧序列总人数  得到的。所以逆推回去 **（新序列中的编号 +  最大的报数4）% 旧序列总人数 = 旧序列中的编号**。

也就是说在，原序列( sum ) 中第二次被扔入海中编号可以由新序列( sum - 1) 第一次扔海里的编号通过特定的逆推运算得出。

而新序列 (sum -1)也是（从0开始）连续的，它的第二次被扔入海中的编号由可以由（sum - 2）的第一次扔入海里的编号通过特定的逆推运算得出，并且它的第二次被扔入海中的编号又与原序列中的第三次被扔入海里的编号是有对应关系的。

(sum-2)环的第1次出环编号 >>>(sum-1)环的第2次出环编号 >>>(sum)环的第3次出环编号

即 在以 k 为出环报数值的约瑟夫环中， m人环中的第n次出环编号可以由 (m-1) 人环中的第 (n-1) 次出环编号通过特定运算推出。

幸运的是，第一次出环的编号是可以直接求出的，也就是说，对于任意次出环的编号，我们可以将之一直降到第一次出环的编号问题，再一  一 递推而出。

那么我们可以推导出递推公式为：
$$
(f(n-1, m) + m) \% n
$$
$f(n-1, m)$就是有n-1个人时报数m时最后剩下人的编号

写成代码就是

```python
def ysfgd(n, m):
    if n == 0:
        return 1
    if n == 1 :
        return 0
    else:
        return (ysfgd(n-1, m) + m) % n
```



## 剑指off--2题

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

![img](https://pic.leetcode-cn.com/39135ce30976f053a8f3b4db7b3756b1f77fd8be91341bbdd1ffc7d2403d137f-4-1.jpg)

```python
def findNumberIn2DArray(matrix, target):
    row_len = len(matrix)
    if row_len == 0:
        return False
    col_len = len(matrix[0])
    if row_len == 0:
        return False
    row = 0
    col = col_len - 1
    while row < row_len and col > -1:
        if target == matrix[row][col]:
            return True
        if target < matrix[row][col]:
            col -= 1
        else:
            row += 1
    return False 
        
```



## 剑指off--3题

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

思路有三种，1.暴力破解，挨个搜索，如果找到重复的就返回。这需要两个循环进行遍历。2.维护一个列表，当正在检查的值已经在列表当中，那就返回。3.对数组进行排序，然后比较相邻的两个元素是否相等。

```python
def findRepeatNumber(self, nums: List[int]) -> int:
    num_dict = dict()
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 0
        else:
            return num

```



```python
def findRepeatNumber(self, nums: List[int]) -> int:
    nums.sort()
    pre = nums[0]
    for i in range(1, len(nums)):
    	if pre == nums[i]:
    	return pre
    pre = nums[i]
```



## 剑指off--10题

斐波那契数列，给出动态规划的证明

动态规划解析：
状态定义： 设 $dp$ 为一维数组，其中 $dp[i]$ 的值代表 斐波那契数列第 i 个数字 。
转移方程： $dp[i + 1] = dp[i] + dp[i - 1]$ ，即对应数列定义 $f(n + 1) = f(n) + f(n - 1)$；
初始状态： $dp[0] = 0, dp[1] = 1$ ，即初始化前两个数字；
返回值： $dp[n]$ ，即斐波那契数列的第 $n$ 个数字。
空间复杂度优化：
若新建长度为 $n$ 的 $dp$ 列表，则空间复杂度为 $O(N)$ 。

由于 $dp$ 列表第 $i$ 项只与第$i−1$ 和第$i−2$ 项有关，因此只需要初始化三个整形变量 $sum, a, b $，利用辅助变量 $sum$ 使 $a, b$ 两数字交替前进即可 （具体实现见代码） 。
节省了 $dp$ 列表空间，因此空间复杂度降至 $O(1)$ 。
循环求余法：
大数越界： 随着 $n$ 增大, $f(n)$会超过 Int32 甚至 Int64 的取值范围，导致最终的返回值错误。

求余运算规则： 设正整数 x, y, p ，求余符号为$ ⊙$ ，则有 $(x + y) \odot p = (x \odot p + y \odot p) \odot p$ 。
解析： 根据以上规则，可推出 $f(n) \odot p = [f(n-1) \odot p + f(n-2) \odot p] \odot p$ ，从而可以在循环过程中每次计算 $sum = (a + b) \odot 1000000007$ ，此操作与最终返回前取余等价。

![Picture0.png](https://pic.leetcode-cn.com/25e913ab8d7a22bb017669e4a097cf51d10861f365002f2d8556ee7a64464cd8-Picture0.png)



## 剑指off--10题--第二问：青蛙跳台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 `n` 级的台阶总共有多少种跳法。



我看了解析，说，类似求多少种可能性的题目  都会有**递推性质**。那么这个问题，是怎么获得这个递推性质的？

假设跳上n级台阶有$f(n)$种跳法。在所有跳法种，青蛙的最后一步只用两种可能：跳上1级或者2级台阶。

1. 当为1级台阶时：剩n-1个台阶，这种情况共有$f(n-1)$种跳法
2. 当为2级台阶时：剩n-2个台阶，这种情况共有$f(n-2)$种跳法

$f(n)$为以上两种情况之和，即$f(n) = f(n-1) + f(n-2)$，以上这个递推性质是斐波那契数列，所以可以转为斐波那契数列第n项值。唯一的区别是起始数字的不同。

青蛙跳台阶：$f(0) = 1, f(1) = 1, f(2) = 2$

斐波那契数列：$f(0) = 0, f(1) = 1, f(2) = 1$

回头看这个问题，正常思路我们是从开始向最后推导，这个题的思路从后向前推导。



## 剑指off--7题 构建二叉树

使用前序遍历和中序遍历来构建二叉树。

想要构建二叉树，必须使用前序遍历+中序遍历，或者后续遍历+中序遍历。前序+后序的方式无法构建二叉树。

构建的重点在于根据前序来确定根节点在中序遍历的位置，再通过中序遍历来确定左子树和右子树的节点是哪些。

```
[3,9,20,15,7] 前序
 ^
[9,3,15,20,7] 中序
   ^              通过中序遍历我们可以知道，左子树有几个节点，这里是1个，而根节点的位置为1，可以根据这个位置确定前序遍历中左子树位置
```



```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder)
    if not preorder:
        return None

    root_index = inorder.index(preorder[0])  # 确定根节点位置
    root = TreeNode(preorder[0])
    root.left = buildTree(preorder[1:root_index+1], inorder[:root_index]) # 从根节点确定左右子树
    root.right = buildTree(preorder[root_index+1:], inorder[root_index+1:])

    return root
```



## 剑指off--15题 二进制中的1

请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

查看一个整型的二进制表示中有几个1。第一个想到的是使用位运算，并且使用移位的操作，但是使用移位的操作又怎么统计1的个数呢？

```python
 def hammingWeight( n: int) -> int:
     res = 0
     while n:
     	res += n & 1  # 与1进行和操作，如果是同为1怎总数加1
     	n >>= 1  # 将数字右移一位
     return res
```

这种方法，基本上是要将每一位都要统计到。4个字节的整形，要统计32次。

看到大神的解法

使用n与n-1进行和运算。对n-1后原本是1的位置的后面会全部变为1，再进行和运算，后面的位全部变为0.只剩下还没有计算的1.

每一次减去1，都会消除原来位置的一个1（暂且这样理解），当n变为0时统计就结束了



![Picture10.png](https://pic.leetcode-cn.com/d9e67ba987e7f9368690b4bf1079e6bbfa87646c62a0d73048aa3d50a0c9c8e9-Picture10.png)

```python

def hammingWeight(n: int) -> int:
    res = 0
    while n:  # 只需按照有几个1进行统计即可
    	res += 1
    	n &= n - 1  # 消除一个1
    return res

```



## **剑指off--30题 包含min的栈**

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

如果使用普通的搜索算法来查找栈中的元素，找到最小的元素再返回，这不符合复杂度为O(1)的要求。

使用另一个栈B，然这个栈中存储正常栈A中非降序的数字。

针对push函数:

将x压入栈A中。

若B栈为空，或者x小于B栈顶的元素，则将x压入B栈中

pop函数：

对A执行出栈

若x等于B栈顶的元素，则对B执行出栈操作。

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_stack = list()
        self.data_temp = list()

    def push(self, x: int) -> None:
        self.data_stack.append(x)
        if x < self.top():
            self.data_temp.append(x)

    def pop(self) -> None:
        temp = self.data_stack.pop(-1)
        if temp == self.data_temp[-1]:
            self.data_temp.pop(-1)

    def top(self) -> int:
        return self.data_stack[-1]

    def min(self) -> int:
        return self.data_temp[-1]
```



## 剑指off--42题：连续子数组的最大和

给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

```
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```



```python
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
     """
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
    return max(nums)
```

`nums[i-1]`并不是数组前一项的意思，而是到前一项为止的最大子序和，和0比较是因为只要大于0，就可以相加构造最大子序和。如果小于0则相加为0，`nums[i]=nums[i]`，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和。

------

一些思考：要求求所有子数组的和值，这种组合方式是非常多的，必然不能使用穷举的方式进行解答。而从头到尾对数组进行遍历的过程可以看成是一个从头到尾选取子数组的过程。

```python
def maxSubArray(nums):
    if len(nums) == 0:
        return 0
    ans = nums[0]
    temp = 0
    for num in nums:
        if temp > 0:
            temp += num
        else:
            temp = num
        if temp > ans:
            ans = temp
    return ans
```













