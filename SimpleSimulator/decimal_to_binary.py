def decimal_to_binary(num):
    binary = [0,0,0,0,0,0,0,0]
    dividend = int(num)
    quotient = -1
    k=7
    while(quotient!=0 and k>=0):
        quotient = dividend//2
        binary[k] = dividend%2
        k=k-1
        dividend = quotient
    return "".join(map(str, binary))
