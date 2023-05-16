from python.Zadatak4.strcmp import strcmp


string1 = "anaa"
string2 = "ana"
a = strcmp(string1, string2)
if a == 0:
    print("Stringovi su jednaki")
elif a == -1:
    print("Prvi string je veci od drugog")
else:
    print("Drugi string je veci od prvog")
    