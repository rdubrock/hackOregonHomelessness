CREATE SCHEMA homeless;

DROP TABLE if EXISTS homeless.HistoryPitSummary;

CREATE TABLE homeless.HistoryPitSummary (
        "Table" VARCHAR(17) NOT NULL,
        "Population" VARCHAR(32) NOT NULL,
        "Sub-Population" VARCHAR(37) NOT NULL,
        "Date" DATE NOT NULL,
        "Value" VARCHAR(11)
);

COPY homeless.HistoryPitSummary FROM '/home/vagrant/proj/data/HistoryPitSummary.csv'
	WITH(FORMAT CSV, HEADER);