user = 'maria'
password = 'pass'
host = 'db'
database = 'beverage'

COCKROACH = {
    'engine': 'cockroachdb',
    'username': 'root',
    'password': '',
    'host': host,
    'db_name': database,
}

MYSQL = {
    'engine': 'mariadb+pymysql',
    'username': user,
    'password': password,
    'host': host,
    'db_name': database,
}

POSTGRESQL = {
    'engine': 'postgresql',
    'username': user,
    'password': password,
    'host': host,
    'db_name': database,
}

SQLALCHEMY = {
  'autocommit': False,
  'autoflush': False,
  'sessionmaker': [False, False],
  'debug': False,
}
