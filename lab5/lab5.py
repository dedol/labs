class Warehouse:
    """
    Абстрактный склад, на котором хранятся процессоры и видеокарты
    """
    def get_processor(self):
        pass

    def get_graphcard(self):
        pass


class Processor():
    """
    Абстрактный процессор, имеет имя и частоту
    """
    def __init__(self):
        self.name = ''
        self.frequency = ''

    def __str__(self):
        return f'{self.name} ({self.frequency})'


class Intel(Processor):
    """
    Конкретный процессор Intel
    """
    def __init__(self):
        self.name = 'INTEL'
        self.frequency = '2.7 Ghz'


class AMD(Processor):
    """
    Конкретный процессор AMD
    """
    def __init__(self):
        self.name = 'AMD'
        self.frequency = '3.2 Ghz'


class GraphCard():
    """
    Абстрактная видеокарта
    """
    def __init__(self):
        self.name = ''

    def __str__(self):
        return self.name


class Nvidia(GraphCard):
    """
    Конкретная видеокарта Nvidia
    """
    def __init__(self):
        self.name = 'NVIDIA'


class Radeon(GraphCard):
    """
    Конкретная видеокарта Radeon
    """
    def __init__(self):
        self.name = 'RADEON'


class IntelWarehouse(Warehouse):
    """
    Склад Intel, с процессорами Intel и видеокартами Nvidia
    """
    def get_processor(self):
        return Intel()

    def get_graphcard(self):
        return Nvidia()


class AMDWarehouse(Warehouse):
    """
    Склад AMD, с процессорами AMD и видеокартами Radeon
    """
    def get_processor(self):
        return AMD()

    def get_graphcard(self):
        return Radeon()


class Computer:
    """
    Абстрактный компьютер
    """
    def __init__(self):
        self.processor = ''
        self.ram = ''
        self.storage = ''
        self.graphcard = ''

    def __str__(self):
        return (
            'Builded computer:\n' +
            f'\tProcessor: {self.processor}\n' +
            f'\tRam: {self.ram}\n' +
            f'\tStorage: {self.storage}\n' +
            f'\tGraph card: {self.graphcard}'
        )


class Builder:
    """
    Работник магазина, собирающий компьютер
    """
    def build(self, warehouse):
        self.computer = Computer()
        self.warehouse = warehouse


class OfficeComputer(Builder):
    """
    Офисный компьютер, собираемый работником магазина
    """
    def set_processor(self):
        self.computer.processor = self.warehouse.get_processor()

    def set_ram(self):
        self.computer.ram = '4 GB'

    def set_storage(self):
        self.computer.storage = 'HDD 250 GB'

    def set_graphcard(self):
        self.computer.graphcard = 'NO'


class GamingComputer(Builder):
    """
    Игровой компьютер, собираемый работником магазина
    """
    def set_processor(self):
        self.computer.processor = self.warehouse.get_processor()

    def set_ram(self):
        self.computer.ram = '16 GB'

    def set_storage(self):
        self.computer.storage = 'SSD 1000 GB'

    def set_graphcard(self):
        self.computer.graphcard = self.warehouse.get_graphcard()


class Shop:
    """
    Компьютерный магазин
    """
    def set_computer(self, builder):
        self.builder = builder

    def build_computer(self, warehouse):
        self.builder.build(warehouse)
        self.builder.set_processor()
        self.builder.set_ram()
        self.builder.set_storage()
        self.builder.set_graphcard()

    def get_computer(self):
        return self.builder.computer


if __name__ == '__main__':
    shop = Shop()
    shop.set_computer(GamingComputer())
    shop.build_computer(AMDWarehouse())
    computer = shop.get_computer()
    print(computer)
