import pandas as pd

######## loading the dataset
data = pd.read_csv('./dataset/pokemon-data.csv',sep=';')
df = pd.DataFrame(data)


####### transforming the data
def clean_str(str1):
    l1=eval(str1)
    s2=",".join(l1)
    return s2


df[['Type1','Type2']] = df["Types"].apply(lambda x : clean_str(x)).str.split(',',expand=True)
df[['Abilities1','Abilities2', 'Abilities3', 'Abilities4']]=df['Abilities'].apply(lambda x: clean_str(x)).str.split(",", expand=True)


df = df.drop(columns=["Types","Abilities"],axis=0)


df['HP'] = df['HP'].astype(int)

df['Attack'] = df['Attack'].astype(int)

df['Defense'] = df['Defense'].astype(int)

df['Special Attack'] = df['Special Attack'].astype(int)

df['Special Defense'] = df['Special Defense'].astype(int)

df['Speed'] = df['Speed'].astype(int)


## Exporting to csv
# df.head(100).to_csv('./dataset/output_data.csv')
# print("Data Exported Success")

###### loading to sqlite database

from db_queries import trigger_insertion
trigger_insertion(data_f=df)