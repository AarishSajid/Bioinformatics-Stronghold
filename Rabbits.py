def fibonacci_Rabiits(maheenai , litre):
    parent, bacha = 1, 1
    for i in range(maheenai - 1):
        bacha , parent = parent, parent + (bacha*litre)
    return bacha

print(fibonacci_Rabiits(34, 2))