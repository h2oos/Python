#function return temperature scale
def getTemperatureScale():
    print("Please enter Fahrenheit, Celsius, Kelvin, Rankine, Delisle, Newton, Roaumur, or Romer")
    scale = input()
    return scale

#function converts temp to scale
def convertToIntermediateTemperatureScale(temperature, inputScale):
    if inputScale == "Fahrenheit":
        return (temperature - 32) * (5/9)
    elif inputScale == "Celsius":
        return temperature
    elif inputScale == "Kelvin":
        return temperature - 273.15
    elif inputScale == "Rankine":
        return (temperature - 491.67) * (5/9)
    elif inputScale == "Delisle":
        return (100 - temperature) * (3/2)
    elif inputScale == "Newton":
        return temperature * (100/33)
    elif inputScale == "Roaumur":
        return temperature * (4/5)
    elif inputScale == "Romer":
        return temperature * (21/40) + 7.5
    else:
        print("Please enter a valid scale.")
    getTemperatureScale()

#function returns temp   
def convertToTargetTemperatureScale(temperature, targetScale):
    if targetScale == "Fahrenheit":
        return temperature * (9/5) + 32
    elif targetScale == "Celsius":
        return temperature
    elif targetScale == "Kelvin":
        return temperature + 273.15
    elif targetScale == "Rankine":
        return temperature * (9/5) + 491.67
    elif targetScale == "Delisle":
        return (100 - temperature) * (2/3)
    elif targetScale == "Newton":
        return temperature * (33/100)
    elif targetScale == "Roaumur":
        return temperature * (5/4)
    elif targetScale == "Romer":
        return (temperature - 7.5) * (40/21)
    else:
        print("Please enter a valid scale.")
    getTemperatureScale()

def main():
    again = "Y"
    while again == "Y":
        temperature = float(input("Please enter a temperature: "))
        inputScale = getTemperatureScale()
        intermediateTemperature = convertToIntermediateTemperatureScale(temperature, inputScale)
        if intermediateTemperature < 0:
            print("That temperature is below absolute zero, and therefore is invalid.")
            print("You need to enter a temperature that is greater than or equal to absolute zero.")
            main()
        targetScale = getTemperatureScale()
        finalTemperature = convertToTargetTemperatureScale(intermediateTemperature, targetScale)
        print("You entered", temperature, "degrees", inputScale + ", which is equal to", finalTemperature, "degrees", targetScale + ".")
        again = input("Would you like to enter another temperature?\nPlease enter Y for yes or N for No.\n")
        if again == "n" or again == "N":
            print("Good-bye!!")  
            break
        while again != "Y" and again != "N":
            print("Please enter Y for yes or N for No.")
            again = input()
    
main()