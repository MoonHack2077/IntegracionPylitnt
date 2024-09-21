"""
This module contains the configuration for the MySQL database used by the application.

It is used by the models to connect to the database.
"""

import os
from dotenv import load_dotenv
from peewee import AutoField, CharField, ForeignKeyField, Model, MySQLDatabase


load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class InstructorModel(Model):
    """
    Model for instructors
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    speciality = CharField(max_length=50)

    class Meta:
        """
        Instructors table
        """

        database = database
        table_name = "instructors"


class CourseModel(Model):
    """
    Model for courses
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    id_instructor = ForeignKeyField(InstructorModel, field="id", backref="courses")

    class Meta:
        """
        Courses table
        """

        database = database
        table_name = "courses"
