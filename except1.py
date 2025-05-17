import pandas as pd
from pandas.errors import EmptyDataError

class Processing:

    def __init__(self, name, name2, name3): 
        self.name = name
        self.name2 = name2
        self.name3 = name3
     
    def data(self): #Отсутствие файла

        try:
            pd.read_csv(self.name3)
        except FileNotFoundError as e:
            print(f"возникла следующая ошибка:{e}")

    def open(self): # Пустой файл
        
        try:
            pd.read_csv(self.name2)
        except EmptyDataError:
            print(f"Возникла сдующая ошибка: Датафрейм {self.name2} пуст")

    def false(self):

        df1 = pd.read_csv('var3.csv')
        df2 = pd.read_csv('var.csv')
        res1 = list(df1.columns)
        res2 = list(df2.columns)


        if res1 == res2:
            print("Чтение датафрейма завершено успешно.") 
        else:
            print("Структура датафрейма НЕ соответствует ожидаемой:")

            try:
                res1 == res2
            except:
                print(f"-Названия столбцов НЕ совпадают")
                print(f"Ожидаемые:{res1}")
                print(f"фактический:{res2}")
            
            common_columns = df1.columns.intersection(df2.columns)# Определяем общие колонки

            for col in common_columns:
                dtype1 = df1[col].dtype
                dtype2 = df2[col].dtype
                print(f"- В столбце {col} тип дфнных не соответствует ожидаемому.")
                print(f"Ожидается: {dtype1}, Фактически: {dtype2}")

            print("Чтение датафрейма завершено успешно.")    
def main():

    file_path = "var3.csv"
    file_path2 = "var2.csv"
    file_path3 = "var4.csv"
    processor = Processing(file_path, file_path2, file_path3)
    processor.data()
    processor.open()
    processor.false()

if __name__ == "__main__":
    main()