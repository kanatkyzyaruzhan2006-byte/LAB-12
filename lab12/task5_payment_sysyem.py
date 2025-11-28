from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def refund(self):
        pass


class PayPal(PaymentSystem):
    def authorize(self):
        print("PayPal авторизация")

    def process(self):
        print("PayPal обработка платежа")

    def refund(self):
        print("PayPal возврат средств")


class KaspiPay(PaymentSystem):
    def authorize(self):
        print("Kaspi авторизация")

    def process(self):
        print("Kaspi обработка платежа")

    def refund(self):
        print("Kaspi возврат средств")


class VisaPayment(PaymentSystem):
    def authorize(self):
        print("Visa авторизация")

    def process(self):
        print("Visa обработка платежа")

    def refund(self):
        print("Visa возврат средств")


p = PayPal()
p.authorize()
p.process()
p.refund()

k = KaspiPay()
k.authorize()
k.process()
k.refund()

v = VisaPayment()
v.authorize()
v.process()
v.refund()