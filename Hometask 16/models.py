# 6. Создать питоновский файл models.py .
# Создать таблицу Users определив поля
# ( id: первичный ключ, first_name,last_name:строки длинной в 50 символов, age: целое число).
# Создать “движок” для подключения SQLite и создать таблицу через Base.metadata.create_all(engine)


from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column()


engine = create_engine("sqlite:///models.db", echo=True)
# Base.metadata.create_all(engine)

# 7. Создать сессию и добавить в базу 5 разных пользователей.

with Session(engine) as session:
    John = User(
        first_name="John",
        last_name="Johnson",
        age=20
    )
    Jack = User(
        first_name="Jack",
        last_name="Jackson",
        age=21
    )
    Sandy = User(
        first_name="Sandy",
        last_name="Sandyson",
        age=22
    )
    Bob = User(
        first_name="Bob",
        last_name="Bobson",
        age=23
    )
    Kate = User(
        first_name="Kate",
        last_name="Kateson",
        age=24
    )
    session.add_all([John, Jack, Sandy, Bob, Kate])
    session.commit()

    # 8. Создать сессию и вывести первых 3 пользователей отсортированных по убыванию возроста

    stmt = select(User).order_by(User.age.desc()).limit(3)
    for User in session.scalars(stmt):
        print(User.first_name, User.last_name, User.age)

    # 9. Создать сессию и вывести пользователей по имени “Jhon”

    stmt = select(User).where(User.first_name.in_(["John"]))
    for User in session.scalars(stmt):
        print(User.first_name, User.last_name)
