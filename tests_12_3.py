import unittest
from module_12_2 import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj = Runner('walk')
        for _ in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj2 = Runner('run')
        for _ in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj3, obj4 = Runner('participant1'), Runner('participant2')
        for _ in range(10):
            obj3.run()
            obj4.walk()
        self.assertNotEqual(obj3.distance, obj4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.participant1 = Runner('Усейн', 10)
        self.participant2 = Runner('Андрей', 9)
        self.participant3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # for i in range(1,4):
        #     print(cls.all_results[i])
        pass

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tour1 = Tournament(90, self.participant1, self.participant3)
        self.all_results[1] = tour1.start()
        self.assertTrue(self.all_results[1][2] == 'Ник', 'Неверно')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tour2 = Tournament(90, self.participant2, self.participant3)
        self.all_results[2] = tour2.start()
        self.assertTrue(self.all_results[2][2] == 'Ник', 'Неверно')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tour3 = Tournament(90, self.participant1, self.participant2, self.participant3)
        self.all_results[3] = tour3.start()
        self.assertTrue(self.all_results[3][3] == 'Ник', 'Неверно')
