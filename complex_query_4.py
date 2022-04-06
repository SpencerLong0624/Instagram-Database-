import random
import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US10 (Complex): As a company, I want to know the most popular location 
demographic of users who liked a specific post so that I know what area I should
target to promote my consumer goods.\n''')

#finds the top city of users who liked a post
def location_demographic(medium):
    query = '''
      SELECT location, count(username)
        FROM Likes
             JOIN Users ON username = liked_by
       WHERE (like_medium_id = %s)
    GROUP BY location
    ORDER BY count(username) DESC
    LIMIT 1
    '''
    cur.execute(query, (medium,))
    rows = cur.fetchall()
    city = ''
    cnt = ''
    for row in rows:
        city = row[0]
        cnt = ' (' + str(row[1]) + ' users' + ')'
    res = city + cnt
    print('Post', medium, 'was liked the most by users in', res)

#test random mediums
for i in range(20):
    num = random.randint(1, 50)
    location_demographic(num)