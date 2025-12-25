import pandas as pd

df = pd.read_csv('demografia.csv', na_values='.')
df['KRAJE'] = df['KRAJE'].str.strip()
df.set_index('KRAJE', inplace=True)
df.columns = df.columns.str.replace('a', '')
max_w_roku = df.max()
szukany_rok = max_w_roku.idxmax()
szukany_kraj = df[szukany_rok].idxmax()
najwieksza_wartosc = df.loc[szukany_kraj, szukany_rok]
print(f"Największy przyrost ludności: {najwieksza_wartosc}")
print(f"Kraj: {szukany_kraj}")
print(f"Rok: {szukany_rok}")