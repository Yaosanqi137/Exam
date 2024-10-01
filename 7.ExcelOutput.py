import random
import pandas as pd
from faker import Faker

def ranScore(minScore, maxScore):
    Score = int(random.gauss(70, 10)) # 用高斯随机数函数生成分数，数据更加真实
    if minScore <= Score <= maxScore : # 限制随机数的范围
        return Score
    else:
        return ranScore(minScore, maxScore)

if __name__ == "__main__":
    lang = Faker(locale='zh_CN')
    amount = int(input()) # 请问想要生成几个人的数据呢?
    name, exam, score = [], [], []

    for n in range(amount): # 给每个学生取名、设置考试项目、生成考试分数
        fakeName = lang.name()
        name += [fakeName] * 3
        exam += ['一面', '国庆题', '二面']
        score += [ranScore(1, 100), ranScore(1, 100), ranScore(1, 100)]

    students = { # 生成一个字典来存储这些信息
        '名字': name,
        '考试项目': exam,
        '分数': score
    }

    df = pd.DataFrame(students) # 将字典导出为excel
    df.to_excel('ExcelOutput/marks.xlsx', index=False)

