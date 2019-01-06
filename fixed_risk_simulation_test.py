from fixed_risk_simulation import FixedRiskSimulation
import unittest


class FixedRiskSimulationTest(unittest.TestCase):
  def test_profits(self):
    """Checks that after multiple turns, there are records of profits."""
    s = FixedRiskSimulation()
    s.turn()
    s.turn()
    self.assertEqual(len(s.profits), 2)


if __name__ == '__main__':
  unittest.main()
