small_value = 1 
big_value = -1
#Loop
while True: 
    n = int(input("n? skriv ett tal < 0 för att sluta "))
    if n < 0:
        break
    else:
        if n < small_value:
            small_value = n
        if n > big_value:
            big_value = n

print("Största värdet är: ", big_value)
print("Minsta värdet är: ", small_value)