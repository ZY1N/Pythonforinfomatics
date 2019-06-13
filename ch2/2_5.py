#Exercise 2.5 Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted temperature.

celsius = raw_input("Enter Celsius ")
celsius = float(celsius)
fahrenheit = (celsius * (9.0/5) + 32)
print celsius,"Celsius into Fahrenehit is", fahrenheit
