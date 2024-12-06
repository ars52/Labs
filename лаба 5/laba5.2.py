class Сircle:
    
    def __init__(self, radius:int):
        self.radius = radius

    def get_radius(self):
        return (f'Значение радиуса: {self.radius}')
    
    def set_radius(self, new_radius:int):
        self.radius = new_radius
        
my_cicrle = Сircle(534)
print('Значение радиуса: {}'.format(my_cicrle.radius))
my_cicrle.set_radius(6)
print('Значение радиуса: {}'.format(my_cicrle.radius))       

