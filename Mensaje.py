class Mensaje:

    def __init__(self, men =""):
        self.mensaje = men
    def codifica(self):
        mensaje_num = []
        for i in self.mensaje:
            if i == ' ':
                mensaje_num.append(0)
            elif i == 'A':
                mensaje_num.append(1)
            elif i == 'B':
                mensaje_num.append(2)
            elif i == 'C':
                mensaje_num.append(3)
            elif i == 'D':
                mensaje_num.append(4)
            elif i == 'E':
                mensaje_num.append(5)
            elif i == 'F':
                mensaje_num.append(6)
            elif i == 'G':
                mensaje_num.append(7)
            elif i == 'H':
                mensaje_num.append(8)
            elif i == 'I':
                mensaje_num.append(9)
            elif i == 'J':
                mensaje_num.append(10)
            elif i == 'K':
                mensaje_num.append(11)
            elif i == 'L':
                mensaje_num.append(12)
            elif i == 'M':
                mensaje_num.append(13)
            elif i == 'N':
                mensaje_num.append(14)
            elif i == 'O':
                mensaje_num.append(15)
            elif i == 'P':
                mensaje_num.append(16)
            elif i == 'Q':
                mensaje_num.append(17)
            elif i == 'R':
                mensaje_num.append(18)
            elif i == 'S':
                mensaje_num.append(19)
            elif i == 'T':
                mensaje_num.append(20)
            elif i == 'U':
                mensaje_num.append(21)
            elif i == 'V':
                mensaje_num.append(22)
            elif i == 'W':
                mensaje_num.append(23)
            elif i == 'X':
                mensaje_num.append(24)
            elif i == 'Y':
                mensaje_num.append(25)
            elif i == 'Z':
                mensaje_num.append(26)
            elif i == 'Ñ':
                mensaje_num.append(27)
        return  mensaje_num

    def probar_lis(self):
        mensaje_num=[]
        mensaje_num.append([5,14,13]);
        mensaje_num.append([5, 14, 13]);
        return  mensaje_num;
    def seccionar(self, mensaje_num):
        
        mensaje_seccionado = []
        contador = 0
        men3 = []
        for i in mensaje_num:
            men3.append(i)
            contador=contador+1
            if contador==3:
                mensaje_seccionado.append(men3)
                contador=0
                men3=[]
        size_list = len(men3)
        if size_list == 1:
            men3.append(0)
            men3.append(0)
            mensaje_seccionado.append(men3)
        elif size_list==2:
            men3.append(0)
            mensaje_seccionado.append(men3)
        return mensaje_seccionado

    def deseccionar(self, mensaje_num):
        mensaje_seccionado = []
        for i in mensaje_num:
            for j in i:
                mensaje_seccionado.append(j)

        return mensaje_seccionado
    
    def decodifica(self, menreci):
        mensaje_num = []
        for i in menreci:
            if i == 0:
                mensaje_num.append(' ')
            elif i == 1:
                mensaje_num.append('A')
            elif i == 2:
                mensaje_num.append('B')
            elif i == 3:
                mensaje_num.append('C')
            elif i == 4:
                mensaje_num.append('D')
            elif i == 5:
                mensaje_num.append('E')
            elif i == 6:
                mensaje_num.append('F')
            elif i == 7:
                mensaje_num.append('G')
            elif i == 8:
                mensaje_num.append('H')
            elif i == 9:
                mensaje_num.append('I')
            elif i == 10:
                mensaje_num.append('J')
            elif i == 11:
                mensaje_num.append('K')
            elif i == 12:
                mensaje_num.append('L')
            elif i == 13:
                mensaje_num.append('M')
            elif i == 14:
                mensaje_num.append('N')
            elif i == 15:
                mensaje_num.append('O')
            elif i == 16:
                mensaje_num.append('P')
            elif i == 17:
                mensaje_num.append('Q')
            elif i == 18:
                mensaje_num.append('R')
            elif i == 19:
                mensaje_num.append('S')
            elif i == 20:
                mensaje_num.append('T')
            elif i == 21:
                mensaje_num.append('U')
            elif i == 22:
                mensaje_num.append('V')
            elif i == 23:
                mensaje_num.append('W')
            elif i == 24:
                mensaje_num.append('X')
            elif i == 25:
                mensaje_num.append('Y')
            elif i == 26:
                mensaje_num.append('Z')
            elif i == 27:
                mensaje_num.append('Ñ')
            else:
                mensaje_num.append('caracter no identificado')
        return mensaje_num



