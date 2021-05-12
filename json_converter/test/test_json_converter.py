from json_converter.json_converter import convert


def test_should_parse_simple_json():
    simple_json = '{"key1" : 1.1 , "key2":true, "key3"  :false, "key4": "i am string", "key5": 1 }'

    result = convert(simple_json)

    assert result == {"key1": 1.1, "key2": True, "key3": False, "key4": "i am string", "key5": 1}


def test_should_parse_nested_json():
    simple_json = '{"key1" :1.1, "key2": true, "key3": {"key": {"key": "value"}}, "key4": "i am string", "key5": 1}'

    result = convert(simple_json)

    assert result == {"key1" :1.1, "key2": True, "key3": {"key": {"key": "value"}}, "key4": "i am string", "key5": 1}


def test_should_parse_json_with_arrays():
    simple_json = '{"key1" : [3, {"key": {"key": [1,2]}, "key1": 1},1], "key2": 2}'

    result = convert(simple_json)

    assert result == {"key1": [3, {"key": {"key": [1,2]}, "key1": 1}, 1], "key2":2}


def test_should_parse_json_with_nested_arrays():
    simple_json = '{"key1":[3, [1,2], {"key": {"key": [1,2]}, "key1": 1},1], "key2": 2}'

    result = convert(simple_json)

    assert result == {"key1":[3, [1,2], {"key": {"key": [1,2]}, "key1": 1},1], "key2": 2}


def test_should_ignore_closing_curly_brackets_in_strings():
    simple_json = '{"key1": "asd}a"}'

    result = convert(simple_json)

    assert result == {"key1": "asd}a"}


def test_should_ignore_closing_sq_brackets_in_strings():
    simple_json = '{"key1": "asd]a"}'

    result = convert(simple_json)

    assert result == {"key1": "asd]a"}


def test_should_ignore_closing_brackets_in_strings_with_nested_objects():
    simple_json = '{"key1": {"key": "asd]a"}}'

    result = convert(simple_json)

    assert result == {"key1": {"key": "asd]a"}}
