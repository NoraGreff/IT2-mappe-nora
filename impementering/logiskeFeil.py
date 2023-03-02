assert 5 > 10 #10 er større enn 5 derfor gjør den ingen ting

assert 10 > 20 #10 er ikke større en  20 detfor gor denne feilmelding

print("Koden er ferdig")

def areal(høyde, bredde):
    return høyde * bredde
def omkrets(høyde, bredde):
    assert høyde + høyde + bredde + bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14

