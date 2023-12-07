print("Hello, world!")

def test_hello_world():
    assert print("Hello, world!") == "Hello, world!"
    if __name__ == "__main__":
        test_hello_world()