from w1thermsensor import W1ThermSensor


def getTemperature():
    temperature = []

    for sensor in W1ThermSensor.get_available_sensors():
        temperature.append(sensor.get_temperature())
    return temperature

