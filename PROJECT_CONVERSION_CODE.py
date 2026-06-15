        "PROJECT CONVERSION CODE"

PROGRAM....

# Unit Converter Tool

while True:

    print("\n===== UNIT CONVERTER =====")
    print("\t\t\t\t\t1. Kilometer to Meter")
    print("\t\t\t\t\t2. Meter to Kilometer")
    print("\t\t\t\t\t3. Meter to Centimeter")
    print("\t\t\t\t\t4. Centimeter to Meter")
    print("\t\t\t\t\t5. Liter to Milliliter")
    print("\t\t\t\t\t6. Milliliter to Liter")
    print("\t\t\t\t\t7. Kilogram to Gram")
    print("\t\t\t\t\t8. Gram to Kilogram")
    print("\t\t\t\t\t9. Celsius to Fahrenheit")
    print("\t\t\t\t\t10. Fahrenheit to Celsius")

    choice = int(input("\n\tEnter your choice (1-10): "))

#Length units

    if choice == 1:
        kilometer = float(input("Enter Kilometer: "))
        meter = kilometer * 1000
        print("Result:", meter, "Meter")

    elif choice == 2:
        meter = float(input("Enter Meter: "))
        kilometer = meter / 1000
        print("Result:", kilometer, "Kilometer")

    elif choice == 3:
        meter = float(input("Enter Meter: "))
        centimeter = meter * 100
        print("Result:", centimeter, "Centimeter")

    elif choice == 4:
        centimeter = float(input("Enter Centimeter: "))
        meter = centimeter / 100
        print("Result:", meter, "Meter")

#Liter units

    elif choice == 5:
        liter = float(input("Enter Liter: "))
        milliliter = liter * 1000
        print("Result:", milliliter, "Milliliter")

    elif choice == 6:
        milliliter = float(input("Enter Milliliter: "))
        liter = milliliter / 1000
        print("Result:", liter, "Liter")

#Weight units

    elif choice == 7:
        kilogram = float(input("Enter Kilogram: "))
        gram = kilogram * 1000
        print("Result:", gram, "Gram")

    elif choice == 8:
        gram = float(input("Enter Gram: "))
        kilogram = gram / 1000
        print("Result:", kilogram, "Kilogram")

#temperature units

    elif choice == 9:
        celsius = float(input("Enter Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Result:", fahrenheit, "°F")

    elif choice == 10:
        fahrenheit = float(input("Enter Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Result:", celsius, "°C")

    else:
        print("Invalid Choice!")

    again = input("\nDo you want another conversion? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using Unit Converter!")
        break


OUTPUT.....
         ===== UNIT CONVERTER =====
                  1.kilometer to Meter
                  2.Meter to kilometer
                  3.meter to Centimeter
                  4.Centimeter to meter
                  5.liter to Milliliter
                  6.Milliliter to liter
                  7.Kilogram to Gram
                  8.gram to Kilogram
                  9.Celsius to Fahrenheit
                 10.Fahrenheit to Celsius

    Enter your choice (1-10): 1

Enter Kilometer: 150
Result: 150000.0 Meter

Do you want another conversion? (Yes/no): yes


         ===== UNIT CONVERTER =====
                  1.kilometer to Meter
                  2.Meter to kilometer
                  3.meter to Centimeter
                  4.Centimeter to meter
                  5.liter to Milliliter–
                  6.Milliliter to liter
                  7.Kilogram to Gram
                  8.gram to Kilogram
                  9.Celsius to Fahrenheit
                 10.Fahrenheit to Celsius
   
      Enter your choice (1-10) : 6

Enter Millimeter:49
Result : 0.049 Liter

Do you want another conversion? (Yes/No): no

Thank you for using unit converter!...






