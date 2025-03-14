import sqlite3
from Team import Team

#Перш за все створюємо підключення з базою
db_conn = sqlite3.connect('db')

# Створити SQL комманду
cmd_teams_sql = '''SELECT * FROM Team'''

# Створити курсор 
cursor_cmd = db_conn.cursor()
cursor_cmd.execute(cmd_teams_sql)

# Виводимо на екран всі команди
teams = []
results = cursor_cmd.fetchall()
for team_row in results:
    team = Team(team_row[0], team_row[1], team_row[2])
    teams.append(team)

for team in teams:
    print(team)

# Додавання об'єктів до бази
permit = True
add_team = input('Введіть команду для додавання: ')
cursor_cmd.execute(f"INSERT INTO Team('Name') VALUES('{add_team}')")
db_conn.commit()

delete_team = input('Введіть команду для додавання: ')
cursor_cmd.execute(f"DELETE FROM Team WHERE name = '{delete_team}'")
# Закриття бази даних
db_conn.close()


