import DecimalToSignedBinary
import pencilAndPaper
import booths
import extendedBooths

def main():
    inp1 = input("Choose a method between....\n(1) Pencil and Paper\n(2) Booth's Algorithm\n(3) Extended Booth's Algorithm\n")
    if(inp1 == "1"):
        print("\nPencil and Paper\n")
        inp = input("Choose input type (D/B): ")
        if(inp == 'D'):
            decimal1 = int(input("Enter decimal 1: "))
            decimal1 = DecimalToSignedBinary.solve(decimal1)
            decimal2 = int(input("Enter decimal 2: "))
            decimal2 = DecimalToSignedBinary.solve(decimal2)
            pencilAndPaper.solve(decimal1, decimal2)
        elif(inp == 'B'):
            pencilAndPaper.get()

    
    elif(inp1 == "2"):
        print("\nBooth's\n")
        inp = input("Choose input type (D/B): ")
        if(inp == 'D'):
            decimal1 = int(input("Enter decimal 1: "))
            decimal1 = DecimalToSignedBinary.solve(decimal1)
            decimal2 = int(input("Enter decimal 2: "))
            decimal2 = DecimalToSignedBinary.solve(decimal2)
            booths.solve(decimal1, decimal2)
        elif(inp == 'B'):
            booths.get()
    
    elif(inp1 == "3"):
        print("\nExtended Booth's\n")
        inp = input("Choose input type (D/B): ")
        if(inp == 'D'):
            decimal1 = int(input("Enter decimal 1: "))
            decimal1 = DecimalToSignedBinary.solve(decimal1)
            decimal2 = int(input("Enter decimal 2: "))
            decimal2 = DecimalToSignedBinary.solve(decimal2)
            extendedBooths.solve(decimal1, decimal2)
        elif(inp == 'B'):
            decimal1 = input("Enter decimal 1: ")
            decimal2 = input("Enter decimal 2: ")
            extendedBooths.solve(decimal1, decimal2)
    
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