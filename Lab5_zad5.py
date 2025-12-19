import pandas as pd

data = {
    'nr_albumu': [1, 2, 3, 4, 5],
    'imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'wiek': [22, 21, 24, 23, 25]
}

df = pd.DataFrame(data)
studenci_plus_4 = df[df['ocena'] > 4]
df_sorted = df.sort_values(by='wiek')
srednia_wieku_grupy = df.groupby('ocena')['wiek'].mean()
poprawa_data = {
    'nr_albumu': [2, 5],
    'ocena_poprawa': [4.0, 3.5]
}
df_poprawa = pd.DataFrame(poprawa_data)
df_final = pd.merge(df, df_poprawa, on='nr_albumu', how='left')
df_final.to_csv('studenci.csv', index=False)
df_wczytany = pd.read_csv('studenci.csv')
print("Nagłówek wczytanych danych:")
print(df_wczytany.head())
nowy_student = {'nr_albumu': 6, 'imię': 'Ewa', 'nazwisko': 'Lis', 'ocena': 4.0, 'wiek': 22}
df = pd.concat([df, pd.DataFrame([nowy_student])], ignore_index=True)
unikalne_oceny = df['ocena'].unique()
liczba_piatek = len(df[df['ocena'] == 5.0])
print(f"\nLiczba studentów z oceną 5: {liczba_piatek}")
print(f"Unikalne oceny: {unikalne_oceny}")