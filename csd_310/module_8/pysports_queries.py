cursor = db.cursor()

cursor.execute(“SELECT team_id, team_name, mascot FROM team”)

teams = cursor.fetchall()

for team in teams:
print(“Team Name: {}”.format(team[1]))