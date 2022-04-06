import random
import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US9 (Analytical): As a company, I want to see how many people follow a 
user and how many people they follow so that I know which users have a larger 
social media presence.\n''')

#finds following and follower stats for a specific user
def follow_stats(user_id):
    followers = ''
    following = ''

    #find how many users follow the specific user
    followers_query = '''
    SELECT count(follower_username)
      FROM Followings
     WHERE (followee_username = %s)
    '''
    cur.execute(followers_query, (user_id,))
    rows = cur.fetchall()
    for row in rows:
        followers = row[0]


    #find how many users followed
    following_query = '''
    SELECT count(followee_username)
      FROM Followings
     WHERE (follower_username = %s)    
    '''
    cur.execute(following_query, (user_id,))
    rows = cur.fetchall()
    for row in rows:
        following = row[0]
    

    table = PrettyTable(['Followers', 'Following'])
    table.add_row((followers, following))
    print('User:', user_id)
    print(table)
    print('\n')

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

#test with 10 random user from list
for i in range(10):
    name = random.choice(n)
    follow_stats(name)