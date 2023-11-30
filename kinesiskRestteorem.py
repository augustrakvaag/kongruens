liste = []
for i in range(220):
    if i % 4 == 3 and i % 5 == 2 and i % 11 == 4:
        liste.append(i)
print(liste)