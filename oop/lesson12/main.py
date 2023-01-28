from camp import Camp
def main():
    our_camp = Camp("Camp Integralytic", 20)
    menu_choice = None
    while menu_choice != 0:
        menu_choice = get_menu_choice()
        try:
            if menu_choice == 1: #add counselor
                # fname=input('Enter conselores first name: ')
                # lname=input('Enter conselores last name: ')
                # hire_date=input('Enter conselores hire date: ')
                # salary=input('Enter conselores salary:')
                # our_camp.add_counselor( fname, lname ,hire_date,salary)
                 our_camp.add_counselor( 'leah', 'itzinger' ,'02/05/2001',200)
                    
            elif menu_choice == 2: #add bunk
                # bunk_name=input('Enter bunk name:')
                # counselor_fname=input('Enter conselores first name:')
                # counselor_lname=input('Enter conselores last name:')
                # our_camp.add_bunk(bunk_name,counselor_fname ,counselor_lname )
                our_camp.add_bunk('A','leah' ,'itzinger' )
                    
            elif menu_choice == 3: #add camper
                # fname=input('Enter camper first name: ')
                # lname=input('Enter camper last name: ')
                # dob=input('Enter camper date of birth: ')
                # our_camp.add_camper( fname, lname ,dob)
                our_camp.add_camper( 'shoshi', 'finkel' ,'02/05/2001')
                    
            elif menu_choice == 4: #add an allergy
                # allergy=input('Enter campers allergy:')
                # fname=input('Enter camper first name:')
                # lname=input('Enter camper last name:')
                # our_camp.add_allergy(fname,lname,allergy )
                our_camp.add_allergy('shoshi','finkel','milk' )
                        
            elif menu_choice == 5: #assign camper to bunk
                # fname=input('Enter camper first name: ')
                # lname=input('Enter camper last name: ')
                # bunk_name=input('Enter bunk name:')
                # our_camp.place_camper( fname, lname ,bunk_name)
                our_camp.place_camper( 'shoshi', 'finkel' ,'A')
                    

                        
            elif menu_choice == 6:
                print(our_camp) 

                    
            elif menu_choice == 0:
                print('you exited this application')
        
        except Exception as ex:
             print('error' +str(ex))
                        
def get_menu_choice():
    menu = "\n1. Add A Counselor"
    menu +=	"\n2. Add a Bunk" 
    menu +=	"\n3. Add a Camper" 
    menu +=	"\n4. Add an Allergy"
    menu +=	"\n5. Assign a Camper to a Bunk"
    menu +=	"\n6. Display Camp data"
    menu +=	"\n0. Exit Application"
    choice = input(menu + "\nPlease enter 1-6 (or 0 to exit): ")
    return int(choice)
if __name__ == "__main__":
    main()