import pandas as pd

df1 = pd.read_csv('var3.csv')
df2 = pd.read_csv('var.csv')

res1 = df1.columns
res2 = df2.columns

try:
    res1 == res2
except:
    print(f"названия столбцов НЕ совпадают")
    print(f"Ожидаемые:{res1}")
    print(f"Ожидаемые:{res2}")
    
for i in res1:
    data1 = pd.read_csv("var3.csv", index_col ="i" )
    data2 =pd.read_csv("var.csv", index_col ="i" )

    try:
        type(data1) == type(data2)
    except ValueError:
        print(f"в столбце {res2[i]} типо данных не соответствует ожидаемому")
        print(f"ожидается: {type(data1)}, фактически: {type(data2)}")