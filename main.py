import DecimalToSignedBinary
import pencilAndPaper
import booths
import extendedBooths

def main():
    print("Choose a method:\n")
    print("[1] Pencil and Paper\n[2] Booth's\n[3] Extended Booth's\n[4] All of the Above")
    inp1 = input()

    if(inp1 == "1"):
        print("Pencil and Paper\n")
        inp = input("Choose input type (D/B): ")
        if(inp == 'D'):
            decimal1 = DecimalToSignedBinary.inputs()
            decimal2 = DecimalToSignedBinary.inputs()
            pencilAndPaper.solve(decimal1, decimal2)
        elif(inp == 'B'):
            pencilAndPaper.get()
    
    elif(inp1 == "2"):
        print("Booth's\n")
        inp = input("Choose input type (D/B): ")
        if(inp == 'D'):
            decimal1 = DecimalToSignedBinary.inputs()
            decimal2 = DecimalToSignedBinary.inputs()
            booths.solve(decimal1, decimal2)
        elif(inp == 'B'):
            booths.get()

    elif(inp1 == "3"):
        print("Extended Booth's\n")
        inp = input("Choose input type (D/B): ")
        if(inp == 'D'):
            decimal1 = DecimalToSignedBinary.inputs()
            decimal2 = DecimalToSignedBinary.inputs()
            extendedBooths.solve(decimal1, decimal2)
        elif(inp == 'B'):
            binary1 = input("Enter multiplicand: ")
            binary2 = input("Enter multiplier: ")
            extendedBooths.solve(binary1, binary2)

    elif(inp1 == "4"):
        print("All of the Above\n")
        inp = input("Choose input type (D/B): ")
        if(inp == 'D'):
            decimal1 = DecimalToSignedBinary.inputs()
            decimal2 = DecimalToSignedBinary.inputs()
            extendedBooths.solve(decimal1, decimal2)
        elif(inp == 'B'):
            binary1 = input("Enter multiplicand: ")
            binary2 = input("Enter multiplier: ")
            extendedBooths.solve(binary1, binary2)
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