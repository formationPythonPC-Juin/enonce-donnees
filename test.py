import pandas as pa



table = pa.read_csv("donnees.csv", delimiter = ";")

T = table["température"]
R = table["Réquivalente"]



file = open("donnees2.csv", "w")

file.write("température,Réquivalente\n")

for i in range(len(T)) : 
    t = str(T[i]) ; file.write(t)
    file.write(",")
    r = str(R[i]) ; file.write(r)
    file.write("\n")

file.close()
