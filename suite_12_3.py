import unittest
import tests_12_3

utests = unittest.TestSuite()
utests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
utests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(utests)