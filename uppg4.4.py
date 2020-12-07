meter = 1
while meter > 0:
    meter = int(input("Släpp bollen från: "))

    centimeter = 100 * meter
    studs = 0

    while centimeter > 1:
        centimeter = centimeter * 0.7
        # print(centimeter)
        studs += 1

    print(f"Studs: {studs}")

print("Hej då")