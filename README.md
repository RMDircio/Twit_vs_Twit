# Twit_vs_Twit
Web app for Twitter predictions from users


# Installation


Clone your existing repo `git clone 'your-repos-title'`
Navigate your directory to your repo `cd 'you-repos-title'`


# Setup


Create a pipenv virtual environment:
`pipenv --python 3.7` - Installs Python 3.7 in VE
`pipenv install Flask Flask-SQLAlchemy Flask-Migrate` - Installs Flask package in VE
`pipenv shell` - Starts the virtual environment

- Migrate the Database
  `FLASK_APP=web_app flask db init`
  `FLASK_APP=web_app flask db migrate`
  `FLASK_APP=web_app flask db upgrade`

# Usage

Run a Flask app:
- Mac:
    `FLASK_APP=web_app flask run`

- Windows:
    `export FLASK_APP=web_app` # one-time thing, to set the environment
    `flask run`
