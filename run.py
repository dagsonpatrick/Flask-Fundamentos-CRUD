from app import app

#flask db init
#flask db migrate
#flask db upgrade

# pybabel extract -F babel.cfg -o messages.pot app
# pybabel init -i messages.pot -d app/translations -l en
# pybabel compile -d app/translations

if __name__ == "__main__":
    app.run()