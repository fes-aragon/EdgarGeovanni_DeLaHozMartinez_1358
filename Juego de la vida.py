from Array2D importArray2D
class juegoDeLAvIDA:
    def __init__(self,rows,cols,generaciones,poblacion_inicial):
        self.cuadro=Array2D(rows,cols)
        self.__=rows
        self.__columnas=colsself.__generaciones=generaciones
        self.__cuadro.clearing(0)
        for cell in poblacion_inicial:
            self.__cuadro.set_item(cell[0],cell[1],1)
