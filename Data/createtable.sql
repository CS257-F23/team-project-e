DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
    country text,
    country_abbreviation text,
    country_region text,
    id serial,
)

DROP TABLE IF EXISTS poll_results;
CREATE TABLE poll_results (
    adult_population text,
    age text,
    education_level text,
    employment_status text,
    financial_account_status text,
    worry_about_financing_education text,
    internet_acess text,
    id serial,
    country_id int
)