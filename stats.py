def calculate_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)