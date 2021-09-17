# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'

    username = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)

    def get(self):
        return {
            "id": self.username,
            "email": self.email,
            "mobile": self.mobile,
            "position": {
                "title": self.title,
                "department": self.department
            }
        }

