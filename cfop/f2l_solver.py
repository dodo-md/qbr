import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.state import CubeState
from collections import deque
import os
import pickle

def get_slot_state(cube, slot_idx):
    c_pos = cube.cp.index(slot_idx); c_ori = cube.co[c_pos]
    e_pos = cube.ep.index(slot_idx); e_ori = cube.eo[e_pos]
    return (c_pos, c_ori, e_pos, e_ori)