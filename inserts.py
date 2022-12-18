from service import ConfigService as conf

conf.init()

# 1 - imports
# from models.xxx import xxx
from models.basemodel import Session, engine, Base

# CREATE SCHEMA `database_name` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci ;

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# create_sample_data(session)
# for instance in session.query(User):
#    print(instance)

# for instance in session.query(Chat):
#    print(instance.name, instance.username, instance.create_date, instance.update_date)

session.close()