# SomeCoolProjectName

Some cool text about the project

## Prequisites

- Python 3.9
- MySql Database
    - For this Bot to work locally you need a MySql Database (it might work with others but for now I don't support them).
- [pipenv](https://github.com/pypa/pipenv) (Python virtual environment and packaging tool)

## Installation

Make sure that you have the prequisites installed and the code checked out.

First create a new Schema in your Database by executing the following SQL (modify the schema name):
```sql
CREATE SCHEMA `yourschemaname` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci ;
```
<br><br>
Then switch to the checked out directory in the Terminal and run:

```bash
pipenv sync
```
This will install all needed python packages in a separate virtual environment.
<br><br><br>
Next is to create the logs folder in the root directory:
```bash
mkdir logs
```

In the resources folder is an example config file. 
<br><br><br>
For the bot to work you need to create a working config:
```bash
cp example_hdconfig.cfg hdconfig.cfg
--> make your changes in the "config.cfg"
cp hdconfig.cfg current_hdconfig.cfg
```
<br><br>
After everything is set up we create the necessary tables in the schema.

For this we execute the following in the root directory:
```bash
pipenv run python inserts.py
```

## Usage
To run the bot, simply issue the follwing in the root directory:
```bash
pipenv run python main.py
```

## Contributing
This repository has a project where ideas for functionalities are stored.
After sighting the idea and discussing it with the other participants, move that task into the coresponding swimlane. Please keep those updated, so that everyone else can track work in progress.

Please use Pull Request for making changes in the code, so i can keep track on whatever changes is beeing done.
