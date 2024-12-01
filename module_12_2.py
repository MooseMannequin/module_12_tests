import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.participant1 = Runner('Усейн', 10)
        self.participant2 = Runner('Андрей', 9)
        self.participant3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in range(1,4):
            print(cls.all_results[i])

    def test_1(self):
        tour1 = Tournament(90, self.participant1, self.participant3)
        self.all_results[1] = tour1.start()
        self.assertTrue(self.all_results[1][2] == 'Ник', 'Неверно')

    def test_2(self):
        tour2 = Tournament(90, self.participant2, self.participant3)
        self.all_results[2] = tour2.start()
        self.assertTrue(self.all_results[2][2] == 'Ник', 'Неверно')

    def test_3(self):
        tour3 = Tournament(90, self.participant1, self.participant2, self.participant3)
        self.all_results[3] = tour3.start()
        self.assertTrue(self.all_results[3][3] == 'Ник', 'Неверно')

if __name__ == '__main__':
    unittest.main()
