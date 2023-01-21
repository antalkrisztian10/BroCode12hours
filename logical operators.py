# logical operators (and,or,not) = utilizați pentru a verifica dacă două sau mai multe declarații condiționale sunt adevărate.
# and = ambele elemente din if trebuie sa fie adevarate
# or = doar un element din if trebuie sa fie adevarat
# not = daca propozitia este adevarata o transforma in fals si invers

temp = int(input("What is the temperature outside!: "))

if not (temp >=0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go outside!")