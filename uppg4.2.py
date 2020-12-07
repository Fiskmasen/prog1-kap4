# Beräkning av summan 1+2+3+ .. +n
while True: 
    n = int(input("n? Skriv ett tal <=0 för att sluta "))
    if n <= 0:
        break
    summa = 0
    k = 1
    while k <= n:
        summa = summa + k      # öka summan med k
        k = k + 1              # öka k med 1
    print("Summan blir", summa)