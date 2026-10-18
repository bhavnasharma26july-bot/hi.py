

print("=== Power Calculator ===")


base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (exponent): "))


answer = 1


for i in range(1, exponent + 1):
    answer = answer * base
    print("Step", i, ": answer =", answer)


print("Answer:", base, "to the power", exponent, "=", answer)