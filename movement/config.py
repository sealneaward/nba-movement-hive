from _config_section import ConfigSection

import os
from movement.constant import data_dir

REAL_PATH = data_dir

data = ConfigSection("data")
data.dir = "%s/%s" % (REAL_PATH, "data")

data.movement = ConfigSection("movement data")
data.movement.dir = "%s/%s" % (data.dir, "movement")

data.shots = ConfigSection("shot information data")
data.shots.dir = "%s/%s" % (data.dir, "shots")
