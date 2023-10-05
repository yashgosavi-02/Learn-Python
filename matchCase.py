# matchCase is like SwitchCase

a = int(input("Enter Your Choice\n1.Start 2.Stop 3.Pause 4.Play : "))
match a:
    case 1: print("Starting..")
    case 2: print("Stopping..")
    case 3: print("Pausing..")
    case 4: print("Playing..")
    case _: print("No match found") # default case


