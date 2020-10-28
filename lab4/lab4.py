class AbstractDecoder():
    """
    Абстрактный класс, фиксирует интерфейс декодера
    """

    def __init__(self, file):
        pass

    def decode(self):
        pass


class Decoder(AbstractDecoder):
    """
    Декодер, преобразует файл в формат, необходимый для вывода на печать
    """

    def __init__(self, file_ext):
        self.file_ext = file_ext

    def decode(self):
        ext = self.file_ext
        if ext in ['doc', 'docx']:
            return 'word file'
        if ext in ['jpg', 'jpeg', 'png', 'bmp', 'tiff']:
            return 'image'
        if ext in ['pdf']:
            return 'pdf file'
        else:
            return 'unknown file'


class PrintOut:
    """
    Модуль принтера, отвечает за вывод печать
    """

    def __init__(self, file_name, data=AbstractDecoder):
        self.file = file_name
        self.data = data

    def out(self):
        decoded = self.data.decode()
        return f'Printing {decoded} [{self.file}]'


class LANPrinter:
    """
    Сетевой принтер, получает файлы и печатает их
    """

    def __init__(self, local_ip):
        self.local_ip = local_ip
        print(f"Found LAN printer on {local_ip}")

    def print_out(self, file):
        ext = file.split('.')[-1]
        doc = PrintOut(file_name=file, data=Decoder(file_ext=ext))
        print(f'{self.local_ip}:', doc.out())


if __name__ == '__main__':
    pr = LANPrinter('192.168.1.52')
    pr.print_out('report.docx')
    pr.print_out('image2.png')
    pr.print_out('ticket.pdf')
    pr.print_out('chip_dump.bin')