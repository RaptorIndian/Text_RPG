from classes import damage_calc

from classes import *
from armors import *
from weapons import *

exp_required = [10, 40, 100, 230, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400]

unit_1 = Unit("Test1", 100, 1, 100, copper_axe, None, steel_sword, None)

unit_2 = Unit("Test1", 100, 1, 100, copper_axe, gambeson, copper_sword, None)

for i in range(len(exp_required)):
  # print(damage_calc(unit_1, unit_2))
  print(damage_calc(unit_1, unit_2))
  unit_1.main_hand.weapon_skill += 1