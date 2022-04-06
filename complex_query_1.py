import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='ig_project', user='isdb')
con.autocommit = True
cur = con.cursor()

print('''US3 (Complex): As a brand ambassador, I want to have my posts 
automatically be posted on my story when I make a new post so that my followers
will have multiple places to see my new content.\n''')

#prints post table
def print_posts():
  query = '''
    SELECT *
      FROM Posts
  ORDER BY post_medium_id DESC
     LIMIT 5
  '''
  cur.execute(query)
  rows = cur.fetchall()
  table = PrettyTable(['post_medium_id', 'post_caption'])
  for row in rows:
    table.add_row(row)
  print(table)

#prints story table
def print_stories():
  tmp = '''
    SELECT *
      FROM Stories
  ORDER BY story_medium_id DESC
     LIMIT 5
  '''
  cur.execute(tmp)
  rows = cur.fetchall()
  table = PrettyTable(['story_medium_id', 'story_length'])
  for row in rows:
    table.add_row(row)
  print(table)

#insert new row into medium and post table based on command line input
def insert_post():
  print('For the purpose of the demo, pick the user as either:')
  print('spencerlongg')
  print('aadenuga')
  user = input('User: ')
  cap = input('Caption: ')

  #find next medium_id to use
  find_max = '''
  SELECT max(medium_id)
    FROM Mediums
  '''
  cur.execute(find_max)
  rows = cur.fetchall()
  num = None
  for row in rows:
    num = row[0]
  num += 1

  q = '''
  INSERT INTO Mediums (medium_id, posted_by_username)
    VALUES (%s, %s);
  INSERT INTO Posts (post_medium_id, post_caption)
    VALUES (%s, %s);
  '''
  cur.execute(q, (num, user, num, cap))


#trigger function and trigger to add to story when a post is made
def automatic_story_post():
  tmpl = '''
  DROP TRIGGER IF EXISTS tr_post_story ON Posts;
  DROP FUNCTION IF EXISTS fn_post_story();

  CREATE FUNCTION fn_post_story()
  RETURNS trigger
  LANGUAGE plpgsql AS
  $$
  DECLARE
      user_id text := (SELECT posted_by_username
                         FROM Posts
                              JOIN Mediums ON medium_id = post_medium_id
                        WHERE (medium_id = new.post_medium_id));
  BEGIN 
      INSERT INTO Mediums (medium_id, posted_by_username)
        VALUES (new.post_medium_id + 1, user_id);

      INSERT INTO Stories (story_medium_id, story_length)
        VALUES (new.post_medium_id + 1, 0.25);
      return NULL;
  END;
  $$;

  CREATE TRIGGER tr_post_story 
  AFTER INSERT ON Posts
  FOR EACH ROW
    EXECUTE FUNCTION fn_post_story();
  '''

  print('At first, there are no new posts or stories.\n')
  print_posts()
  print_stories()
  print('We will now add a new post.\n')
  insert_post()
  cur.execute(tmpl)
  print('You will now see that we have a story and posts.\n')
  print_posts()
  print_stories()

automatic_story_post()
  
