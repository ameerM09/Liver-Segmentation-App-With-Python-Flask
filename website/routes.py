from .test_model import calculate_accuracy
import os
from io import BytesIO
import zipfile
from flask import Flask, send_file, redirect, url_for, Blueprint, render_template, request, flash

from flask_login import login_required, current_user

from . import db
from .db_models import PatientScan

web_app = Flask(__name__)

web_app.config['UPLOAD_FOLDER'] = './data/final_nifti_files/imagesVal'
os.makedirs(web_app.config['UPLOAD_FOLDER'], exist_ok=True)

IMAGE_FOLDER = "./data/model_results"

routes = Blueprint("routes", __name__)

@routes.route("/", methods = ["GET", "POST"])
def home_page():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        new_patient = PatientScan(patient_name=patient_name)

        print(patient_name)

        db.session.add(new_patient, account_id = current_user.id)
        db.session.commit()

        flash('Patient added successfully!', category = 'successful')

        # patients = PatientScan.query.all()

    return render_template("my_patients.html", account = current_user)

@routes.route('/download', methods=['GET'])
def download():
    memory_file = BytesIO()

    with zipfile.ZipFile(memory_file, 'w') as zf:
        for root, dirs, files in os.walk(IMAGE_FOLDER):
            for file in files:
                if file.endswith('.png'):
                    file_path = os.path.join(root, file)
                    zf.write(file_path, os.path.basename(file_path))

    memory_file.seek(0)

    return send_file(memory_file, attachment_filename='results.zip', as_attachment=True)
        
@routes.route('/results', methods = ["GET", "POST"])
def results():
    # model_results_dir = "G:/OrganSegmentationApplication/data/model_results"

    # image_list = os.listdir(model_results_dir)

    # TODO: Change the absolute path in image_paths

    # image_paths = [f'../../data/model_results/{img}' for img in image_list]

    return render_template("results.html", account = current_user)

@routes.route('/uploader', methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        if f and (f.filename.endswith('.nii') or f.filename.endswith('.nii.gz')):
            filepath = os.path.join(web_app.config['UPLOAD_FOLDER'], f.filename)
            f.save(filepath)

            #TODO: on success case, we will not move to the new folder. We have to call our model to perform segmentation
            primary_dir = "./data/final_nifti_files"
            model_dir = "./data/dl_models"

            test_file_name = f.filename

            accuracy = calculate_accuracy(primary_dir, model_dir, test_file_name)

            # return f"Accuracy: {accuracy} + {f.filename}"

            # return f"File {f.filename} uploaded successfully!"
            return redirect(url_for('routes.results'))
        
        else:
            return "Please upload a valid NIFTI file (.nii or .nii.gz)."