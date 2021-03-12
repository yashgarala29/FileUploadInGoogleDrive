"""
    Author  :- Yash Garala
    Date    :- 12-03-2021
    Problem :-
"""
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1-f8QEs8Pfm1zC9mF8NVNNYugG6VPvY5r')}).GetList()
for file in file_list:
    if (file['title'] == "a.png"):
        fileID = file['id']
file_delete=drive.CreateFile({'id': fileID})
# file_delete.Trash()
# file_delete.UnTrash()
file_delete.Delete()
