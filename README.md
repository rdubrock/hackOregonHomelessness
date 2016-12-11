# hackOregonHomelessness

### Troy's Notes 10DEC

1. Added port forwarding 8000/8001 to Vagrantfile
2. Created Django app 'tallyapp' for my open implementation of the API
3. Created database 'portlandhomelesstally' that will hold the schema defined by the API
4. Created database user troys/troys with rights to access the databases 'vagrant' and 'portlandhomelesstally'
5. Created Django superuser admin/password123
6. Default views from the host OS's web browser:
    localhost:8001,
    localhost:8001/admin
