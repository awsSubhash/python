import wmi

def get_cpu_fan_speed():
    try:
        w = wmi.WMI(namespace="root\\LibreHardwareMonitor")
        sensors = w.Sensor()

        fans = []
        for sensor in sensors:
            if sensor.SensorType == 'Fan':
                fans.append((sensor.Name, sensor.Value))

        return fans if fans else "No fan data found"

    except Exception as e:
        return f"Error: {e}"

print(get_cpu_fan_speed())