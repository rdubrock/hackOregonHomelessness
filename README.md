# hackOregonHomelessness

### Troy's Notes

1. Adjusted Vagrantfile to include port forwarding 8000/8001 to Vagrantfile
2. Created database user 'dbuser/password123'
3. Created database 'portlandhomelesstally'
4. Adjusted spreadsheet / csv files to use numeric values
5. Adjusted build-tables.sql to include PRIMARY KEYs and NUMERIC data types for values
6. Created Django app 'tallyapp' for implementation of the API
7. Created Django superuser 'admin/password123'
9. Default views from the host OS's web browser:
    localhost:8001/admin
9. GET of JSON data from host OS Postman:
    localhost:8001/pit
