class Variable:
    def __init__(self, n, t, v):
        self.nombre = n
        self.tipo = t
        self.valor = v

def esSimboloEsp(caracter):
    return caracter in "+-*;,.:!=%&/()[]<>=!"

def esSeparador(caracter):
    return caracter in " \n\t"

def esEntero(cad):
    try:
        int(cad)
        return True
    except:
        return False

def tokeniza(linea):
    tokens = []
    tokens2 = []
    dentro = False
    cad = ""

    for l in linea:
        if esSimboloEsp(l) and not dentro:
            tokens.append(l)
        elif (esSimboloEsp(l) or esSeparador(l)) and dentro:
            tokens.append(cad)
            cad = ""
            dentro = False
            if esSimboloEsp(l):
                tokens.append(l)
        elif not esSimboloEsp(l) and not esSeparador(l) and not dentro:
            dentro = True
            cad = l
        elif not esSimboloEsp(l) and not esSeparador(l) and dentro:
            cad = cad + l

    if dentro:
        tokens.append(cad)

    compuesto = False
    for c in range(len(tokens) - 1):
        if compuesto:
            compuesto = False
            continue
        if tokens[c] in "=<>!" and tokens[c + 1] == "=":
            tokens2.append(tokens[c] + "=")
            compuesto = True
        else:
            tokens2.append(tokens[c])
    if tokens:
        tokens2.append(tokens[-1])

    for c in range(1, len(tokens2) - 1):
        if tokens2[c] == "." and esEntero(tokens2[c - 1]) and esEntero(tokens2[c + 1]):
            tokens2[c] = tokens2[c - 1] + tokens2[c] + tokens2[c + 1]
            tokens2[c - 1] = "borrar"
            tokens2[c + 1] = "borrar"

    while "borrar" in tokens2:
        tokens2.remove("borrar")

    tokens = []
    dentroCad = False
    cadena = ""

    for t in tokens2:
        if dentroCad:
            cadena = cadena + " " + t
            if t[-1] == '"':
                tokens.append(cadena[1:-1])
                dentroCad = False
        elif t[0] == '"':
            cadena = t
            dentroCad = True
        else:
            tokens.append(t)

    return tokens

def esId(cad):
    return cad[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"

def agregaVar(varNombre, tipoVar):
    tablaVar.append(Variable(varNombre, tipoVar, "0"))

def setValor(varNombre, valor):
    print("asignar a la variable", varNombre, "El valor", valor)
    for v in tablaVar:
        if v.nombre == varNombre:
            tipo = getTipo(varNombre)
            if tipo == "int":
                v.valor = int(valor)
            elif tipo == "char":
                v.valor = valor
            elif tipo == "float":
                v.valor = float(valor)

def getValor(varNombre):
    for v in tablaVar:
        if v.nombre == varNombre:
            return v.valor

def getTipo(varNombre):
    for v in tablaVar:
        if v.nombre == varNombre:
            return v.tipo

def estaEnTabla(n):
    for reg in tablaVar:
        if reg.nombre == n:
            return True
    return False

# Inicio del intérprete
tablaVar = []
renglon = ""

while renglon != "end;":
    renglon = input("## ")
    tokens = tokeniza(renglon)
    print(tokens)

tablaVar = []
renglon = ""

while (renglon != "end;"):
    renglon = input("## ")
    tokens = tokeniza(renglon)
    print(tokens)

    if len(tokens) == 0:
        continue

    if tokens[0] == "var":  # Declaración de variable: var int x;
        if len(tokens) >= 3:
            agregaVar(tokens[2], tokens[1])
        else:
            print("Error en declaración de variable.")
    
    elif esId(tokens[0]):  # El primer token es un identificador
        if len(tokens) == 4 and tokens[1] == "=":  # Asignación: x = 5;
            setValor(tokens[0], tokens[2])
        elif len(tokens) == 2:  # Solo imprimir valor de variable: x;
            print(getValor(tokens[0]))
        else:
            print("No se reconoce la expresión")

    elif tokens[0] == "print":  # print(x);
        if len(tokens) >= 4 and tokens[3] == ")":
            valor = getValor(tokens[2])
            print(valor)
        else:
            print("Error en la instrucción print.")

    else:
        print("No se reconoce la expresión")
