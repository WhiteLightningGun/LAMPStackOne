Hello from README, 16/01/2024

Now we use Python3 flask for cross platform windows/linux convenience.

Scribbled notes for my convenience:

The go command is: flask run

You will need to set local environment variables in a .env file. For the moment it need only contain: "FLASK_APP=main.py"

To activate the local Python environment on Windows: .\venv\Scripts\activate  
or Unix: source venv/bin/activate

Installing for the first time?

python3 -m venv venv
followed by:
pip install -r requirements.txt

Update dependencies list after adding a module with: pip freeze > requirements.txt
