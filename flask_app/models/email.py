import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email():
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('validation_emails_schema').query_db(query)
        emails = []
        for email in results:
            emails.append(email)
        return emails

    @classmethod
    def add_email(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        connectToMySQL('validation_emails_schema').query_db(query, data)


    @staticmethod
    def validate_email(data):
        is_valid = True
        flash("success")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid