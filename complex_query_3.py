import random
import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US7 (Complex): As a casual user, I want to find the users I follow that  
liked a specific medium that I also liked so that I can see the users that I have things in common with.\n''')

# This function prints the mediums of a user
def print_mediums(user):
    query = '''
    SELECT medium_id  -- shows the mediums of the user
      FROM Mediums
    WHERE (posted_by_username = %s) -- filters by user who posted the medium
    '''
    cur.execute(query, (user, ))
    rows = cur.fetchall()

# Creates an organzied table of Medium Ids
    table = PrettyTable(['Medium ID'])
    for row in rows:
        table.add_row(row)
    print(table)

# This function asks the users to input the user who's mediums they would like to see
def ask():
    print('Usernames: ')
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
    print(n)

# Tells the user to select the user theu would like to view
    print('Select any user')
    u = input('User: ')
    print_mediums(u)

# Tells the user to select the medium they would like to view
    print('Select any medium from the table above.')
    m = input('Medium: ')
    same_likes(u, m)



# This function finds users that liked the same post as the input user.
def same_likes(user, medium):
    query = '''
    SELECT liked_by  -- selects users who liked the post
      FROM Likes
     WHERE (like_medium_id = %s) AND   -- filters by the liked post
           (liked_by IN (SELECT followee_username  -- selects user that the input user follows
                          FROM Followings
                         WHERE (follower_username = %s))) -- filters for users that input user follows
      
    '''
    cur.execute(query, (medium, user))
    rows = cur.fetchall()
    table = PrettyTable(['User ID'])
    for row in rows:
        table.add_row(row)
    print('Users who liked this post: ' + str(medium))
    print(table)

# Calls command line input
ask()


  
