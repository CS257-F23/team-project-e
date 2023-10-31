DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
    id text,
    country text,
    country_abbreviation text,
    country_region text,
    adult_population text
);
DROP TABLE IF EXISTS poll_results;
CREATE TABLE poll_results (
    id text,
    age text,
    education_level text,
    employment_status text,
    financial_account_status text,
    worry_about_financing_education text,
    internet_access text,
    country_id text
)