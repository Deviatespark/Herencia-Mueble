class Mueble():

    #Constructor
    def __init__(self, alto, ancho, largo):
        self.alto = float(alto)
        self.ancho = float(ancho)
        self.largo = float(largo)

    #getter y setter
    def getLargo(self):
        return self.__largo

    def setLargo(self,largoUsuario):
        self.__largo = largoUsuario

    def getAlto(self):
        return self.__alto

    def setAlto(self,altoUsuario):
        self.__alto = altoUsuario

    def getAncho(self):
        return self.__ancho

    def setAncho(self,achoUsuario):
        self.__ancho = achoUsuario

    # metodo calcula que calcula area

    def calculoArea(self):
        print("El volumen del mueble es: ", self.ancho * self.alto * self.largo)




