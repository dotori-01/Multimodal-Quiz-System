import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("DataBase/gpt-quiz-db-firebase-adminsdk-fbsvc-e84673227c.json")
firebase_admin.initialize_app(cred)

db = firestore.client()