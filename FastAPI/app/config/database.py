from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class InstructorModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    speciality = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "instructors"


class CourseModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    id_instructor = ForeignKeyField(InstructorModel, field="id", backref="courses")

    class Meta:
        database = database
        table_name = "courses"