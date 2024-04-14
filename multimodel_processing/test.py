#test.py
#File to test code 
# import pydrive2
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

if __name__ == "__main__":
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)