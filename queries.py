queries = {
    "CreateUsersTable": "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR(60) NOT NULL, email VARCHAR(50) UNIQUE NOT NULL, birthdate DATETIME NOT NULL, phone_number VARCHAR(25) UNIQUE, created_at DATETIME DEFAULT CURRENT_TIMESTAMP);",
    "CreateGamesTable": "CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, title VARCHAR(60) NOT NULL, genre VARCHAR(30) NOT NULL, year INTEGER, created_at DATETIME DEFAULT CURRENT_TIMESTAMP);",
    "CreateLoansTable": "CREATE TABLE IF NOT EXISTS loans (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, game_id INTEGER NOT NULL, borrowed_at DATETIME DEFAULT CURRENT_TIMESTAMP, return_until DATETIME, is_returned BOOLEAN DEFAULT FALSE, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (game_id) REFERENCES games(id));",
    "GetUsers": "SELECT * FROM users",
    "GetGames": "SELECT * FROM games",
    "GetLoans": "SELECT u.name as User, u.email as Email, g.title as 'game_title', g.genre, g.year as 'game_released', l.borrowed_at, l.return_until, l.is_returned FROM loans l JOIN users u ON l.user_id = u.id JOIN games g ON l.game_id = g.id WHERE is_returned = 0;",
    "FindLoansByUserId": "SELECT loans.id, loans.game_id, loans.user_id, games.title as 'game_title' FROM loans JOIN (games) ON loans.game_id = games.id WHERE user_id = ?",
    "FindActiveLoansByGameIdAndUserId": "SELECT * FROM loans WHERE user_id = ? AND game_id = ? AND is_returned = 0",
    "FindUserByEmail": "SELECT * FROM users WHERE email = ?",
    "AddUser": "INSERT INTO users (name, email, birthdate, phone_number) VALUES(?, ?, ?, ?);",
    "AddGame": "INSERT INTO games (title, genre, year) VALUES(?, ?, ?);",
    "AddLoan": "INSERT INTO loans (user_id, game_id, return_until) VALUES(?, ?, ?);",
    "UpdateLoanReturnGame": "UPDATE loans SET is_returned = 1 WHERE id = ?"
}