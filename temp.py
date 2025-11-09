import pandas as pd
import chardet 

with open('2023 second.csv', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(f"检测到的编码是：{encoding}")
    
df1 = pd.read_csv("2023 second.csv", encoding='gbk')
df2 = pd.read_csv("n_movies.csv", encoding='gbk')

df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

merged_df = pd.merge(df1, df2, on="Title", how="inner")

merged_df.to_csv("merged_common_titles_1.csv", index=False)

