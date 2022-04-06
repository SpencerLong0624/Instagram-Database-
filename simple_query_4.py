import random
import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US6 (Analytical): As a casual user, I want to see how many mediums I 
have on my profile page so that I know how much content I’ve posted.\n''')


#finds how many mediums a user posts
def show_post(user_id):
    query = '''
    SELECT count(medium_id)
      FROM Mediums
     WHERE (posted_by_username = %s) --filter by mediums postsed by user
    '''
    cur.execute(query, (user_id,))
    rows = cur.fetchall()
    for row in rows:
        if row[0] == 1:
            print('User', user_id, 'has', 1, 'post.') #singular
        else:
            print('User', user_id, 'has', row[0], 'posts.') #plural


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

#test function using 10 random usernames from list
for i in range(10):
    name = random.choice(n)
    show_post(name)