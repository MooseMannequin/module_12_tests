import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log",
                    encoding='UTF-8', format='%(levelname)s | %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            obj = Runner('walk', speed=-3)
            for _ in range(10):
                obj.walk()
            self.assertEqual(obj.distance, 50)
            logging.info('"test_walk" выполнен успешно')

        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            return

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            obj2 = Runner(['aaa', 3])
            for _ in range(10):
                obj2.run()
            self.assertEqual(obj2.distance, 100)
            logging.info('"test_run" выполнен успешно')

        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
            return


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj3, obj4 = Runner('participant1'), Runner('participant2')
        for _ in range(10):
            obj3.run()
            obj4.walk()
        self.assertNotEqual(obj3.distance, obj4.distance)


if __name__ == '__main__':
    unittest.main()