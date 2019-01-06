from simulation import BankingSimulation
import unittest

class SimulationTest(unittest.TestCase):
  def test_make_accounts(self):
    """Checks that a simulation correctly populates the saving accounts."""
    s = BankingSimulation()
    self.assertAlmostEqual(s.assets_under_management, 1)
    
if __name__ == '__main__':
  unittest.main()
