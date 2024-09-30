# 看上去感觉像是归并排序的最坏情况 O(nlogn) 或者冒泡的最坏情况 O(n^2)，这两种排序方式都是两两比较
# 考虑到要“最大”，所以这里使用冒泡的最坏情况
# 冒泡排序:
# 假设有 n 个数据等待排序，那么排序程序将从第一个数据开始往后比较
# 将第 a 个数据和第 a + 1 个数据进行大小比较(也就是本题中的称量书本的动作)，然后将最大的那个数放在两者之前，之后以此类推着进行
# 最终，数据中最大的数字就会像水中的泡泡浮到最后一位
# 此时只有 n - 1 个数据等待排序了，最后全部故技重施即可完成排序
# 那么显然这个步数的总和就是一个简单的等差数列求和，即: n * (n - 1) / 2

def maxTimes(n):
    print(int(n * (n - 1) / 2))

if __name__ == '__main__':
    bookAmount = int(input())
    maxTimes(bookAmount)