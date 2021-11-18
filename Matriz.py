class Matriz:
    A = [[0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0]]

    def __init__(self,matriz):
        separar = matriz.split(sep = ',')
        separar_int = [float(i) for i in separar]
        contador=0
        for i in range(0,3):
            for j in range(0,3):
                self.A[i][j]=separar_int[contador]
                contador = contador+1
    
                
    def mostrarma(self):
        print(self.A)
        
    def obtdetmatriz(self):
        det = self.A[0][0]*(self.A[1][1]*self.A[2][2]-self.A[2][1]*self.A[1][2])
        det1 =  self.A[0][1]*(self.A[1][0]*self.A[2][2]-self.A[2][0]*self.A[1][2])
        det2 =  self.A[0][2]*(self.A[1][0]*self.A[2][1]-self.A[2][0]*self.A[1][1])
        det_f = (det)-(det1)+(det2)
        return det_f

    def adjtrans (self):
        a = +(self.A[1][1]*self.A[2][2]-self.A[2][1]*self.A[1][2])
        b = -((self.A[1][0]*self.A[2][2]-self.A[2][0]*self.A[1][2]))
        c = +((self.A[1][0]*self.A[2][1]-self.A[2][0]*self.A[1][1]))
        d = -((self.A[0][1]*self.A[2][2]-self.A[2][1]*self.A[0][2]))
        e = +((self.A[0][0]*self.A[2][2]-self.A[2][0]*self.A[0][2]))
        f = -((self.A[0][0]*self.A[2][1]-self.A[2][0]*self.A[0][1]))
        g = +((self.A[0][1]*self.A[1][2]-self.A[1][1]*self.A[0][2]))
        h = -((self.A[0][0]*self.A[1][2]-self.A[1][0]*self.A[0][2]))
        i = +((self.A[0][0]*self.A[1][1]-self.A[1][0]*self.A[0][1]))
        
        adj = [[a,b,c],[d,e,f],[g,h,i]]
        
        trans = [[0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0]]
        for i in range (0,3):
            for j in range (0,3):
                trans [j][i] = adj[i][j]
        return trans

    def inversa(self):
        trans_adj = self.adjtrans()
        inv = [[0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0]]
        for i in range (0,3):
            for j in range (0,3):
                inv [i][j]= (1/self.obtdetmatriz()) * trans_adj [i][j]
        #inv = (1/self.obtdetmatriz()) * self.adjtrans()
        return inv
    def multiplica(self, fila):
        self.A
        acu = 0
        con = 0
        mares = []
        for i in range (0,3):
            acu = 0
            for j in range (0,3):
                pos=fila[0][j]*self.A[j][i]
                con = con + 1
                acu = acu + pos
                if con == 3:
                    mares.append(acu)
                    con = 0
        return mares

    def mensajecodificado(self, mensaje):
        pos1 = 0
        pos2 = 1
        tama = len(mensaje)
        mensajeCodificado = []
        for i in range(0, tama):
            var = mensaje[pos1:pos2]
            menres = self.multiplica(var) #manda a llamar a la funcion mutiplica
            pos1 = pos1 + 1
            pos2 = pos2 + 1
            mensajeCodificado.append(menres)
        return mensajeCodificado

    def multiplica_inv(self, fila):
        matriz_inversa = self.inversa()
        acu = 0
        con = 0
        mares = []
        for i in range (0,3):
            acu = 0
            for j in range (0,3):
                pos=fila[j]*matriz_inversa[j][i]
                con = con + 1
                acu = acu + pos
                if con == 3:
                    mares.append(acu)
                    con = 0
        return mares

    def mensajedecodificado(self, mensaje):
        pos1 = 0
        pos2 = 3
        tama = len(mensaje)/3
        tama=int(tama)
        mensajeCodificado = []
        for i in range(0, tama):
            var = mensaje[pos1:pos2]
            menres = self.multiplica_inv(var) #manda a llamar a la funcion mutiplica
            pos1 = pos1 + 3
            pos2 = pos2 + 3
            mensajeCodificado.append(menres)
        return mensajeCodificado
                    
       
                    
                    

                



        
