import DecimalToSignedBinary
import pencilAndPaper
import booths
import extendedBooths

def main():
    print("Enter input type:\n")
    print("[1] Decimal\n[2] Binary")
    while inputType != '1' or inputType != '2':
        inputType = input()
        if inputType == 1: #Decimal
            num1 = int(input("Enter multiplicand: "))
            num2 = int(input("Enter multiplicand: "))
            num1 = DecimalToSignedBinary.solve(num1)
            num2 = DecimalToSignedBinary.solve(num2)
        elif inputType == 2: #Binary
            num1 = input("Enter multiplicand: ")
            num2 = input("Enter multiplicand: ")

    print("Choose a method:\n")
    print("[1] Pencil and Paper\n[2] Booth's\n[3] Extended Booth's\n[4] All of the Above")
    inp1 = input()

    if(inp1 == "1"):
        print("Pencil and Paper\n")
        pencilAndPaper.solve(num1, num2)
    
    elif(inp1 == "2"):
        print("Booth's\n")
        booths.solve(num1, num2)

    elif(inp1 == "3"):
        print("Extended Booth's\n")
        extendedBooths.solve(num1, num2)

    elif(inp1 == "4"):
        print("All of the Above\n")
        pencilAndPaper.solve(num1, num2)
        booths.solve(num1, num2)
        extendedBooths.solve(num1, num2)
    
    loop()

def loop():
    x = input("\nWould you like to try again (Y/N): ")
    if x == 'Y':
        main()
    elif x == 'N':
        print("Program ended.") 
    elif x != 'Y':
        loop()

main()