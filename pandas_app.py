import pandas as pd

# var_name = ['Sharique','Nargis','Sufiyan']
# var_age = [30,23,1]
# data_frame_work = {
#     'name':var_name,
#     'Age':var_age
# }

#? To convert data into table
# my_table = pd.DataFrame(data_frame_work, index=['person 1','person 2','person 3']) 
# print(my_table)

#? To read a row
# print(my_table.loc[[0,1,2]])
# print(my_table.loc['person 1'])

#? read csv file
# df = pd.read_csv('first.csv')
# print(df)
# print(df.to_string()) 

# data = df.to_string()

# df = pd.read_csv('data.csv')
# print(df.mean())
# print(df.median())
# print(df.mode())


df = pd.read_csv('data.csv')
# print(df.to_string())
# print(df.head(10))
# print(df.tail(10))
print(df.info())



