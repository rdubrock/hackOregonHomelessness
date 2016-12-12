
\connect portlandhomelesstally
DROP SCHEMA IF EXISTS homeless CASCADE;
CREATE SCHEMA homeless
    CREATE TABLE HistoryHic (
        "id" serial NOT NULL PRIMARY KEY,
        "UnitBedType" VARCHAR(17) NOT NULL,
        "ShelterType" VARCHAR(32) NOT NULL,
        "Date" DATE NOT NULL,
        "Value" VARCHAR(11))
    CREATE TABLE HistoryPitSummary (
        "id" serial NOT NULL PRIMARY KEY,
        "Table" VARCHAR(17) NOT NULL,
        "Population" VARCHAR(32) NOT NULL,
        "Sub-Population" VARCHAR(37) NOT NULL,
        "Date" DATE NOT NULL,
        "Value" VARCHAR(11));
COPY homeless.HistoryPitSummary ("Table", "Population", "Sub-Population", "Date", "Value")
    FROM '/home/vagrant/proj/data/HistoryPitSummary.csv'
        	WITH(FORMAT CSV, HEADER);

--- troys 11DEC HistoryHic.csv needs to reorient the records
--- COPY homeless.HistoryHic FROM '/home/vagrant/proj/data/HistoryHic.csv'
--- 	WITH(FORMAT CSV, HEADER);
