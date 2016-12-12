# hackOregonHomelessness

### Troy's Notes

1. Adjusted Vagrantfile to include port forwarding 8000/8001 to Vagrantfile
2. Created database user 'dbuser/password123'
3. Created database 'portlandhomelesstally'
4. Adjusted build-tables.sql to include PRIMARY KEYs
5. Created Django app 'tallyapp' for implementation of the API
6. Created Django superuser 'admin/password123'
7. Default views from the host OS's web browser:
    localhost:8001/admin
8. GET of JSON data from host OS Postman:
    localhost:8001/pit
