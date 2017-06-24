from zoo import *


def test_rule12():
    assert rule12([albatross]) == True
    assert rule12([]) == True
    assert rule12([albatross, flamingo]) == True
    assert rule12([albatross, flamingo, swan]) == True
    assert rule12([albatross, flamingo, meetkat, swan]) == True
    assert rule12([swan, flamingo]) == False
    assert rule12([swan, meetkat, flamingo]) == False
    assert rule12([albatross, swan, flamingo]) == False


def test_rule3():
    assert rule3([swan, meetkat, lion, warthog]) == True
    assert rule3([meetkat, lion, warthog]) == True
    assert rule3([warthog, lion, meetkat]) == True
    assert rule3([warthog, lion, swan, meetkat]) == True
    assert rule3([warthog, swan, meetkat]) == False
    assert rule3([warthog, swan]) == True


