from project_2.database import db
from project_2 import models
from project_2 import create_app

if __name__ == "__main__":
    fake_app = create_app()

    with fake_app.test_request_context():

        db.create_all()
