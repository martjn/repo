maakonnad = {
    "Tartumaa": "Tartu",
    "Jõgevamaa": "Jõgeva",
    "Harjumaa": "Tallinn",
    "Viljandimaa": "Viljandi",
}

linnad = {
    "Tartu": "Mäksa",
    "Jõgeva": "Voore",
    "Tallinn": "Rae",
    "Viljandi": "Paistu",
}

maakonnad["Saaremaa"] = "Kuressaare"
maakonnad["Hiiumaa"] = "Kärdla"

linnad["Kuressaare"] = "Pihtla"
linnad["Kärdla"] = "Emmaste"

a = "-" * 20

print(a)

for maakond, linn in list(maakonnad.items()):
    print(f"{maakond}l on üheks tema linnaks {linn}.")
    print(f"Ehk siis {linn} linn asub {maakond}l.")

for linn, vald in list(linnad.items()):
    if linn == "Tallinn":
        print(f"{linn}a linna üheks ligidaseks vallaks on {vald}.")
    else:
        print(f"{linn} linna üheks ligidaseks vallaks on {vald}.")

print(a)
print("Proovime uuesti.")

for maakond, linn in list(maakonnad.items()):
    print(f"{maakond}l on {linn} linn.")
    if linn == "Tallinn":
        print(f"{linn}a linna lähedal asub {linnad[linn]} vald.")
    else:
        print(f"{linn} linna lähedal asub {linnad[linn]} vald.")

print(list(linnad.keys()))

for linn in list(linnad.keys()):
    print(f"See on {linn} linn.")