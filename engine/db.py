import sqlite3
from config import DATABASE_NAME

conn = sqlite3.connect(DATABASE_NAME)
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUEs (null, 'word', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')"
# query = "INSERT INTO sys_command VALUEs (null, 'excel', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE')"
# query = "INSERT INTO sys_command VALUEs (null, 'discord', 'C:\\Users\\danil\\AppData\\Local\\Discord\\app-1.0.9168\\Discord.exe')"
# cursor.execute(query)
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUEs (null, 'mail', 'https://mail.google.com/mail?hl=en')"
# query = "INSERT INTO web_command VALUEs (null, 'cabinet', 'https://cabinet.sumdu.edu.ua/')"
# query = "INSERT INTO web_command VALUEs (null, 'mix', 'https://mix.sumdu.edu.ua')"
# query = "INSERT INTO web_command VALUEs (null, 'git', 'https://github.com/')"
# cursor.execute(query)
# conn.commit()