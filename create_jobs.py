from data.jobs import Jobs
from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# Первая работа

def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'cleaning of the corridor'
    job.work_size = 10
    job.collaborators = '3, 4'
    job.is_finished = True

    session.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'washing test tubes'
    job.work_size = 30
    job.collaborators = '2, 4'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 4
    job.job = 'catching mice'
    job.work_size = 14
    job.collaborators = '3, 5'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 5
    job.job = 'reading fairy tales'
    job.work_size = 10
    job.collaborators = '4'
    job.is_finished = True


    session.add(job)

    session.commit()


if __name__ == '__main__':
    main()
