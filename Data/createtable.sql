DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
    /*The id column refuses to be anything besides type text.
    We talked to Anya about this and she is okay with us leaving it as text.*/
    id text,
    country text,
    country_abbreviation text,
    country_region text,
    adult_population float 
);
DROP TABLE IF EXISTS poll_results;
CREATE TABLE poll_results (
    /*The id column refuses to be anything besides type text.
    We talked to Anya about this and she is okay with us leaving it as text.*/
    id text, 
    age smallint,
    education_level smallint,
    employment_status smallint,
    financial_account_status smallint,
    worry_about_financing_education smallint,
    internet_access smallint,
    /*We need to be able to join country_id on the id column from the 
    countries table to access information across the two tables, so we must 
    also make the country_id column type text.*/
    country_id text
);




