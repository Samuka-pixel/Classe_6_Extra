R = int(input("Quanta energia é que as residencias gastaram?: "))
I = int(input("Quanta energia é que as industrias gastaram?: "))
C = int(input("Quanta energia é que os comercios gastaram?: "))
if R <= 500:
    R_p = 0.40
else:
    R_p = 0.65
if C <= 1000:
    C_p = 0.55
else:
    C_p = 0.60
if I <= 5000:
    I_p = 0.55
else:
    I_p = 0.60

print("*-----------------------------------*\n"
      "|Tipo           |kWH         |Preço |\n"
      "*-----------------------------------*\n"
      "|Residencial    |", R,"      |", R_p," |\n"
      "*-----------------------------------*"
      "|Comercial      |", C,"      |", C_p," |\n"
      "*-----------------------------------*\n"
      "|Industrial     |", I,"      |", I_p," |\n"
      "*-----------------------------------*")


