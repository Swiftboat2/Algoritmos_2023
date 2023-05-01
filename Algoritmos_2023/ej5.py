romano = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

numero = 'MMXXIII'

def conv_romano_to_dec(numero_romano):
    if len(numero_romano) == 1:
        return romano[numero_romano]
    else:
        if romano[numero_romano[0]] >= romano[numero_romano[1]]:
            return romano[numero_romano[0]] + conv_romano_to_dec(numero_romano[1:])
        else:
            return romano[numero_romano[0]] + conv_romano_to_dec(numero_romano[1:])
print(conv_romano_to_dec(numero))