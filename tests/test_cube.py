from core.state import CubeState

def test_initial_state_is_solved():
    cube = CubeState()
    assert cube.is_solved()

def test_all_moves_4x():
    for move in ["U", "D", "F", "B", "R", "L", "M", "E"]:
        cube = CubeState()
        cube.apply_move(move)
        assert not cube.is_solved()
        for _ in range(3):
            cube.apply_move(move)
        assert cube.is_solved()

def test_sexy_move_6x():
    cube = CubeState()
    for _ in range(6):
        cube.apply_algorithm("R U R' U'")
    assert cube.is_solved()

def test_t_perm_2x():
    cube = CubeState()
    t_perm = "R U R' U' R' F R2 U' R' U' R U R' F'"
    for _ in range(2):
        cube.apply_algorithm(t_perm)
    assert cube.is_solved()

def test_jb_perm_2x():
    cube = CubeState()
    jb_perm = "R U R' F' R U R' U' R' F R2 U' R' U'" 
    for _ in range(2):
        cube.apply_algorithm(jb_perm)
    assert cube.is_solved()

def test_h_perm_2x():
    cube = CubeState()
    h_perm = "M2 U M2 U2 M2 U M2"
    for _ in range(2):
        cube.apply_algorithm(h_perm)
    assert cube.is_solved()

def test_f2l():
    cube = CubeState()
    scramble = "F2 L B D' L D B' L' F2 D2 L U2 L' U2 L U2 L' D2"
    cube.apply_algorithm(scramble)
    assert cube.is_f2l_solved()