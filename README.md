To run project:
Step 1:
    install mosquittoMQTT
Step 2:
    activate environment
Step 3:
    install all requirements in requirements.txt
Step 4: Run project with command
    python3 manage.py runserver --noreload "<your IP>":8000
To publish mqtt message:
    run script mosquittoMQTTPub.py with option --server_ip, --port
    default is localhost and 1883