class Array2D:
    def __init__(self,rows,cols):
        self.__data=[]
        self.__row=rows
        self.__col=cols
        for row in range(rows):
            tmp=[]                    #Todas las listas que se van generando tienen el mismo nombre entonces como las identifico?
            for col in range(cols):   #estamos creando la matriz
                tmp.append(None)
            self.__data.append(tmp)
        
            
    def to_string(self):
        print(self.__data)  #va a imprimir la matriz 
    
    def get_num_rows(self): #devuelve el numero de filas
        return self.__row
        
    def get_num_cols(self): #devuelve el numero de columnas
        return self.__col
        
    def clearing(self,value):
        for row in range(self.__row):              #pone un valor que yo le envie en todas las casillas
            for col in range(self.__col):
                self.__data[row][col]=value
                
    def set_item(self,renglon,columna,valor):
        r=renglon
        c=columna
        if(r>=0 and r<self.__row)and(c>=0 and c<self.__row):   
            self.__data[r][c]=valor                            #Pone un valor en la casilla que le indiquemos
            

    def get_item(self,renglon,columna):  #obtiene un valor de un reglon y columna que yo le indique
        r=renglon
        c=columna
        self.__data[r][c]=valor
        return valor
        
        
        
     



def main():
    pass
  
    
    
   
main()
