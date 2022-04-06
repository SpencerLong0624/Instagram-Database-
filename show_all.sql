\c ig_project


\echo "Users Table"
\echo "Contains Account information for each user"
SELECT * FROM Users;

\echo "Mediums Table"
\echo "Contains information about the user who posted a medium"
SELECT * FROM Mediums;

\echo "Hashtags Table"
\echo "Contains the names of all the hashtags"
SELECT * FROM Hashtags;

\echo "Posts Table"
\echo "Contains the contents of posts"
SELECT * FROM Posts;

\echo "Reels Table"
\echo "Contains the contents of reels"
SELECT * FROM Reels;

\echo "Stories Table"
\echo "Contains the contents of stories"
SELECT * FROM Stories;

\echo "Associations Table"
\echo "Contains all the mediums associated with a hashtag"
SELECT * FROM Associations;

\echo "Likes Table"
\echo "Contains all the mediums that have been liked by users"
SELECT * FROM Likes;

\echo "Companies Table"
\echo "Contains all the users that are consumer goods companies"
SELECT * FROM Consumer_Goods_Companies;

\echo "Ambassadors Table"
\echo "Contains all the users that are brand ambassadors"
SELECT * FROM Brand_Ambassadors;

\echo "Viewers Table"
\echo "Contains all the users that are casual viewers"
SELECT * FROM Casual_Viewers;

\echo "Followings Table"
\echo "Contains all the accounts that users follow"
SELECT * FROM Followings;