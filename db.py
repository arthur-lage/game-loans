import sqlite3
from queries import queries


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Database:
    def __init__(self, name):
        con = sqlite3.connect(name)
        con.row_factory = dict_factory
        self.con = con
        self.cur = self.con.cursor()
    
    def init(self):
        self.cur.execute(queries["CreateUsersTable"])
        self.cur.execute(queries["CreateGamesTable"])
        self.cur.execute(queries["CreateLoansTable"])

    def fill_mock_data(self):
        try:
            self.cur.execute("INSERT INTO users (name, email, birthdate, phone_number) VALUES ('Donna', 'donna@gmail.com', '03-29-2006 9:00:00', '+551112341234')")
            self.cur.execute("INSERT INTO users (name, email, birthdate, phone_number) VALUES ('Mark', 'mark@gmail.com', '07-21-2003 9:00:00', '+551112344321')")
            self.cur.execute("INSERT INTO users (name, email, birthdate, phone_number) VALUES ('Huron', 'huron@gmail.com', '10-24-2003 9:00:00', '+551112348345')")
            self.con.commit()
            
            self.cur.execute("INSERT INTO games (title, genre, year) VALUES ('League of Legends', 'MOBA', 2009)")
            self.cur.execute("INSERT INTO games (title, genre, year) VALUES ('Mortal Kombat 1', 'Fighting', 2024)")
            self.cur.execute("INSERT INTO games (title, genre, year) VALUES ('Dead By Daylight', 'Horror', 2016)")
            self.con.commit()

            self.cur.execute("INSERT INTO loans (user_id, game_id, return_until) VALUES (1, 1, 10-25-2025)")
            self.cur.execute("INSERT INTO loans (user_id, game_id, return_until) VALUES (1, 2, 11-21-2025)")
            self.cur.execute("INSERT INTO loans (user_id, game_id, return_until) VALUES (2, 3, 12-10-2025)")
            self.con.commit()
        except Exception as e:
            print("An error ocurred while filling mock data:" + repr(e))

    def get_users(self):
        res = self.cur.execute(queries["GetUsers"])
        return res.fetchall()

    def get_games(self):
        res = self.cur.execute(queries["GetGames"])
        return res.fetchall()
    
    def get_loans(self):
        res = self.cur.execute(queries["GetLoans"])
        return res.fetchall()
    
    def find_user_by_email(self, email):
        res = self.cur.execute(queries["FindUserByEmail"], (email,))
        return res.fetchone()

    def add_user(self, name, email, birthdate, phone_number): 
        try:
            self.cur.execute(queries["AddUser"], (name, email, birthdate, phone_number))
            self.con.commit()
        except Exception as e:
            print("Could not create user: " + repr(e))

    def add_game(self, title, genre, year): 
        try:
            self.cur.execute(queries["AddGame"], (title, genre, year))
            self.con.commit()
        except Exception as e:
            print("Could not create game: " + repr(e))

    def add_loan(self, user_id, game_id, return_until):
        try:
            self.cur.execute(queries["AddLoan"], (user_id, game_id, return_until))
            self.con.commit()
        except Exception as e:
            print("Could not create loan: " + repr(e))

    def find_loans_by_user_id(self, user_id) :
        loans = self.cur.execute(queries["FindLoansByUserId"], (user_id,))
        return loans.fetchall()

    def find_active_loan_by_game_id_and_user_id(self, user_id, game_id):
        loans = self.cur.execute(queries["FindActiveLoansByGameIdAndUserId"], (user_id, game_id))
        return loans.fetchall()

    def return_game(self, loan_id):
        try:
            self.cur.execute(queries["UpdateLoanReturnGame"], (loan_id,))
            self.con.commit()
        except Exception as e:
            print("Could not update loan: " + repr(e))


    def close(self):
        self.cur.close()
