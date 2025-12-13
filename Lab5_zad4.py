import pandas as pd
data = {
 'Numer ID pracownika' : [ "1","2","3","4","5"],
 'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
 'Nazwisko': ["Kowalska", "Nowak", "Wiśniewska","Kaczmarek", "Zieliński"],
 'Stanowisko': ["Manager", "Programista", "Konsultant", "Programist", "Manager"],
 'Wiek': [35,28,40,30,45],
 'Pensja': [8000,4500,6000,5500,7000]
}
df = pd.DataFrame(data)
print(df)
pensja_wieksza5000=df[df['Pensja'] > 5000]
pensja = df.loc[pensja_wieksza5000,"Imię"]
print(f"Oni zarabiają więcej niż 5000zl {pensja}")
wiek=df.sort_index("Wiek",ascending=False)
print(wiek)