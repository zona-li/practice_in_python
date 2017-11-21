from single_linked_lists import *


def test_push():
    colors = SingleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors.push("Royal Purple")
    assert colors.count() == 3

def test_pop():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None

def test_unshift():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    colors.push("Viridian")
    assert colors.unshift() == "Magenta"
    assert colors.unshift() == "Alizarin"
    assert colors.unshift() == "Viridian"
    assert colors.unshift() == None