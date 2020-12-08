class Message:
    def translate_message(self):
        pass


class TranslateToEnglish(Message):
    def __init__(self, text):
        self.text = text

    def translate_message(self):
        # Тут якобы осуществляется перевод
        if self.text == "Привет, Продавец!":
            return "Hello Seller!"
        else:
            return "Translation error"


class TranslateToRussian(Message):
    def __init__(self, text):
        self.text = text

    def translate_message(self):
        # Тут якобы осуществляется перевод
        if self.text == "Hello Buyer!":
            return "Привет, Покупатель!"
        else:
            return "Translation error"


class Translator:
    def __init__(self, source):
        self.source = source

    def translate(self):
        return self.source.translate_message()





class Mediator():
    def notify(self, sender, event):
        pass


class Messenger(Mediator):
    def __init__(self, buyer, seller):
        self._buyer = buyer
        self._buyer.mediator = self
        self._seller = seller
        self._seller.mediator = self

    def notify(self, sender, event, text):
        if event == "Buyer to Seller":
            print("Мессенджер перенаправил сообщение от покупателя к продавцу")
            message = TranslateToEnglish(text)
            translated = Translator(message).translate()
            self._seller.get_message(translated)

        elif event == "Seller to Buyer":
            print("Мессенджер перенаправил сообщение от продавца к покупателю")
            message = TranslateToRussian(text)
            translated = Translator(message).translate()
            self._buyer.get_message(translated)


class SiteUser:
    def __init__(self, mediator=None):
        self.mediator = mediator


class Buyer(SiteUser):
    def send_message(self, text):
        print(f"Покупатель отправил сообщение продавцу: {text}")
        self.mediator.notify(self, "Buyer to Seller", text)

    def get_message(self, text):
        print(f"Покупатель получил сообщение от продавца: {text}")


class Seller(SiteUser):
    def send_message(self, text):
        print(f"Продавец отправил сообщение покупателю: {text}")
        self.mediator.notify(self, "Seller to Buyer", text)

    def get_message(self, text):
        print(f"Продавец получил сообщение от покупателя: {text}")


if __name__ == "__main__":
    buyer = Buyer()
    seller = Seller()
    messenger = Messenger(buyer, seller)

    buyer.send_message("Привет, Продавец!")
    print()
    seller.send_message("Hello Buyer!")