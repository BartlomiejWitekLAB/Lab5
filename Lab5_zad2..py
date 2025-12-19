import pandas as pd
df = pd.read_csv('demografia.csv', na_values='.')
df['KRAJE'] = df['KRAJE'].str.strip()
df.set_index('KRAJE', inplace=True)
najwiekszy_przyrost_kraj = df['2022'].idxmax()
najwiekszy_przyrost_wartosc = df['2022'].max()

print(f"Największy przyrost w 2022 r.: {najwiekszy_przyrost_kraj} ({najwiekszy_przyrost_wartosc})")