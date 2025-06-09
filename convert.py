import os
from sys import platform as plat
import urllib.request
import platform
import zipfile
import glob

# Change below values as appropriate
username = "YOUR-USERNAME"
password = "YOUR-PASSWORD"
directory = "/change/to/your/save/location" # This is where the music will be saved to

if username == "YOUR-USERNAME" or password == "YOUR-PASSWORD" or directory == "/change/to/your/save/location":
    print("Please update the options in the Python file! You need to set your Soulseek username, password and a save location.")
    exit()

# This downloads, extracts and configures SLDL for the user
# SLDL repository can be found here: https://github.com/fiso64/slsk-batchdl
if not glob.glob("*sldl*"):
    print("ok")
    arc = platform.machine().lower() 
    if plat == "linux" or plat == "linux2":
        # Linux
        if arc == "amd64":
            urllib.request.urlretrieve("https://github.com/fiso64/slsk-batchdl/releases/latest/download/sldl_linux-x64.zip", "sldl.zip")
        elif arc == "arm64":
            urllib.request.urlretrieve("https://github.com/fiso64/slsk-batchdl/releases/latest/download/sldl_linux-arm.zip", "sldl.zip")
        os.system("chmod 755 sldl")
        exec = "./sldl"
    elif plat == "darwin":
        # Mac OS
        if arc == "amd64":
            urllib.request.urlretrieve("https://github.com/fiso64/slsk-batchdl/releases/latest/download/sldl_osx-x64.zip", "sldl.zip")
        elif arc == "arm64":
            urllib.request.urlretrieve("https://github.com/fiso64/slsk-batchdl/releases/latest/download/sldl_osx-arm64.zip", "sldl.zip")
        exec = "./sldl"
    elif plat == "win32":
        # Windows
        urllib.request.urlretrieve("https://github.com/fiso64/slsk-batchdl/releases/latest/download/sldl_win-x86.zip", "sldl.zip")
        exec = "sldl.exe"
    with zipfile.ZipFile("sldl.zip", 'r') as zip_ref:
        zip_ref.extractall(os.getcwd())
        if plat == "darwin":
            os.system("xattr -c sldl")
            os.system("chmod 755 sldl")
            os.system("codesign --sign - --force --preserve-metadata=entitlements,requirements,flags,runtime sldl")

os.remove("sldl.zip")

url = input("Enter URL of Spotify playlist: ")

os.system(f"{exec} \"{url}\" --user \"{username}\" --pass \"{password}\" --name-format \"{{title}} - {{artist}}\" --pref-format flac -p \"{directory}\"")
