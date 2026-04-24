# Write a function that takes two numbers and returns their sum.


def two(a, b):
    return a + b


c = int(input("enter any number"))

d = int(input(" enter any number"))

total = two(c, d)

print("total is = ", total)

import psutil

def get_cpu_fan_speed():
    fans = psutil.sensors_fans()
    if not fans:
        return "No fan data available"

    result = {}
    for name, entries in fans.items():
        result[name] = []
        for entry in entries:
            result[name].append({
                "label": entry.label,
                "speed_rpm": entry.current
            })
    return result


# Example usage
if __name__ == "__main__":
    print(get_cpu_fan_speed())