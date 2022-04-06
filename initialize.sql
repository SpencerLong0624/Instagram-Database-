\c postgres
DROP DATABASE IF EXISTS ig_project;

CREATE database ig_project;
\c ig_project

\i ig_project_create.SQL


\copy Users(username, legal_name, biography, location) FROM 'users.csv'   csv header

\copy Mediums(medium_id, posted_by_username) FROM 'mediums.csv'   csv header 

\copy Hashtags(hashtag_name) FROM 'hashtags.csv'   csv header

\copy Posts(post_medium_id, post_caption) FROM 'posts.csv'   csv header

\copy Reels(reel_medium_id, reel_caption, reel_length) FROM 'reels.csv'   csv header

\copy Stories(story_medium_id, story_length) FROM 'stories.csv'   csv header

\copy Associations(association_medium_id, association_hashtag_name) FROM 'associations.csv'   csv header

\copy Likes(like_id, like_medium_id, liked_by) FROM 'likes.csv'   csv header

\copy Consumer_Goods_Companies(company_username) FROM 'companies.csv'   csv header

\copy Brand_Ambassadors(ambassador_username) FROM 'ambassadors.csv'   csv header

\copy Casual_Viewers(viewer_username) FROM 'viewers.csv'   csv header

\copy Followings(follower_username, followee_username) FROM 'followings.csv'   csv header