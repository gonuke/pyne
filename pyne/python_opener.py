#!/usr/bin/python
from pyne.mcnp import Mctal 
from pyne.mcnp import Tally
data = Mctal()
tally = Tally()

data.read("mctal")
tally.read("mctal")
