# Vern mot kjøretidsfeil og logiske feil i programmer

##Kjøretidsfeil

Håndtering av kjøretidsfeil i Python gjøres med nøkkelordene try og except. 
Python forsøker å kjøre kodenlokken som ligger under `try` hvis python får en feil meldig, vil den kjøre kodeblokken som ligger under `except`
```python
try:
    alder = int(input("Alder: "))
    fødselsår = 2023 -alder
    print(f"Fødselsår: {fødselsår}")
except:
    print("Feil: alder må være et heltall")

print("koden fortsetter")
```

###Eksperttips : While løkke

```python
while True:
    try:
        alder= int(input("Alder: "))
        break
    except:
        print("Alder må være et heltall, prøv igjen")
fødselsår = 2023 - alder
print(f"fødselsår: {fødselsår}")
```

## Logiske feil i rogrammer

for å oppdage logiske feil i python.programmer kan vi bruke nøkkelordet `assert`for å forsikre oss om at koden gir korrekte 

```python
assert 5 > 10 #10 er større enn 5 derfor gjør den ingen ting

assert 10 > 20 #10 er ikke større en  20 detfor gor denne feilmelding
```

eksempel: Test av fuksjoner med assert:

```python
def areal(høyde, bredde):
    return høyde + bredde
def omkrets(høyde, bredde):
    assert høyde + høyde + bredde + bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 
assert omkrets(3,4) ==
```

