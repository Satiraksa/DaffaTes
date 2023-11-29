#SOAL NO 2
import pandas as pd 

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

#pertanyaan 1
df['Status'] = df['Usia'].apply(lambda x: 'Muda' if x < 30 else 'Tua')

#pertanyaan 2
df['Total_Gaji'] = df.apply(lambda row: row['Gaji'] * 1.1 if row['Status'] == 'Tua' else row['Gaji'] * 1.05, axis = 1)

#pertanyaan 4
df['Gaji_Ganda'] = df.apply(lambda row: row['Gaji'] * 2 if row['Usia'] > 30 else row['Gaji'], axis = 1)

#pertanyaan 3
print(df)