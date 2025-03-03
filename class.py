from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, ForeignKey, TIMESTAMP, UniqueConstraint, CheckConstraint, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Подключение к базе данных SQLite
DATABASE_URL ="sqlite:///C:/Users/user/twix.db" # Укажите путь к базе данных

engine = create_engine(DATABASE_URL, echo=True)

# Создание базы
Base = declarative_base()

# Таблица пользователей
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    orders = relationship("Order", back_populates="user")

# Таблица категорий товаров
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    products = relationship("Product", back_populates="category")

# Таблица товаров
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"))

    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")

# Таблица заказов (ограничение: один пользователь — одна категория)
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    order_date = Column(TIMESTAMP, server_default=func.now())
    status = Column(String(50), default="pending")

    user = relationship("User", back_populates="orders")
    category = relationship("Category")
    order_items = relationship("OrderItem", back_populates="order")

    __table_args__ = (UniqueConstraint("user_id", "category_id", name="unique_user_category"),)

# Таблица товаров в заказе
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

    __table_args__ = (CheckConstraint("quantity > 0", name="check_quantity_positive"),)

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Добавление тестовых данных
def seed_data():
    # Создаем пользователей
    user1 = User(name="Иван", email="ivan@example.com")
    user2 = User(name="Анна", email="anna@example.com")

    # Создаем категории
    category1 = Category(name="Одежда")
    category2 = Category(name="Обувь")

    # Создаем товары
    product1 = Product(name="Футболка", price=1500.00, category=category1)
    product2 = Product(name="Джинсы", price=3000.00, category=category1)
    product3 = Product(name="Кроссовки", price=5000.00, category=category2)
    product4 = Product(name="Ботинки", price=7000.00, category=category2)

    # Добавляем данные в сессию и коммитим
    session.add_all([user1, user2, category1, category2, product1, product2, product3, product4])
    session.commit()

    # Создаем заказ (Иван заказывает обувь)
    order1 = Order(user_id=user1.id, category_id=category2.id)

    # Добавляем товары в заказ
    order_item1 = OrderItem(order=order1, product=product3, quantity=1, price=5000.00)
    order_item2 = OrderItem(order=order1, product=product4, quantity=1, price=7000.00)

    session.add_all([order1, order_item1, order_item2])
    session.commit()

    print("Данные успешно добавлены!")

# Запуск заполнения данных
seed_data()
