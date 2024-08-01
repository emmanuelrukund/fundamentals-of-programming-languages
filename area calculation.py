area = input("which shape(triangle, rectangle, circle)do you want to calculate: ")
if area == str("triangle"):
    print ("area of a triangle")
    x = int(input("enter base of triangle: "))
    y = int(input("enter height of triangle: "))
    area = ((1/2) * x * y)
    print ("area of triangle is",area)
elif area == str("rectangle"):
    print ("area of rectangle")
    x = float(input("enter length of rectangle: "))
    y = float(input("enter width of rectangle: "))
    area = (x * y)
    print("area of the rectangle is",area)
else:
    print ("area of a circle")
    x = float(input("enter pie: "))
    y = float(input("enter radius of the circle:"))
    area = (x * y**2)
    print ("area of the circle is",area )
