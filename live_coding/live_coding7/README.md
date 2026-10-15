# Database System Installation for DS 6001
Docker compose files for launching MySQL, PostGreSQL, and MongoDB with associated settings. Intended to assist students in DS 6001 at the University of Virginia with installing DB systems

## Instructions for setting up the environment the first time

**Step 1**: Find and open the terminal on your computer. On Mac, click on the magnifying glass in the top right corner of the screen and type "Terminal". On Windows, search for an application called "Windows Powershell".

**Step 2**: If you are using this approach, you must be willing to save all of your work for this course in one folder (although you may create sub-folders inside this folder if you want). The folder will be named "ds6001databases", and the following steps will download it for you -- don't create it yourself. First, decide on a location where you want this folder to download and copy the file path. Then inside the terminal, move inside this directory by typing
```
cd \path\to\location
```
where you need to replace `\path\to\location\` with the appropriate folder address for your system. 

**Step 3**: Use git to download the contents of this repository to your own computer by typing
```
git clone https://github.com/jkropko/ds6001databases
```
If you receive an error that `git` is not recognized on your computer, see the installation instructions for the git version control system here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

**Step 4**: The "ds6001databases" folder is now downloaded, but to work inside this folder, type
```
cd ds6001databases
``` 

**Step 5**: Install the packages you need (they are all listed in the requirements.txt file) by typing: 
```
pip install -r requirements.txt
```

**Step 6**: Create an ".env" file to store your passwords, API keys, and other sensitive information. On a Mac, open a new terminal or a new tab, make sure the working directory is still the "ds6001databases" folder. Then type
```
touch .env
```
On Windows, open Notepad and create a new document. Then click FILE -> Save AS. Under File as Type select "All files". Click through the file window to your "ds6001databases" folder, and save the file as `.env` (it begins with the period, and contains no spaces)

**Step 7**: Open the `.env` file. On Windows, your file should be open already as a result of Step 5, and on Mac type `open .env`. Inside the .env file, paste the following
```
POSTGRES_PASSWORD=password1
MONGO_INITDB_ROOT_PASSWORD=password2
MYSQL_ROOT_PASSWORD=password3
mongo_init_db=mongodb
MYSQL_DATABASE=db
MONGO_INITDB_ROOT_USERNAME=mongo
```
On the first three lines, change `password1`, `password2`, and `password3` to anything you like (but please do not use the @ symbol as that causes problems for some packages). Leave the 4th, 5th, and 6th lines alone. Then SAVE the .env file.

**Step 8**: Download and install the Docker desktop client for your operating system, here: https://www.docker.com/products/docker-desktop/. Once the Docker desktop is installed, open it on your local computer. 

**Step 9**: In the terminal, type
```
docker compose up
```
If successful, you will see a large amount of output from JupyterLab, MySQL, PostgreSQL, and Mongo. If you see a "docker daemon" error, then double-check that the Docker desktop client is running.

**Step 10**: Launch JupyterLab, VS Code, or another Python IDE on your computer. 

**Step 11**: Open the `db_tests.ipynb` file. This notebook contains code that will check whether the MySQL, PostgreSQL, and MongoDB database systems we will explore in this course are operating as expected. Run all cells in this notebook. If there are errors, contact the instructor or see the Troubleshooting section below.

**Step 12**: Return to the terminal where you previously typed `docker compose up`. Press CONTROL + C to stop the container. Then type
```
docker compose down
```
to remove the extra volumes and networks Docker had built and free up that space on your computer.

If steps 1 through 11 all ran as expected, then congratulations, you are all set with the environment and you are ready to start using it in class. 

## Instructions for using the environment each time

**Step 1**: Open your terminal. On Mac, click on the magnifying glass in the top right corner of the screen and type "Terminal". On Windows, search for an application called "Windows Powershell".

**Step 2**: Navigate to the "ds6001databases" folder on your computer by typing
```
cd \path\to\location\ds6001databases
```
where you need to replace `\path\to\location\` with the appropriate folder address for your system. 

**Step 3**: Make sure the Docker desktop client is running, and get the latest versions of each container by typing
```
docker compose pull
```
Then type 
```
docker compose up
```
If successful, you will see a large amount of output from MySQL, PostgreSQL, and Mongo. If you see a "docker daemon" error, then double-check that the Docker desktop client is running.

**Step 4**: Work within JupyterLab, VS Code, or another Python IDE as you would do normally.

**Step 5**: When using `mysql.connector`, `psycopg`, `pymongo`, or `sqlalchemy` to connect to one of the running database systems, use `localhost` for the host name, and use the following usernames, passwords, and ports for accessing the DB server:

* For MySQL, the user should be `root`, the password should be your environmental variable named `MYSQL_ROOT_PASSWORD`, and the port should be 3306.

* For PostgreSQL, the user should be `postgres`, the password should be your environmental variable named `POSTGRES_PASSWORD`, and the port should be 5432.

* For MongoDB, the user should be your environmental variable `MONGO_INITDB_ROOT_USERNAME`, the password should be your environmental variable named `MONGO_INITDB_ROOT_PASSWORD`, and the port should be 27017.

**Step 6**: When you are done working, return to the terminal where you previously typed `docker compose up`. Press CONTROL + C to stop the containers. Then type
```
docker compose down
```
to remove the extra volumes and networks Docker had built and free up that space on your computer.

## Troubleshooting

* If `db_tests.ipynb` returns errors, it may be because you have an older, local installation of MySQL, PostgreSQL, or MongoDB running on your computer. Find these local installations and uninstall them (unless you have important data stored there)

* If you are seeing authentication errors when running the cells in `db_tests.ipynb` it might be either because you changed your passwords, or used special characters such as @ and # in your passwords (which are understood differently by Python). If you changed your passwords, the old passwords may still be cached in the attached volumes, so open the Docker Desktop client, click on Volumes, and delete the volumes attached to MySQL, PostgreSQL, and Mongo. Then retry `docker compose up`.

* If you used special characters in your passwords, try deleting these characters, then open the Docker Desktop client, click on Volumes, and delete the volumes attached to MySQL, PostgreSQL, and Mongo. Then retry `docker compose up`.
