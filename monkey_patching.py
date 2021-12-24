
class Greeting:
    def human(self):
        print("Hello there!")


def monkey(self):
    print('Ooh Ooh Ooh!')


Greeting.human = monkey  # Human greeting is patched with monkey

G = Greeting()

G.human()
