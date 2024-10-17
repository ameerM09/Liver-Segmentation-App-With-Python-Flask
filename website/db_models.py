from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class PatientScan(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    """
    1. Stores the patient's name on record
    2. Meant to store the specific type of cancer affiliated with the patient (e.g. liver, pancreatic, etc)
    3. Meant to keep track of when each patient directory was created
    4. Meant to keep track of the CT scans associated with each respective patient
    """
    
    patient_name = db.Column(db.String(150), nullable = False, unique = True)

    # patient_type_of_cancer = db.Column(db.String(150), nullable = False)

    # date_of_patient_scan = db.Column(db.DateTime(timezone = True), default = func.now())

    # patient_scan_on_record = db.Column(db.String(150), nullable = True)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))

class Account(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)

    # Enforces that no two accounts can hold the same associated email
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150), nullable = False)

    patient_scans_on_account = db.relationship("PatientScan")