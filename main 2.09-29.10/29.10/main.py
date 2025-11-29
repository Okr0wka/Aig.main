import psycopg2

# Параметры подключения
DB_NAME = "my_python_app"
DB_USER = "postgres"
DB_PASSWORD = "beregenov013108"  # замените на ваш пароль postgres
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    print("Подключение к базе данных успешно!")

    # Создание таблицы users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL
        );
    """)
    conn.commit()
    print("Таблица users создана или уже существует.")

    # Вставка пользователей
    cursor.execute("INSERT INTO users (username) VALUES (%s), (%s), (%s) ON CONFLICT DO NOTHING;",
                   ('Alice', 'Bob', 'Charlie'))
    conn.commit()
    print("Пользователи добавлены.")

    # Выборка всех пользователей
    cursor.execute("SELECT username FROM users;")
    users = cursor.fetchall()
    print("Список пользователей:")
    for user in users:
        print(user[0])

except Exception as e:
    print("Ошибка:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
