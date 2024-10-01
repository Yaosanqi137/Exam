import pandas as pd

if __name__ == "__main__":
    df = pd.read_excel('ExcelOutput/marks.xlsx', sheet_name='Sheet1')
    name, exam1, score1, exam2, score2, exam3, score3, total, totalScore = [], [], [], [], [], [], [], [], []
    for i in range(0, len(df), 3): # 录入数据
        name.append(df['名字'][i])
        exam1.append(df['考试项目'][i])
        exam2.append(df['考试项目'][i + 1])
        exam3.append(df['考试项目'][i + 2])
        score1.append(df['分数'][i])
        score2.append(df['分数'][i + 1])
        score3.append(df['分数'][i + 2])
        total.append('加权总分')
        totalScore.append((score1[-1] + score2[-1] * 2 + score3[-1] * 2) / 5)

    finalData = { # 打包成字典
        'name': name,
        'exam1': exam1,
        'score1': score1,
        'exam2': exam2,
        'score2': score2,
        'exam3': exam3,
        'score3': score3,
        'total': total,
        'totalScore': totalScore
    }

    df = pd.DataFrame(finalData) # 将字典输出为excel
    df.to_excel('ExcelOutput/finalData.xlsx', index=False, header=False)