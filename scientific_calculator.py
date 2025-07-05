import math

def sin_deg(angle):
    return math.sin(math.radians(angle))

def cos_deg(angle):
    return math.cos(math.radians(angle))

def log10(value):
    return math.log10(value)

if __name__ == "__main__":
    print("Scientific Calculator Test")
    print("sin(30) =", sin_deg(30))
    print("cos(60) =", cos_deg(60))
    print("log10(1000) =", log10(1000))
