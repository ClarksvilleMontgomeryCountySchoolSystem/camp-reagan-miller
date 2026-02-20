def main():
    #Collect Input for each
    #Variable: first Prompt: Child's First Name:
    first = input("Child's First Name: ")
    #Variable: last Prompt: Child's Last Name:
    
    last = input("Child's Last Name: ")

    #Variable: birth Prompt: In what year was {first} {last} born:
    
    birth = input(f"In what year was {first} {last} born: ")

    #Variable: days Prompt: How many days will {first} attend?
    
    days = input(f"How many days will {first} attend? ")

    #Variable: p_first Prompt: Parent's First Name:

    p_first = input(f"Parent's First Name: ")

    #Variable: p_last Prompt: Parent's Last Name:
    
    p_last = input(f"Parent's Last Name: ")

    #Variable: phone Prompt: Parent's Phone #:
    
    phone = input(f"Parent's Phone #: ")

    #Variable: street Prompt: Street Address:

    street = input(f"Street Address: ")

    #Variable: city Prompt: City:

    city = input(f"City: ")

    #Variable: state Prompt: State Abbreviation:

    state = input(f"State Abbreviation: ")

    #Variable: zip Prompt: Zip Code:
    
    zip = input(f"Zip Code:\n{street}\n{city}, {state} {zip}")

if __name__ == "__main__":
    main()
