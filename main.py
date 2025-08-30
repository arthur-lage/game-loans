from db import Database
from ui import UI
    
def main ():
    opt = None

    db = Database("database.db")
    db.init()
    db.fill_mock_data()

    while(opt != 0):
        UI.show_options()
        opt = int(input("\nOption: "))

        match(opt):
            case 0:
                print("Exiting session...")
            case 1:
                for el in db.get_users():
                    print(el)
            case 2:
                for el in db.get_games():
                    print(el)
            case 3:
                for el in db.get_loans():
                    print(el)
            case 4:
                print("\nCreating new user...")
                
                name = input("User's name: ")        
                email = input("User's email: ")        
                birthdate = input("User's birthdate: ")        
                phone_number = input("User's phone number: ")        

                db.add_user(name, email, birthdate, phone_number)
            case 5:
                print("\nCreating new game...")
                
                title = input("Game title: ")        
                genre = input("Game genre: ")        
                year = int(input("Game release year: "))        

                db.add_game(title, genre, year)
            case 6:
                print("\nCreating new loan...")
                
                email = input("User email: ")
                user_id = None

                try:
                    user = db.find_user_by_email(email)
                    print(user)
                    if user:
                        user_id = user["id"]
                    else:
                        print("User not found.")
                        continue
                except Exception as e:
                    print(f"An error ocurred while searching for user with email '{email}': " + repr(e))
                    continue

                game_id = int(input("Game id: "))       
                return_until = input("The game must be returned until the day: ")        

                db.add_loan(user_id, game_id, return_until)
            case 7:
                print("\nReturning game...")
                
                user_id = None
                email = input("User's email: ")

                try:
                    user = db.find_user_by_email(email)
                    print(user)
                    if user:
                        user_id = user["id"]
                    else:
                        print("User not found.")
                        continue
                except Exception as e:
                    print(f"An error ocurred while searching for user with email '{email}': " + repr(e))
                    continue

                loans = db.find_loans_by_user_id(user_id)
                
                for loan in loans:
                    print(f"{loan["id"]} - {loan["game_title"]}")

                print("Choose game to be returned: ")
                game_id = int(input("Game ID: "))

                current_loan = db.find_active_loan_by_game_id_and_user_id(user_id, game_id)[0]
                print(current_loan)

                if not current_loan:
                    print("No loans found for this game.")
                    continue

                if current_loan["is_returned"] == 0:
                    db.return_game(current_loan["id"])

    db.close()

if __name__ == "__main__":
    main()