"""
    Author  :- Yash Garala
    Date    :- 12-03-2021
    Problem :-
"""
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
path="./upload"
for upload_file in os.listdir(path):
    gfile = drive.CreateFile({'title': upload_file,'parents': [{'id': '1-f8QEs8Pfm1zC9mF8NVNNYugG6VPvY5r'}]})
    # Read file and set it as the content of this instance.
    x=os.path.join(path,upload_file)

    gfile.SetContentFile(x)
    gfile.Upload()  # Upload the file.
