'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7.


'''
sudo pip3 install virtualenv
mkdir ~/.venvs
virtualenv −−system−site−packages ~/.venvs/CodingNomads
pip freeze -local > requirements.txt
pip install -r /path-to-file/requirements.txt
