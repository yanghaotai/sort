'''
冒泡排序
原理
冒泡排序(Bubble Sort)是一种简单的排序算法。
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

步骤
冒泡排序算法的运作如下：
1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

'''

# def bubble_sort(list):
#     length = len(list)
#     # 第一级遍历
#     for index in range(length):
#         # 第二级遍历
#         for j in range(1, length - index):
#             if list[j - 1] > list[j]:
#                 # 交换两者数据，这里没用temp是因为python 特性元组。
#                 list[j - 1], list[j] = list[j], list[j - 1]
#     return list

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
        print(array)
    return array



'''

选择排序
原理
选择排序（Selection sort）是一种简单直观的排序算法。
它的工作原理大致是将后面的元素最小元素一个个取出然后按顺序放置。

步骤
1.在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3.重复第二步，直到所有元素均排序完毕。

'''


# def selection_sort(list):
#     n=len(list)
#     for i in range(0,n):
#        min = i
#        for j in range(i+1,n):
#            if list[j]<list[min]:
#                min=j
#        list[min],list[i]=list[i],list[min]
#        print(list)
#     return list

def select_sort(array):
    for i in range(len(array)):
        x = i  # min index
        for j in range(i+1, len(array)):
            if array[j] < array[x]:
                x = j
        array[i], array[x] = array[x], array[i]
        print(array)
    return array

'''
插入排序
原理
插入排序（Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

步骤
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5

'''

def insert_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
        print(array)
    return array

'''
希尔排序
原理
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。
希尔排序是非稳定排序算法。
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。


步骤
每次以一定步长(就是跳过等距的数)进行排序，直至步长为1.

'''

def shell_sort(array):
    gap = len(array)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
            print(array)
    return array

'''
快速排序
原理
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

步骤
1.从数列中挑出一个元素，称为”基准”（pivot），
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
  在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

'''

def quick_sort(array):
    def recursive(begin, end):
        if begin > end:
            return
        l, r = begin, end
        pivot = array[l]
        while l < r:
            while l < r and array[r] > pivot:
                r -= 1
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]
        recursive(begin, l - 1)
        recursive(r + 1, end)

    recursive(0, len(array) - 1)
    return array

s1 = [10,13,9,5,12,15,7,3,1,14,4,8,2,6,11]
t1 = bubble_sort(s1)
print(t1)
print('..........')
s2 = [10,13,9,5,12,15,7,3,1,14,4,8,2,6,11]
t2 = select_sort(s2)
print(t2)
print('..........')
s3 = [10,13,9,5,12,15,7,3,1,14,4,8,2,6,11]
t3 = insert_sort(s3)
print(t3)
print('..........')
s4 = [10,13,9,5,12,15,7,3,1,14,4,8,2,6,11]
t4 = shell_sort(s4)
print(t4)
print('..........')
s5 = [10,13,9,5,12,15,7,3,1,14,4,8,2,6,11]
t5= quick_sort(s5)
print(t5)


