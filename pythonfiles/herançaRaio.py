class Círculo:
    def __init__(self,raio):
        self.raio=raio
    
    def area(self):
        area=3.14*(self.raio)**2
        return area

    def perimetro(self):
        perimetro=(2*3.14*self.raio)
        return perimetro
    
