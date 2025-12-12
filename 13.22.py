class Category:
    """Класс категории товаров"""
    def __init__(self, name: str, description:str):
        """
        Инициализация категории

        :param name: Название категории
        :param description: Описание категории
        """
        self.name = name
        self.description = description
        self.__products = [] # Приватный атрибут для хранения товаров

    def add_product(self, product):
        """
        Добавляет товар в категорию

        :param product: Объект товара
        """
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """Геттер для получения строкового представления товаров"""
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(products_list)


class Product:
    """Класс товара"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
               Инициализация товара

               :param name: Название товара
               :param description: Описание товара
               :param price: Цена товара
               :param quantity: Количество товара
               """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с валидацией и подтверждением"""
        if new_price <= 0:
            print("Цена введена некорректная. Цена должна быть больше нуля.")
        elif new_price < self.__price:
            # Запрос подтверждения на понижение цены
            confirm = input(f"Цена снижается с {self.__price} до {new_price}. "
                            f"Подтвердите понижение цены (y/n): ").lower()
            if confirm == 'y':
                self.__price = new_price
                print("Цена успешно изменена.")
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = new_price


    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int,  products_list=None):
        """
        Создает и возвращает новый товар

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара
        :return: Объект товара
        """
        if products_list is not None:
            for product in products_list:
                if product.name == name:
                    # Объединяем количество
                    product.quantity += quantity
                    # Выбираем максимальную цену
                    if price > product.price:
                        product.price = price
                    return product

        # Если товар не найден, создаем новый
        return cls(name, description, price, quantity)



# Создание категории
electronics = Category("Электроника", "Электронные товары")

# Создание товаров
product1 = Product.create_product("Смартфон", "Мощный смартфон", 50000, 10)
product2 = Product.create_product("Ноутбук", "Игровой ноутбук", 80000, 5)

# Добавление товаров в категорию
electronics.add_product(product1)
electronics.add_product(product2)

# Вывод товаров
print(electronics.products)

# Изменение цены
product1.price = 45000  # Запросит подтверждение
product1.price = 55000  # Установится без подтверждения
product1.price = -100   # Выведет сообщение об ошибке