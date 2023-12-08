from main import file_reader


def test_file_reader():
    assert file_reader.read(file_name="test_file.txt", path="tests/resources") == [
        " test-preserve-left-padding",
        "111",
        "222",
        "333",
    ]
