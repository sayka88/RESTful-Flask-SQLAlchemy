if __name__ == '__main__':
    with app.app_context():
        create_tables()  # Создание таблиц перед запуском приложения
    app.run(debug=True)
