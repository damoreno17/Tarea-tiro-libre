import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
import hashlib


r_0 = None
def get_r_0(pref1='FISI',pref2='2028'):
    '''
        Funcion para determinar r_0 usando un algoritmo de hash
    '''
    global r_0
    def get_codigo():
        while True:
            try:
                c = int(input("Ingrese su código de estudiante "))       
            except ValueError:
                print("El código debe ser un entero")
                continue
            else:
                if c < 300000000 and c > 190000000:
                    return c
                else:
                    print("El código no parece ser válido. Intente nuevamente")
    def hasher(key, n):
        # sum ASCII values and convert string to integer
        lst = [ord(char) for char in list(key)]
        return np.sum(lst) % n
    codigo = get_codigo()
    key1 = hashlib.sha256((pref1+str(codigo)).encode('utf-8'))
    key2 = hashlib.sha256((pref2+str(codigo)).encode('utf-8'))
    r_0 = np.array([
        hasher(key1.hexdigest(),100)/10+26,
        hasher(key2.hexdigest(),400)/10-20,
        0
    ])
    print("Posición inicial r_0=(x=%.1fm,y=%.1fm,z=%.1fm)"%(r_0[0],r_0[1],r_0[2]))
get_r_0()


