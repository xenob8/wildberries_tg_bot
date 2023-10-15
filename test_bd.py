from sqlalchemy import create_engine, text
from config import bd_pass

# Замените 'your_password' на ваш пароль
DATABASE_URL = f"postgresql://dyvawvhc:{bd_pass}@trumpet.db.elephantsql.com/dyvawvhc"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    version = result.fetchone()[0]
    print(version)
# Теперь вы можете использовать engine для выполнения запросов к БД
