### Below is what the final directory structure should look like:

```
Liver-Segmentation-App-With-Python-Flask/
    |──data/
       |──dl_models/
          |──liver_segmentation.pth
       |──final_nifti_files/
          |──imagesVal/
          |──labelsVal/
      |──model_results/
    |──instance/
       |──database.db
    |──website/
       |──templates/
          |──base.html
          |──my_patients.html
          |──results.html
          |──sign_in.html
          |──sign_up.html
    |──__init__.py
    |──authentication.py
    |──db_models.py
    |──routes.py
    |──test_model.py
```
### In order to derive the data for the imagesVal and labelsVal folders, you need to download the data from this Google Drive link: https://drive.google.com/drive/folders/1qKkkZMjdw6CGdiPNrfopERvWwYHxr8qN?usp=sharing. Please note that you have been granted editor permission, but please do not make any changes to the data.

### This validation data is the only data that the model can be tested on (in the context of this Flask web app). However, the goal I have under your tutoring isn't to make any changes to the machine learning aspect. Rather, I want to:
### - Enhance the frontend (currently only using Bootstrap and HTML)
### - Make it so that when you "open a new patient workspace" a database stores the patient name that is entered, the file name uploaded in that workspace, and (potentially) the date on which the workspace was created
### - Make each of these workspaces be linked to their own unique HTML pages that can be accessed again from the "My Patients" webpage
### - Make it so that the segmentations that appear after hitting the "Upload" button on the "Results" page are not saved to one location, which, in this case, is the data/model_results directory. Add a feature to choose file location on computer.
