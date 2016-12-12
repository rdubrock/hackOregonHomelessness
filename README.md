# hackOregonHomelessness

## How to Setup the Hack Oregon Homeless Tally REST API

1) From host OS:

"""
$ vagrant up
$ vagrant ssh
"""

2) From guest OS:

"""
$ cd proj
$ source activate cvdjango
$ ./manage.py createsuperuser # optional if you want to see the admin interface from a browser
$ ./manage.py runserver 0.0.0.0:8000
"""

3) From host OS, run Postman GET/POST:

    """
    localhost:8001/pit
    localhost:8001/pitsub
    localhost:8001/hic
    """

4) From host OS, run Postman GET/PUT/DELETE:

    """
    localhost:8001/pit/<pk>
    localhost:8001/pitsub/<pk>
    localhost:8001/hic/<pk>
    """

    where <pk> is a primary key

5) Default views from the host OS's web browser:

    """
    localhost:8001/admin
    """


### Notes
troys DEC2016
1. Adjusted Vagrantfile to include port forwarding 8000/8001 to Vagrantfile
2. Created database user 'dbuser/password123'
3. Created database 'portlandhomelesstally'
4. Adjusted spreadsheet / csv files to use numeric values
5. Adjusted build-tables.sql to include PRIMARY KEYs and NUMERIC data types for values
6. Created Django app 'tallyapp' for implementation of the API
7. Created Django superuser 'admin/password123'
