# from typing import List

# class Vehicule:
#     def accelerate(self):
#         raise NotImplementedError("The method is abstract")

# class MotorlessVehicule(Vehicule):
#     def accelerate(self):
#         print("Go cleanly !")

        
# class Bike(MotorlessVehicule):
#     def accelerate(self):
#         print("Go cleanly by bike!")

# class Skateboard(MotorlessVehicule):
#     def accelerate(self):
#         print("Go cleanly by skate!")
        

# vehicules : List[Vehicule] = [] # notation typé (depuis python3)
# vehicules.append(Bike())
# vehicules.append(Skateboard())

# for v in vehicules:
#     v.accelerate()


# class Counter:
#     count = 0                   # attribut de classe

#     def __init__(self, name):
#         self.name = name        # attribut d'instance

#     @classmethod
#     def add(cls, num):          # méthode de classe
#         cls.count += num

# c1 = Counter("Counter #1")      
# c2 = Counter("Counter #2")

# print(Counter.count, c1.count, c2.count)

# Counter.add(5)         
# print(Counter.count, c1.count, c2.count)

# c1.add(5)         
# print(Counter.count, c1.count, c2.count)

# c2.add(-10)         
# print(Counter.count, c1.count, c2.count)


class A():
    pass

class B():
    pass

class C(A):
    pass

class D(B,A):
    pass

class E(D,A):
    pass

class F(E, D):
    pass

class G(F, C):
    pass

print(C.__mro__)
print(D.__mro__)

print(E.__mro__)
print(G.__mro__)
