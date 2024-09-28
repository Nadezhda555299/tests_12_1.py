import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r_1 = runner.Runner("Test Walker")
        for i in range(10):
            r_1.walk()
        self.assertEqual(r_1.distance, 50)

    def test_run(self):
        r_2 = runner.Runner("Test Runner")
        for i in range(10):
            r_2.run()
        self.assertEqual(r_2.distance, 100)

    def test_challenge(self):
        r_1 = runner.Runner("Runner_1")
        r_2 = runner.Runner("Runner_2")

        for i in range(10):
            r_1.run()
            r_2.walk()

        self.assertNotEqual(r_1.distance, r_2.distance)


if __name__ == '__main__':
    unittest.main()