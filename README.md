Early February Update: The most intereting thing about this experiment was using websockets for instant upates for any computer in the network accessing this web-app. 

It was gruelling but fun to get this app hosted on an Apache linux server with a cheap laptop and available on the local wi-fi network. I'll look back on this project in a few years and probably see it as a massive watershed moment for me. 

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
