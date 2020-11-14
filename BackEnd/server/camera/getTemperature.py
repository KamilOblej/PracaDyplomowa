from w1thermsensor import W1ThermSensor


def getTemperature():
    temperature = []

    for sensor in W1ThermSensor.get_available_sensors():
        # print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
        temperature.append(sensor.get_temperature())
    return temperature

