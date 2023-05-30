import pymysql


class MySQLConnector:
    def __init__(self):
        # Connect to the database
        self.connection = pymysql.connect(host='127.0.0.1',
                                          user='user',
                                          password='password',
                                          database='db',
                                          cursorclass=pymysql.cursors.DictCursor)

    def insert(self):
        with self.connection:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (`id`, `email`) VALUES (%s, %s)"
                cursor.execute(sql, ('1', 'hello'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()

    def query(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `email` FROM `users` WHERE `id`=%s"
            cursor.execute(sql, ('1',))
            result = cursor.fetchone()
            print(result)
