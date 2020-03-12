def divisores(i, entry, suma):
    while i < entry-1:
        i += 1
        if entry % i == 0:
            suma += i
    return suma