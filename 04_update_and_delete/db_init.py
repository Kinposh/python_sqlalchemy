import sqlalchemy

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:kinposh@8.136.221.2/study', echo=True)


meta_data = sqlalchemy.MetaData()

person_table = sqlalchemy.Table(
    "person", meta_data,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column("birthday", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("address", sqlalchemy.String(255), nullable=True),
)


