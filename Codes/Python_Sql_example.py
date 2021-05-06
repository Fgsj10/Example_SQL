from prettytable import PrettyTable

#specify name of columns and initializing table

myTabble = PrettyTable(["Name","last name", "age", "cellphone"])

#Adding lines
myTabble.add_row(["Francisco", "Gomes", "26", "99675-7122"])
myTabble.add_row(["Isabella", "Andrade", "28", "98620-4311"])
myTabble.add_row(["Iasmim", "Galvão", "28", "null"])


#Printing table
print(myTabble)