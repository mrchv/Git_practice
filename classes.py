class QA:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def test(self):
        return "I'm testing!"

tester = QA('Dima', 'Autotesting')
print(tester.test())