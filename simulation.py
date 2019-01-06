# A base class for simulating a bank that provides prize-based savings accounts.
#
# For the purposes of this simulation, we make the following assumptions:
#
# * A bank offers loans to its customers at an average of 8%.
# * Wealth follows a standard Pareto distribution, where roughly 20% of the
#   accounts will own 80% of the assets under management in our bank.
# * All assets under management will be loaned out at a rate of 8%.
# * A bank will pay out "prizes" according to the latest recording balance
#   before the formal end of year "drawing" takes place.

import numpy as np


# The assets under management (AUM) controlled by the bank.
AUM = 10**6

# The rates that the bank will offer loans at.
LOAN_RATE = 0.08

# The interest rate that the bank will offer to savings account by default.
INTEREST_RATE = 0.03

# The number of savings accounts under the bank.
NUM_ACCOUNTS = 10000

class BankingSimulation(object):
  def __init__(self):
    self.accounts = _make_accounts()
    self.assets_under_management = np.sum(self.accounts)
    self.profits = []
    
def _make_accounts():
  # Seed all saving accounts with wealth obeying a standard Pareto distribution.
  accounts = np.random.pareto(1, NUM_ACCOUNTS)
  
  # Scale each balance equally such that the assets under management is
  # 1 million units.
  temp_sum = np.sum(accounts)
  for i in xrange(len(accounts)):
    accounts[i] *= (AUM / temp_sum)
  return accounts
