CREATE TABLE teams (
    id serial PRIMARY KEY,
    name text UNIQUE NOT NULL,
    rating real NOT NULL DEFAULT 0,
    contest_cnt integer NOT NULL DEFAULT 0,
    member_1 serial,
    member_2 serial,
    member_3 serial,
    country text,
    organization text
);

CREATE TABLE teams_aliases (
    id serial PRIMARY KEY,
    name text UNIQUE NOT NULL,
    team_id serial
);

CREATE TABLE contestants (
    id serial PRIMARY KEY,
    name text,
    cf_profile text,
    tc_profile text,
    country text,
    organization text
);

CREATE TABLE contests (
    id serial PRIMARY KEY,
    title text UNIQUE NOT NULL,
    date timestamp with time zone DEFAULT current_timestamp,
    description text,
    participants integer NOT NULL,
    max_problems_solved integer NOT NULL,
    CHECK(participants >= 0),
    CHECK(max_problems_solved >= 0)
);

CREATE TABLE contests_results (
    id serial PRIMARY KEY,
    contest_id serial NOT NULL,
    team_id serial,
    place integer,
    problems_solved integer,
    team_name text NOT NULL,
    CHECK(place >= 1),
    CHECK(problems_solved >= 0)
);



