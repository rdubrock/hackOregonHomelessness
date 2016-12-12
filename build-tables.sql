
\connect portlandhomelesstally
DROP SCHEMA IF EXISTS homeless CASCADE;
CREATE SCHEMA homeless
    CREATE TABLE HistoryPitSummary (
        "id" serial NOT NULL PRIMARY KEY,
        "Table" VARCHAR(17) NOT NULL,
        "Population" VARCHAR(40) NOT NULL,
        "SubPopulation" VARCHAR(40) NOT NULL,
        "Date" DATE NOT NULL,
        "Value" NUMERIC(7,2))
    CREATE TABLE PitSubpopulations (
        "id" serial NOT NULL PRIMARY KEY,
        "Table" VARCHAR(18) NOT NULL,
        "Population" VARCHAR(67) NOT NULL,
        "Shelter" VARCHAR(40) NOT NULL,
        "Date" DATE NOT NULL,
        "Value" NUMERIC(7,2))
    CREATE TABLE HistoryHic (
        "id" serial NOT NULL PRIMARY KEY,
        "Table" VARCHAR(23) NOT NULL,
        "Shelter" VARCHAR(40) NOT NULL,
        "UnitBed" VARCHAR(40) NOT NULL,
        "Date" DATE NOT NULL,
        "Value" NUMERIC(7,2));

COPY homeless.HistoryPitSummary ("Table", "Population", "SubPopulation", "Date", "Value")
    FROM '/home/vagrant/proj/data/HistoryPitSummary.csv'
        WITH(FORMAT CSV, HEADER);
COPY homeless.PitSubpopulations ("Table", "Population", "Shelter", "Date", "Value")
    FROM '/home/vagrant/proj/data/PITSubpopulations.csv'
        WITH(FORMAT CSV, HEADER);
COPY homeless.HistoryHic ("Table", "Shelter", "UnitBed", "Date", "Value")
    FROM '/home/vagrant/proj/data/HistoryHic.csv'
 	      WITH(FORMAT CSV, HEADER);
