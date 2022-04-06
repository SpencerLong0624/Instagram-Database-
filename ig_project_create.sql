-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2021-12-04 22:47:20.469

-- tables
-- Table: Associations
CREATE TABLE Associations (
    association_medium_id int  NOT NULL,
    association_hashtag_name text  NOT NULL,
    CONSTRAINT Associations_pk PRIMARY KEY (association_medium_id,association_hashtag_name)
);

-- Table: Brand_Ambassadors
CREATE TABLE Brand_Ambassadors (
    ambassador_username text  NOT NULL,
    CONSTRAINT Brand_Ambassadors_pk PRIMARY KEY (ambassador_username)
);

-- Table: Casual_Viewers
CREATE TABLE Casual_Viewers (
    viewer_username text  NOT NULL,
    CONSTRAINT Casual_Viewers_pk PRIMARY KEY (viewer_username)
);

-- Table: Consumer_Goods_Companies
CREATE TABLE Consumer_Goods_Companies (
    company_username text  NOT NULL,
    CONSTRAINT Consumer_Goods_Companies_pk PRIMARY KEY (company_username)
);

-- Table: Followings
CREATE TABLE Followings (
    follower_username text  NOT NULL,
    followee_username text  NOT NULL,
    CONSTRAINT Followings_pk PRIMARY KEY (follower_username,followee_username)
);

-- Table: Hashtags
CREATE TABLE Hashtags (
    hashtag_name text  NOT NULL,
    CONSTRAINT Hashtags_pk PRIMARY KEY (hashtag_name)
);

-- Table: Likes
CREATE TABLE Likes (
    like_id int  NOT NULL,
    like_medium_id int  NOT NULL,
    liked_by text  NOT NULL,
    CONSTRAINT Likes_pk PRIMARY KEY (like_id,like_medium_id,liked_by)
);

-- Table: Mediums
CREATE TABLE Mediums (
    medium_id int  NOT NULL,
    posted_by_username text  NOT NULL,
    CONSTRAINT Mediums_pk PRIMARY KEY (medium_id)
);

-- Table: Posts
CREATE TABLE Posts (
    post_medium_id int  NOT NULL,
    post_caption text  NOT NULL,
    CONSTRAINT Posts_pk PRIMARY KEY (post_medium_id)
);

-- Table: Reels
CREATE TABLE Reels (
    reel_medium_id int  NOT NULL,
    reel_caption text  NOT NULL,
    reel_length real  NOT NULL,
    CONSTRAINT Reels_pk PRIMARY KEY (reel_medium_id)
);

-- Table: Stories
CREATE TABLE Stories (
    story_medium_id int  NOT NULL,
    story_length real  NOT NULL,
    CONSTRAINT Stories_pk PRIMARY KEY (story_medium_id)
);

-- Table: Users
CREATE TABLE Users (
    username text  NOT NULL,
    legal_name text  NOT NULL,
    biography text  NOT NULL,
    location text  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (username)
);

-- foreign keys
-- Reference: Associations_Hashtags (table: Associations)
ALTER TABLE Associations ADD CONSTRAINT Associations_Hashtags
    FOREIGN KEY (association_hashtag_name)
    REFERENCES Hashtags (hashtag_name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Associations_Mediums (table: Associations)
ALTER TABLE Associations ADD CONSTRAINT Associations_Mediums
    FOREIGN KEY (association_medium_id)
    REFERENCES Mediums (medium_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Brand_Ambassadors_Users (table: Brand_Ambassadors)
ALTER TABLE Brand_Ambassadors ADD CONSTRAINT Brand_Ambassadors_Users
    FOREIGN KEY (ambassador_username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Casual_Viewers_Users (table: Casual_Viewers)
ALTER TABLE Casual_Viewers ADD CONSTRAINT Casual_Viewers_Users
    FOREIGN KEY (viewer_username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Consumer_Goods_Companies_Users (table: Consumer_Goods_Companies)
ALTER TABLE Consumer_Goods_Companies ADD CONSTRAINT Consumer_Goods_Companies_Users
    FOREIGN KEY (company_username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Followings_Users1 (table: Followings)
ALTER TABLE Followings ADD CONSTRAINT Followings_Users1
    FOREIGN KEY (follower_username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Followings_Users2 (table: Followings)
ALTER TABLE Followings ADD CONSTRAINT Followings_Users2
    FOREIGN KEY (followee_username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Likes_Mediums (table: Likes)
ALTER TABLE Likes ADD CONSTRAINT Likes_Mediums
    FOREIGN KEY (like_medium_id)
    REFERENCES Mediums (medium_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Likes_Users (table: Likes)
ALTER TABLE Likes ADD CONSTRAINT Likes_Users
    FOREIGN KEY (liked_by)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Mediums_Users (table: Mediums)
ALTER TABLE Mediums ADD CONSTRAINT Mediums_Users
    FOREIGN KEY (posted_by_username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Posts_Mediums (table: Posts)
ALTER TABLE Posts ADD CONSTRAINT Posts_Mediums
    FOREIGN KEY (post_medium_id)
    REFERENCES Mediums (medium_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reels_Mediums (table: Reels)
ALTER TABLE Reels ADD CONSTRAINT Reels_Mediums
    FOREIGN KEY (reel_medium_id)
    REFERENCES Mediums (medium_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Stories_Mediums (table: Stories)
ALTER TABLE Stories ADD CONSTRAINT Stories_Mediums
    FOREIGN KEY (story_medium_id)
    REFERENCES Mediums (medium_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

