def main():
    #Collect Input for each
    #Variable: first Prompt: Child's First Name:
    first = input("Child's First Name: ")
    #Variable: last Prompt: Child's Last Name:
    
    last = input("Camper's Name: ")

    #Variable: birth Prompt: In what year was {first} {last} born:
    
    birth = input(f"Birth Year: ")

    #Variable: days Prompt: How many days will {first} attend?
    
    days = input(f"Camp Duration: days")

    #Variable: p_first Prompt: Parent's First Name:

    p_first = input(f"Parent's Name: ")

    #Variable: p_last Prompt: Parent's Last Name:
    
    p_last = input(f"Parent's Name: ")

    #Variable: phone Prompt: Parent's Phone #:
    
    phone = input(f"Phone Number: ")

    #Variable: street Prompt: Street Address:

    street = input(f"Phone Number: ")

    #Variable: city Prompt: City:

    city = input(f"Phone Number: ")

    #Variable: state Prompt: State Abbreviation:

    state = input(f"Phone Number: ")

    #Variable: zip Prompt: Zip Code:
    
    input(f"Address:\n{street}\n{city}, {state} {zip}")

if __name__ == "__main__":
    main()
