""" This the Quick Reference for git"""

""" E-book for git """

https://git-scm.com/book/en/v2



# Configure Git

git config --global user.name "UserName"

git config --global user.email user@email.com 

# Setting up your repository  

# If you already have your project folder.
# This command will create subdirectory ".git" in your project folder
# This subdirectory contains all the necessary files of your repository 

git init 

# You can also create and initialize project by using this command 
"""
NOTE : Your project haven't been tracked yet
"""
git init project_name


# To Begin Tracking files and to do initial commit
# add files to the repository(local)

git add file_name
git add --all
git add *.c # this will add all the (*.c here c is the extension of the file)C files to the repository
git commit -m ' Your message here for the files ' 



# Cloning the  Existing repositorty 

git clone repository_link

""" 
Git has a number of different transfer protocols you can use. 
The previous example uses the https:// protocol, 
but you may also see git:// or user@server:path/to/repo.git, 
which uses the SSH transfer protocol.
"""

# Adding files to repository

git add file_name

# To check the status of the repository
"""
If there is any updates or changes in project folder,
this command will show you and what you have to update in repository.
"""
git status


# To save the changes 
git commit -m "comments"

# this will update the github
git push 

#to sync the local repository 
git pull 

#Say you made changes in one of your file but you don’t want to commit it to the repo then you can stash it and also you can push it later as well.
sudo git stash
