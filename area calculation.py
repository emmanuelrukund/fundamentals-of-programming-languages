# Prompt user to choose a shape to calculate the area for
area = input("Which shape (triangle, rectangle, circle) do you want to calculate: ")

# Check if the chosen shape is a triangle
if area == "triangle":
    print("Area of a triangle")
    # Prompt user to enter the base of the triangle
    x = int(input("Enter base of triangle: "))
    # Prompt user to enter the height of the triangle
    y = int(input("Enter height of triangle: "))
    # Calculate the area of the triangle
    area = (1/2) * x * y
    # Print the calculated area of the triangle
    print("Area of triangle is", area)

# Check if the chosen shape is a rectangle
elif area == "rectangle":
    print("Area of rectangle")
    # Prompt user to enter the length of the rectangle
    x = float(input("Enter length of rectangle: "))
    # Prompt user to enter the width of the rectangle
    y = float(input("Enter width of rectangle: "))
    # Calculate the area of the rectangle
    area = x * y
    # Print the calculated area of the rectangle
    print("Area of the rectangle is", area)

# If the chosen shape is not a triangle or rectangle, assume it is a circle
else:
    print("Area of a circle")
    # Prompt user to enter the value of pi
    x = float(input("Enter pi: "))
    # Prompt user to enter the radius of the circle
    y = float(input("Enter radius of the circle: "))
    # Calculate the area of the circle
    area = x * y**2
    # Print the calculated area of the circle
    print("Area of the circle is", area)
