#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Crazy Canyon = https://steamcommunity.com/sharedfiles/filedetails/?id=1611573177
# Get Spooked! = https://steamcommunity.com/sharedfiles/filedetails/?id=1540250327
# 18 hole paradise = https://steamcommunity.com/sharedfiles/filedetails/?id=1542178473
# Factory = https://steamcommunity.com/sharedfiles/filedetails/?id=1513002564
# The Temple of One = https://steamcommunity.com/sharedfiles/filedetails/?id=1438631129
# N. Sanity Island = https://steamcommunity.com/sharedfiles/filedetails/?id=1524546907

import random

game = ["Crazy Canyon", "Get Spooked!", "18 hole paradise", "Factory", "The Temple of One", "N. Sanity Island", "holey mini golf : dos", "montezuma's revenge", "salty bois chrismas", "https://steamcommunity.com/sharedfiles/filedetails/?id=1611573177", "https://steamcommunity.com/sharedfiles/filedetails/?id=1346471502", "https://steamcommunity.com/sharedfiles/filedetails/?id=1520891664&searchtext="]

secure_random = random.SystemRandom()
print(secure_random.choice(game))