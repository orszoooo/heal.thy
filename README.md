# heal.thy
Heal.thy is an online platform for managing diet plans. Users can add recipes to the database, we encourage to do that. 
From wide selection of recipes, one can arrange meal plan for their needs. Each created plan is attached to user's account.
Created plan can be exported to pdf file.

# Installation
At this moment we do not have hosting for this site yet. Usage of this platform is possible in offline mode.
Clone the GitHub repository or download the .zip file. In cmd.exe type: `.\.venv\Scripts\activate` to activate the python 
virtual environment with all the necessary libraries. Then type:  `python.exe manage.py runserver` and type in browser `127.0.0.1:8000`.
You have to be in the main folder directory to make above commands work. This project should run in the Linux based operating systems but 
it may need to install python, django and xhtml2pdf in the used distribution manually. 

# Usage
Usage of this site is straightforward. After account creation and login, user can see their meal plan in the main page. 
There is the main page, recipe page, page to make plan or add meal to existing plan. The Profile page lets user to select active plan 
as one user can have multiple plans attached to the account. 

## Main Page
![image](https://user-images.githubusercontent.com/117857476/212065733-ed32c5ac-6a42-40fb-a519-7a081bf54432.png)

## Recipe Page
![image](https://user-images.githubusercontent.com/117857476/212065796-d254dcdd-710e-4458-8a99-f6512a643f9e.png)

## Generated PDF file
![image](https://user-images.githubusercontent.com/117857476/212066743-ceaead30-57fb-44ea-8ed1-3594895302c1.png)

