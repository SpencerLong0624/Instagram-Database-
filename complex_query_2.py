import random
import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US4 (Complex): As a brand ambassador, I want to to see the most liked 
medium of each user so that I know what audience of each user tailors to.\n''')

#finds the most liked medium for every user
def most_liked():
    query = '''
      SELECT username, medium_id, count(like_id) as Like_Count
        FROM Users
             JOIN Mediums ON posted_by_username = username
             JOIN Likes ON like_medium_id = medium_id
    GROUP BY username, medium_id
    --filter by most liked post of user
      HAVING medium_id = ( SELECT m.medium_id
                             FROM Mediums as m
                                  JOIN Likes as l ON like_medium_id = medium_id
                            WHERE (m.posted_by_username = username)
                         GROUP BY m.medium_id
                         ORDER BY count(l.like_id) DESC
                            LIMIT 1) 
    ORDER BY username ASC               
    '''
    cur.execute(query)
    rows = cur.fetchall()
    table = PrettyTable(['username', 'medium_id', 'Like_Count'])
    for row in rows:
        table.add_row(row)
    print(table)

most_liked()
