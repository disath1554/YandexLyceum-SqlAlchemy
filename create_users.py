from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# Добавляем users
def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    session.add(user)

    user = User()
    user.surname = "Smit"
    user.name = "Rob"
    user.age = 16
    user.position = "captain's helper"
    user.speciality = "boy"
    user.address = "module_1"
    user.email = "rob@mars.org"
    user.hashed_password = "rob"
    session.add(user)

    user = User()
    user.surname = "Edison"
    user.name = "Alex"
    user.age = 17
    user.position = "doctor's helper"
    user.speciality = "medicine"
    user.address = "module_1"
    user.email = "alex@mars.org"
    user.hashed_password = "alex"
    session.add(user)

    user = User()
    user.surname = "Jordanson"
    user.name = "Bob"
    user.age = 45
    user.position = "doctor"
    user.speciality = "medicine"
    user.address = "module_1"
    user.email = "bob@mars.org"
    user.hashed_password = "bob"
    session.add(user)

    user = User()
    user.surname = "Merlin"
    user.name = "Monro"
    user.age = 30
    user.position = "pilot"
    user.speciality = "pilot"
    user.address = "module_1"
    user.email = "monro@mars.org"
    user.hashed_password = "monro"
    session.add(user)

    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
