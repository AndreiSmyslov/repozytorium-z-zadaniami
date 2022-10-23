#word-rank

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

wszystkie_slowa = []
male_slowa = []
ilosc_slowa = {}

for i in sentences:
    wszystkie_slowa += i.split(" ")

for e in wszystkie_slowa:
    male_slowa.append(e.lower())

for x in male_slowa:
    if x not in ilosc_slowa:
        ilosc_slowa.update({x:1})
    else:
        ilosc_slowa[x] += 1

poukladane_slowa = sorted(ilosc_slowa.items(),key = lambda y: y[1], reverse = True)
    
print(f'''Wynik:\n1. "{poukladane_slowa[0][0]}" - {poukladane_slowa[0][1]}
2. "{poukladane_slowa[1][0]}" - {poukladane_slowa[1][1]}
3. "{poukladane_slowa[2][0]}" - {poukladane_slowa[2][1]}''')
