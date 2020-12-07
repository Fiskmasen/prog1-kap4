# Ränta på ränta
balance = float(input("Ditt startkapital: "))
save = float(input("jag vill spara i månaden: "))
year = int(input("under så många år: "))
interest = int(input("ränta i %: "))
balanceWithInterest = 0

for i in range(0, year):
    balance += save * 12
    balanceWithInterest += save * 12
    balanceWithInterest *= (interest / 100 + 1)
    print(f"År {i} har du sparat {balance:.2f} kronor, \
        vilket är {balanceWithInterest:.2f} med ränta.")

print(f"Efter {year} år har du sparat ihop {balanceWithInterest:.2f} kronor")