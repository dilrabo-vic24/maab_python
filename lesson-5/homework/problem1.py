def convert_cel_to_far(gradus):
    return round(gradus * 9 / 5 + 32, 2)

gradus = float(input("Enter a temperature in degrees C: "))
print(f"{gradus} degrees C = {convert_cel_to_far(gradus)} degrees F")


def convert_far_to_cel(temperatura):
    return round((temperatura - 32) * 5 / 9, 2)

temperatura = float(input("Enter a temperature in degrees F: "))
temperatura_cel = convert_far_to_cel(temperatura)
print(f"{temperatura} degrees F = {temperatura_cel} degrees C")