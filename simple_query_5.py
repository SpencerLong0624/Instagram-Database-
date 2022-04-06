import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US8 (Simple): As a company, I want to see what mediums are under a 
hashtag so that I can know what type of people my products sell to.\n''')

#finds the different mediums assocaited with a hashtag
def show_hashtag_mediums(hashtag):
    print('#'+ hashtag)

    #find posts associated with hastag
    post_query = '''
    SELECT post_medium_id, post_caption
      FROM Hashtags
           JOIN Associations ON association_hashtag_name = hashtag_name
           JOIN Posts ON post_medium_id = association_medium_id
     WHERE (hashtag_name = %s)
    '''
    cur.execute(post_query, (hashtag,))
    rows = cur.fetchall()
    table = PrettyTable(['ID', 'Caption'])
    #if no posts found do not print
    if rows:
        for row in rows:
            table.add_row(row)
        print('Posts')
        print(table)

    #find reels associated with hastag
    reel_query = '''
    SELECT reel_medium_id, reel_caption, reel_length
      FROM Hashtags
           JOIN Associations ON association_hashtag_name = hashtag_name
           JOIN Reels ON reel_medium_id = association_medium_id
     WHERE (hashtag_name = %s)
    '''
    cur.execute(reel_query, (hashtag,))
    rows = cur.fetchall()
    table = PrettyTable(['ID', 'Caption', 'Length (minutes)'])
    #if no posts found do not print
    if rows:
        for row in rows:
            table.add_row(row)
        print('Reels')
        print(table)

    #find stories associated with hashtag
    story_query = '''
    SELECT story_medium_id, story_length
      FROM Hashtags
           JOIN Associations ON association_hashtag_name = hashtag_name
           JOIN Stories ON story_medium_id = association_medium_id
     WHERE (hashtag_name = %s)
    '''
    cur.execute(story_query, (hashtag,))
    rows = cur.fetchall()
    table = PrettyTable(['ID', 'Length (minutes)'])
    #if no posts found do not print
    if rows:
        for row in rows:
            table.add_row(row)
        print('Stories')
        print(table)
    
    print('\n')

h = [
'thaifood',
'fashionnova',
'explorepage',
'idgaf',
'evileye',
'houseofhighlights'    
]

#test with every hashtag in DB
for tag in h:
    show_hashtag_mediums(tag)
