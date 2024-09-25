def trapezoid_area(a, b, c, d):
    
    p = (a + b + c + d) / 2
    
    area = (p * (p - a) * (p - b) * (p - c) * (p - d)) ** 0.5
    
    return area

a = 5 
b = 7
c = 5
d = 3 

area = trapezoid_area(a, b, c, d)
print(f"Площадь трапеции: {area:.2f}")
