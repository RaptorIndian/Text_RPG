from classes import *

name = "Gambeson"
description = "A padded jacket made out of multiple layers of linen fabric that were quilted together. Decent against cuts and clobbering, but weak against piercing."
price = 500
weight = 8
defense = .95
bludgeon_resist = 1.2
slash_resist = 1.7
pierce_resist = .9


gambeson = Armor(name, description, price, weight, defense, bludgeon_resist, slash_resist, pierce_resist)

name = "Leather Armor"
description = "To be decided."
weight = 10
defense = 1.05
bludgeon_resist = .95
slash_resist = .95
pierce_resist = 1.2


leather_armor = Armor(name, description, price, weight, defense, bludgeon_resist, slash_resist, pierce_resist)


name = "Chainmail"
description = "To be decided."
weight = 15
defense = 1.1
bludgeon_resist = .9
slash_resist = 1.1
pierce_resist = 1.2


chainmail = Armor(name, description, price, weight, defense, bludgeon_resist, slash_resist, pierce_resist)


name = "Plate Mail"
description = "To be decided."
weight = 20
defense = 1.15
bludgeon_resist = .85
slash_resist = 1.25
pierce_resist = 1.2


plate_mail = Armor(name, description, price, weight, defense, bludgeon_resist, slash_resist, pierce_resist)