import numpy as np
import matplotlib.pyplot as plt

def calculate_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)

def calculate_variance(data):
    if not data:
        return 0
    avg = calculate_mean(data)
    return sum((x - avg) ** 2 for x in data) / (len(data)-1)
    # Changed variance (originally pop variance)
    
def calculate_standard_deviation(data):
    import math
    return math.sqrt(calculate_variance(data))

def calculate_median(data):
    if not data:
        return 0
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        return data[n // 2]
