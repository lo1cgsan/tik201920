def pobierzDane():
    m = float(input('Podaj masę ciała (kg): '))
    while m < 10 or m > 200:
        print('Błędna wartość')
        m = float(input('Podaj masę ciała (kg): '))

    w = float(input('Podaj wzrost (m): '))
    while w < 1 or w > 2.5:
        print('Błędna wartość')
        w = float(input('Podaj wzrost (m): '))

    return m, w


m, w = pobierzDane()
print(m, w)

bmi = m / (w**2)
print(bmi)

if bmi < 18.5:
    print('niedowaga')
elif bmi < 25:
    print('norma')
elif bmi < 30:
    print('nadwaga')
else:
    print('otyłość')


input('Naciśnij jakiś klawisz...')
