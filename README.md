### Below is what the final directory structure should look like:

```
Liver-Segmentation-App-With-Python-Flask/
    |──data/
       |──dl_models/
          |──liver_segmentation.pth
       |──final_nifti_files/
          |──imagesVal
          |──labelsVal
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
