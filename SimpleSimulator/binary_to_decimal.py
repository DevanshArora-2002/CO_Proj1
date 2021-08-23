def binary_to_decimal(str):
    num=0
    for i in range(1,9):
        num+=int(str[-i])*2**(i-1)
    return num
