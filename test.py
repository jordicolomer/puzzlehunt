from zoo import *

def test_rule12():
    assert rule12([albatross]) == True
    assert rule12([]) == True
    assert rule12([albatross, flamingo]) == True
    assert rule12([albatross, flamingo, swan]) == True
    assert rule12([albatross, swan, flamingo]) == True