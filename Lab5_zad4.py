import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
}

df = pd.DataFrame(data)
pensja_powyzej_5000 = df[df['Pensja'] > 5000]
df_posortowany = df.sort_values(by='Wiek')
srednia_pensja_stanowisko = df.groupby('Stanowisko')['Pensja'].mean()
nowe_stanowiska_data = {
    'ID': [2, 4],
    'Nowe_Stanowisko': ['Senior Programista', 'Lead Programista']
}
df_nowe = pd.DataFrame(nowe_stanowiska_data)
df_polaczony = pd.merge(df, df_nowe, on='ID', how='left')
df.to_csv('pracownicy.csv', index=False, encoding='utf-8')
df_wczytany = pd.read_csv('pracownicy.csv')

# --- WYŚWIETLENIE WYNIKÓW ---
print("Oryginalny DataFrame:")
print(df)
print("\n[a] Pensja > 5000:")
print(pensja_powyzej_5000)
print("\n[b] Posortowane według wieku:")
print(df_posortowany)
print("\n[c] Średnia pensja na stanowisku:")
print(srednia_pensja_stanowisko)
print("\n[d] Połączone dane (awanse):")
print(df_polaczony)
print("\n[f] Sprawdzenie pliku:")
print(df_wczytany.head())