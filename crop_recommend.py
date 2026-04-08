def recommend_crop(soil, temp):
    
    if soil == "loamy" and temp > 20:
        return "Wheat"
    
    if soil == "sandy":
        return "Groundnut"
    
    return "Rice"