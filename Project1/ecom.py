import pandas as pd


filepath = './dataset/Ecommerce_Purchases.csv'
data = pd.read_csv(filepath)

# Display top 10 rows of the dataset
print(data.head(10))

# Display last 10 rows of the dataset
print(data.tail(10))

# Check a data type of columns
print(data.dtypes)
print(data["Address"].dtypes)

# check the column
print(data.columns)

# check null values
print(data.isnull())

# how many rows and column are there in our dataset
print(data.shape)

# no. of rows
print(len(data))
# no. of columns
print(len(data.columns))

# highest and lowest purchase price
print(data['Purchase Price'].max())
print(data["Purchase Price"].min())

# Avg purchase price 
print(data['Purchase Price'].mean())

# How many people have french 'fr' as their lang
print(data[data['Language'] == 'fr'].count())

# Job Title contain engineer
print(len(data[data["Job"].str.contains('engineer',case=False)]))

#  Find email of the person with the following ip address 132.207.160.22
print(data[data['IP Address']== '132.207.160.22']['Email'])

# How many people have mastercard as their credit card provider and made a purchase above 50
print(len(data[(data['CC Provider'] == 'Mastercard') & (data['Purchase Price']>50)]))

# Find email of the person with following credit card number 4664825258997302
print(data[data['Credit Card']== 4664825258997302 ]['Email'])

# How many people purchase during the am and how many people purchase during pm
print(data["AM or PM"].value_counts())

#How many people have a credit card that expires in 2020
print(len(data[data["CC Exp Date"].apply(lambda x:x[3:] =='20')]))


# Top 5 most popular email provider(eg. gmail.com, yahoo.com,etc)
list1=[]
for email in data['Email']:
    list1.append(email.split('@')[1])
data['temp'] = list1
print(data['temp'].value_counts().head()) 

print(data['Email'].apply(lambda x:x.split('@')[1]).value_counts().head())










