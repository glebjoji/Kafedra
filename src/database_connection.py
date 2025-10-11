import psycopg2


class DatabaseConnection:
    #Singleton для подключения к PostgreSQL.

    _instance = None
    _connection = None

    def __new__(cls, db_name=None, user=None, password=None, host='localhost', port=5432):
        # Если объект уже создан- та же ссылка
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            try:
                cls._connection = psycopg2.connect(
                    dbname=db_name,
                    user=user,
                    password=password,
                    host=host,
                    port=port
                )
                cls._connection.autocommit = True
                print("Подключение к PostgreSQL успешно установлено")
            except Exception as e:
                raise ConnectionError(f"Ошибка подключения к базе данных: {e}")
        return cls._instance

    def get_connection(self):
        """Возвращает текущее соединение."""
        return self._connection

    def get_cursor(self):
        """Удобный способ получить курсор."""
        return self._connection.cursor()

    def close(self):
        """Закрыть соединение."""
        if self._connection:
            self._connection.close()
            print("Соединение с базой данных закрыто")
