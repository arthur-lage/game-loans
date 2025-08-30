queries = {
    "CreateUsersTable": "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR(60) NOT NULL, email VARCHAR(50) UNIQUE NOT NULL, birthdate DATETIME NOT NULL, phone_number VARCHAR(25) UNIQUE, created_at DATETIME DEFAULT CURRENT_TIMESTAMP);",
    "CreateGamesTable": "CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, title VARCHAR(60) NOT NULL, genre VARCHAR(30) NOT NULL, year INTEGER, created_at DATETIME DEFAULT CURRENT_TIMESTAMP);",
    "CreateLoansTable": "CREATE TABLE IF NOT EXISTS loans (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, game_id INTEGER NOT NULL, borrowed_at DATETIME DEFAULT CURRENT_TIMESTAMP, return_until DATETIME, is_returned BOOLEAN DEFAULT FALSE, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (game_id) REFERENCES games(id));",
    "GetUsers": "SELECT * FROM users",
    "GetGames": "SELECT * FROM games",
    "GetLoans": "SELECT u.name as User, u.email as Email, g.title as 'Game Title', g.genre as 'Genre', g.year as 'Released on', l.borrowed_at as 'Borrowed at', l.return_until as 'Must Return Until', l.is_returned as 'Returned?' FROM loans l JOIN users u ON l.user_id = u.id JOIN games g ON l.game_id = g.id;",
    "FindUserByEmail": "SELECT * FROM users WHERE email = ?",
    "AddUser": "INSERT INTO users (name, email, birthdate, phone_number) VALUES(?, ?, ?, ?);",
    "AddGame": "INSERT INTO games (title, genre, year) VALUES(?, ?, ?);",
    "AddLoan": "INSERT INTO loans (user_id, game_id, return_until) VALUES(?, ?, ?);",
}