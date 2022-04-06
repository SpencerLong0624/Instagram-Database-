import random
import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US2 (Analytical): As a brand ambassador, I want to to be able to 
see how many likes I get on a medium so that I can know what content my followers like the most.\n''')

# This function counts the number of likes on a user's medium
def number_likes(medium):
    query = '''
    SELECT count(like_id)    -- counts the number of likes 
      FROM Likes
     WHERE (like_medium_id = %s)    -- filters by each specifically liked medium
    '''
# Executes the function using the query and the input medium from the number_likes function.
    cur.execute(query, (medium,))
    rows = cur.fetchall()

# Loops through each row and prints how many likes each medium has
    for row in rows:
        s = 'Medium ' + str(medium) + ' has ' + str(row[0]) + ' likes.'
        print(s)

# Test case of 30 users randomly selected between 1-50 and returns the number of likes on a medium for each.
for i in range(30):
    n = random.randint(1, 50)
    number_likes(n)
