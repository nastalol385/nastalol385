class Phone:

    def __init__(self, number, model, weight):
        self.number = number

        self.model = model

        self.weight = weight

    def receive_call(self, name):
        print('Звонит', name, 'на', self.number)

    def get_number(self):
        return self.number


a = Phone(89537777777, 'samsung', 170)

b = Phone(89535555555, 'xiaomi', 160)

c = Phone(89533333333, 'iphone', 150)

a.receive_call("Аделина")

a.get_number()

b.receive_call("Егор")

b.get_number()

c.receive_call("Вика")

c.get_number()

