def main():
    #escribe tu código abajo de esta línea
us=input()
res=us.split()

us2=input()
res2=us2.split()

if len(res)!=2:
    print('La matriz no es una matriz de 2x2')
else:
    mat=[[int(res[0]),int(res[1])],[int(res2[0]),int(res2[1])]]
    res=(int(res[0])*int(res2[1]))-((int(res[1])*int(res2[0])))
    print(res)
if __name__=='__main__':
    main()
