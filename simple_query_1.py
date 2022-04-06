import random
import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US1 (Simple): As a brand ambassador, I want to see the people who liked one of 
my specific mediums so that I have an idea of my target demographics.\n''')

# This function will find who liked a certain medium.
def who_liked_post(medium):
    query = '''
    SELECT liked_by  -- selects users who liked the post
      FROM Likes
     WHERE (like_medium_id = %s)    -- filters by each liked medium
    '''

# Executes the function using the query and medium input from who_like_post function
    cur.execute(query, (medium,))
    rows = cur.fetchall()
# Creates organized table with single column Liked By
    table = PrettyTable(['Liked By'])
# Loops over rows and prints each medium
    for row in rows:
        table.add_row(row)
    print('Medium: '+ str(medium))
    print(table)
    
# Test case that selects 20 random users from 0-50 and shows who liked their specific medium.
for i in range(20):
    n = random.randint(1, 50)
    who_liked_post(n)

        

