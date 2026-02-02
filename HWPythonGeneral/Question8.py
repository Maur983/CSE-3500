def addstwo(a,b):
    return a+b
def test_addstwo():
    assert addstwo(3,6)==9, "Add fails"
if __name__ == "__main__":
    test_addstwo()