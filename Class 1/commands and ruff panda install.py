# 1. create the environment (once per project)
$ python -m venv .venv

# 2. activate it (every time you open a new terminal)
$ source .venv/bin/activate        # macOS / Linux
$ .venv\Scripts\activate           # Windows
(.venv) $                          # the prompt shows you're inside

# 3. install what the project needs
(.venv) $ pip install ruff pandas

# 4. record exact versions so others can rebuild it
(.venv) $ pip freeze > requirements.txt
(.venv) $ cat requirements.txt
pandas==2.2.3
ruff==0.6.9
...

# 5. on another laptop (or after deleting .venv)
$ python -m venv .venv && source .venv/bin/activate
(.venv) $ pip install -r requirements.txt

# leave the environment
(.venv) $ deactivate