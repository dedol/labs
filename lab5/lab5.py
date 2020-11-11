class Warehouse:
    """
    Абстрактный склад, на котором хранятся процессоры и память
    """
    def get_processor(self):
        pass

    def get_flash(self):
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


class OriginalATMega(Processor):
    """
    Оригинальный процессор
    """
    def __init__(self):
        self.name = 'Original 328p'
        self.frequency = '8 Mhz'


class CloneATMega(Processor):
    """
    Копия оригинального процессора
    """
    def __init__(self):
        self.name = 'Clone 328p'
        self.frequency = '8 Mhz'


class Flash():
    """
    Абстрактная флеш память
    """
    def __init__(self):
        self.name = ''

    def __str__(self):
        return self.name


class OriginalFlash(Flash):
    """
    Оригинальная флеш память
    """
    def __init__(self):
        self.name = 'Original flash'


class CloneFlash(Flash):
    """
    Копия оригинальной флеш памяти
    """
    def __init__(self):
        self.name = 'Clone flash'


class OriginalWarehouse(Warehouse):
    """
    Склад с оригинальными компонентами
    """
    def get_processor(self):
        return OriginalATMega()

    def get_flash(self):
        return OriginalFlash()


class CloneWarehouse(Warehouse):
    """
    Склад с копиями оригинальных компонентов
    """
    def get_processor(self):
        return CloneATMega()

    def get_flash(self):
        return CloneFlash()


class Controller:
    """
    Абстрактный контроллер
    """
    def __init__(self):
        self.processor = ''
        self.flash = ''
        self.boardsize = ''
        self.plugtype = ''

    def __str__(self):
        return (
            'Builded controller:\n' +
            f'\tProcessor: {self.processor}\n' +
            f'\tFlash: {self.flash}\n' +
            f'\tBoardsize: {self.boardsize}\n' +
            f'\tPlugtype: {self.plugtype}'
        )


class Builder:
    """
    Работник производства
    """
    def build(self, warehouse):
        self.controller = Controller()
        self.warehouse = warehouse


class DevelopmentBoard(Builder):
    """
    Плата для разработки
    """
    def set_processor(self):
        self.controller.processor = self.warehouse.get_processor()

    def set_flash(self):
        self.controller.flash = self.warehouse.get_flash()

    def set_boardsize(self):
        self.controller.boardsize = 'Big'

    def set_plugtype(self):
        self.controller.plugtype = 'Micro USB'


class ProjectBoard(Builder):
    """
    Плата для готового проекта
    """
    def set_processor(self):
        self.controller.processor = self.warehouse.get_processor()

    def set_flash(self):
        self.controller.flash = self.warehouse.get_flash()

    def set_boardsize(self):
        self.controller.boardsize = 'Small'

    def set_plugtype(self):
        self.controller.plugtype = 'Without connector'


class Factory:
    """
    Фабрика, собирает контроллеры на заказ
    """
    def set_controller_type(self, builder):
        self.builder = builder

    def build_controller(self, warehouse):
        self.builder.build(warehouse)
        self.builder.set_processor()
        self.builder.set_flash()
        self.builder.set_boardsize()
        self.builder.set_plugtype()
        return self.builder.controller


if __name__ == '__main__':
    factory = Factory()
    factory.set_controller_type(DevelopmentBoard())
    c = factory.build_controller(CloneWarehouse())
    print(c)