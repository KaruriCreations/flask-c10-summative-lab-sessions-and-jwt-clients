import os
from flask import Flask, request, session
from flask_restful import Api, Resource
from flask_migrate import Migrate

from models import db, bcrypt, User, Note
from schemas import user_schema, note_schema, notes_schema