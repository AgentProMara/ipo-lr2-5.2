a = 5 
b = 7
c = 5
d = 3 
    
p = (a + b + c + d) / 2
    
area = (p * (p - a) * (p - b) * (p - c) * (p - d)) ** 0.5

print(f"Площадь трапеции: {area:.2f}")
