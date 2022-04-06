import random
import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US5 (Simple): As a casual user, I want to see all the mediums of a user 
in one screen so that I can easily see what they post about.\n''')

# This function shows all the mediums of a user 
def user_homepage(user_id):
    query = '''
    SELECT medium_id   -- selects each medium
      FROM Mediums
     WHERE (posted_by_username = %s)    -- filters by user who posted the medium
    '''

# Executes function using query and  input, user id.
    cur.execute(query, (user_id,))
    rows = cur.fetchall()

# Creates an organized table of the table with one row "User Mediums" 
    table = PrettyTable(['User Mediums'])
    for row in rows:
        table.add_row(row)
    print('User: '+ user_id)
    print(table)

# Test users for test cases
n = [
'spencerlongg',
'aadenuga',
'jenny123',
'raja',
'ambnoelle',
'noahv24',
'tyler_sp',
'varun.baldwa',
'maddyroe',
'punx2_l',
'isaiahbowes',
'lisaa.og',
'farabakare',
'gucci',
'itsconel',
'k.lovato',
'caitlyn_karis',
'bbybellz',
'welcomeovo',
'nayaahbenet'
]

# Randomly chooses user out of range 16 and returns all the mediums on their page
for i in range(16):
    name = random.choice(n)
    user_homepage(name)