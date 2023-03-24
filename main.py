import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("List of languages by total number of speakers.csv")#считали данные
data.drop('Unnamed: 0', axis=1, inplace=True)#удалили 1 столбик

sns.countplot(data=data, x='Family')#столбчатая диаграмма
plt.title("Количество семейств языков")
plt.xticks(rotation=90)#повернули подписи по оси х на 90 градусов
plt.show()

data.Branch.value_counts().plot(kind='pie', figsize=(18,10),autopct='%0.1f%%')#По стобику Branch строим пироговую диаграмму
plt.title("Наиболее частые семейства языков")
plt.ylabel('')
plt.show()


toplanguages = data[['Language', 'Total speakers(L1+L2)']].copy()#создаем копию данных, чтобы по ним посторить график
toplanguages["Total speakers(L1+L2)"] = toplanguages["Total speakers(L1+L2)"].replace({"billion":"*1e9", "million":"*1e6"}, regex=True).map(pd.eval).astype(int)#заменяем текстовые названия величин на числа типа инт
top_speakers = toplanguages.head(20)#берем первые 20 значений
#Stash
plt.figure(figsize=(18,12))
graph=sns.barplot(y='Total speakers(L1+L2)',x='Language',data=top_speakers, color="Purple")#строим столбчатую диаграмму из библиотеки seaborn
graph.set_title('Топ 20 языков по количествуууууу носителей')
plt.xticks(rotation=90)
plt.show()

data['First-language(L1) speakers'] = data['First-language(L1) speakers'].str.replace('\[a\]', '')#при наличии значения (Native Languages) удаляем ее значение
data['First-language(L1) speakers'] = data['First-language(L1) speakers'].str.replace('—', '0')#заменяем пустые значения на 0
data["First-language(L1) speakers"] = data["First-language(L1) speakers"].replace({"billion":"*1e9", "million":"*1e6"}, regex=True).map(pd.eval).astype(int)#заменяем текстовые названия величин на числа типа инт
topfirstlanguage = data[['Language', 'First-language(L1) speakers']].copy()#создаем копию данных, чтобы по ним посторить график
topfirstlanguage=topfirstlanguage.head(5)#берем первые 5 значений

plt.figure(figsize=(18,12))
graph=sns.barplot(y='First-language(L1) speakers',x='Language',data=topfirstlanguage, color="Green")
graph.set_title('Топ 5 первых языков')
plt.xticks(rotation=90)
plt.show()

data['Second-language(L2) speakers'] = data['Second-language(L2) speakers'].str.replace('\[\d+\]', '')#при наличии численного значения (Neighboring Language) удаляем их значение
data['Second-language(L2) speakers'] = data['Second-language(L2) speakers'].str.replace('—', '0')#заменяем пустые значения на 0
data["Second-language(L2) speakers"] = data["Second-language(L2) speakers"].replace({"billion":"*1e9", "million":"*1e6"}, regex=True).map(pd.eval).astype(int)#заменяем текстовые названия величин на числа типа инт
topsecondlanguage = data[['Language', 'Second-language(L2) speakers']].copy()#создаем копию данных, чтобы по ним посторить график
topsecondlanguage=topsecondlanguage.head(5)#берем первые 5 значений

plt.figure(figsize=(18,12))
graph=sns.barplot(y='Second-language(L2) speakers',x='Language',data=topsecondlanguage, color="Black")#строим столбчатую диаграмму из библиотеки seaborn
graph.set_title('Топ 5 вторых языков')
plt.xticks(rotation=90)
plt.show()