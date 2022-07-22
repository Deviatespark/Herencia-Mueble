from models.Mueble import Mueble

class Mesa(Mueble):
    numeroPatas = int(4)

    def calculoArea(self):
        print("El volumen del mueble es: ", self.ancho * self.alto * self.largo,
              "\n y el numero de patas: ", self.numeroPatas)



