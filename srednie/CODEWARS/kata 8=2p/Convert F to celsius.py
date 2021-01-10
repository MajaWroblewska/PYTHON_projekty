def weather_info(temp):         #Maja
    celsius = (temp - 32) * (5 / 9)
    if (celsius < 0):
        return (str(celsius) + " is freezing temperature")
    else:
        return (str(celsius) + " is above freezing temperature")
##########################################################################

def weather_info(temp):
    c = convertToCelsius(temp)
    if (c <= 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")

def convertToCelsius(temperature):
    celsius = (temperature - 32) * (5.0 / 9.0)
    return celsius
####################################################################################
def weather_info (temp):    #Jana
    c = round((temp - 32) * (5 / 9), 16)
    return f"{c} is above freezing temperature" if c > 0 else f"{c} is freezing temperature"

print(weather_info(50)) # '10.0 is above freezing temperature')
print(weather_info(23))    # '-5.0 is freezing temperature')