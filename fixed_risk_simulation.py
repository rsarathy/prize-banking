# A simulation demonstrating the viability of "prize-based" savings accounts.
#
# Instead of each account accruing a fixed amount of interest annually (~3%),
# we offer an independent, 1% chance for an account to increase its principal
# by 300%.
#
# For the purposes of this simulation, we make the following assumptions:
#
# * A bank offers loans to its customers at an average of 8%.
# * Wealth follows a standard Pareto distribution, where roughly 20% of the
#   accounts will own 80% of the assets under management in our bank.
# * All assets under management will be loaned out at a rate of 8%.
# * A bank will pay out "prizes" according to the latest recording balance
#   before the formal end of year "drawing" takes place.
# * Savings account begin with a fixed amount of money and do not increase their
#   balance thereafter, apart from receiving any prizes from the bank, should 
#   they happen to.

from __future__ import division
import numpy as np
import random
import simulation


# The rates that the bank will offer loans at.
LOAN_INTEREST = 0.08

class FixedRiskSimulation(simulation.BankingSimulation):
  def turn(self):
    """
    Simulates 1 year's worth of the bank's events.
    
    At the end of the year, the bank does the following:
    1. Randomly quadruple certain savings accounts.
    2. Collects its interest on the loans that it issued.
    3. Calculates its profits (interest minus awarded money).
    """

    # Let 
    #   I = loan interest rate
    #   E = awarded money as a result of certain accounts randomly quadrupling
    #   A = original assets under management
    #
    # Then profit = A * I - E
    self.profits.append(self.assets_under_management * LOAN_INTEREST - \
      self._award_accounts())
    self.assets_under_management = np.sum(self.accounts)
  
  def _award_accounts(self):
    """
    Gives each savings account under the bank an independent 1% chance of 
    increasing their balance by 300%.
    """

    prize_money = 0
    for i in xrange(len(self.accounts)):
      # Each savings account has a 1% chance of quadrupling their principal. The
      # chance is independent between accounts.
      if random.randint(1, 100) == 1:
        prize_money += 3 * self.accounts[i]
        self.accounts[i] *= 4
    return prize_money


if __name__ == '__main__':
  s = FixedRiskSimulation()
  for i in xrange(10):
    s.turn()
    print s.assets_under_management, sum(s.profits)
  print s.profits
  print 'Ten year profits:', sum(s.profits)
