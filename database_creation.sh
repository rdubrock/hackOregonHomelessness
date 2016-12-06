psql
CREATE USER vagrant with CREATEUSER;
ALTER USER vagrant PASSWORD 'vagrant';
CREATE database homelesness;
CREATE EXTENSION plpython3u
CREATE SCHEMA homelesness;

#COPY education.schools FROM '/home/vagrant/proj/schools_original.csv'
#  WITH(FORMAT CSV, HEADER);

#CREATE TABLE education.performance (
#    DistrictID INTEGER NOT NULL,
#    District VARCHAR32 NOT NULL,
#    SchoolID INTEGER NOT NULL,
#    School VARCHAR NOT NULL,
#    AcademicYear INTEGER NOT NULL,
#    Subject VARCHAR NOT NULL,
#    Subgroup VARCHAR NOT NULL,
#    GradeLevel VARCHAR NOT NULL,
#    ParticipationRate2014to2015 FLOAT,
#    PercentageMeetsORExceeds2014to2015 FLOAT
#);

#COPY education.schools FROM '/home/vagrant/proj/performance_original.csv' 
#WITH(FORMAT CSV, HEADER);
