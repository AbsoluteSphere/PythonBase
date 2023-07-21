class Person:
    def __init__(self, name):
        self.name = name

    def say(self, message):
        print(f'{self.name}: {message}')


p1 = Person('安娜')
p2 = Person('双双')

p1.say('双双一起去吃饭...')
p2.say('好呀好呀...')


