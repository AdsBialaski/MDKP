import math

def hardCap(cap, amount, *_):
    if amount > cap:
        return float("inf")
    return 0

def linearCost(cap, amount, mult, *_):
    return max(0, amount - cap) * mult

def quadraticCost(cap, amount, mult, *_):
    return max(0, amount - cap) ** 2 * mult

def cubicCost(cap, amount, mult, *_):
    return max(0, amount - cap) ** 3 * mult

def expCost(cap, amount, mult, base):
    return base ** (max(0, amount - cap)) * mult

def logCost(cap, amount, mult, base):
    return math.log(max(0, amount - cap) + 1, base) * mult

def costFunction(costType, cap, amount, mult=1, base=2):
    functions = {
        "hard": hardCap,
        "linear": linearCost,
        "quadratic": quadraticCost,
        "cubic": cubicCost,
        "exp": expCost,
        "log": logCost
    }
    
    if costType not in functions:
        # error
        return None
    
    return functions[costType](cap, amount, mult, base)