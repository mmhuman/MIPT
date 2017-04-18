CREATE TABLE contestants (
    id serial PRIMARY KEY,
    name text,
    cf_profile text,
    tc_profile text,
    country text,
    organization text
);

CREATE TABLE teams (
    id serial PRIMARY KEY,
    name text UNIQUE NOT NULL,
    rating real NOT NULL DEFAULT 0,
    contest_cnt integer NOT NULL DEFAULT 0,
    member_1 serial REFERENCES contestants (id),
    member_2 serial REFERENCES contestants (id),
    member_3 serial REFERENCES contestants (id),
    country text,
    organization text
);

CREATE TABLE teams_aliases (
    id serial PRIMARY KEY,
    name text UNIQUE NOT NULL,
    team_id serial REFERENCES teams (id)
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
    contest_id serial NOT NULL REFERENCES contests (id),
    team_id serial REFERENCES teams (id),
    place integer,
    problems_solved integer,
    team_name text NOT NULL,
    CHECK(place >= 1),
    CHECK(problems_solved >= 0)
);


CREATE INDEX contestants_names ON contestants (name);

CREATE INDEX teams_aliases_names ON teams_aliases (name);

CREATE INDEX contests_titles ON contests (title);

CREATE INDEX contests_results_contest_id ON contests_results (contest_id);

