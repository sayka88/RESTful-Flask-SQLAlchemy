from app import app, db

# Создание таблиц
def create_tables():
    with app.app_context():
        db.create_all()
        print("Database tables created.")

if __name__ == '__main__':
    create_tables()
