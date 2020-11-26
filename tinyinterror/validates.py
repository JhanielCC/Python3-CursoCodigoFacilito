def validate_tiny_int(val):
    return val >= 0 and val <= 255

def validate_val(val): #"60"
    try:
        return isinstance(int(val),int) #retorna T/F siel valor es una instancia de int
    except ValueError as error:
        return print(error)