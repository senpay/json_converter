from json_converter.json_converter import convert


def test_should_parse_simple_json():
    simple_json = '{"key1" : 1.1 , "key2":true, "key3"  :false, "key4": "i am string", "key5": 1 }'

    result = convert(simple_json)

    assert result == {"key1": 1.1, "key2": True, "key3": False, "key4": "i am string", "key5": 1}


def test_should_parse_nested_json():
    simple_json = '{"key1" :1.1, "key2": true, "key3": {"key": {"key": "value"}}, "key4": "i am string", "key5": 1}'

    result = convert(simple_json)
    print(result)
    print({"key1" :1.1, "key2": True, "key3": {"key": {"key": "value"}}, "key4": "i am string", "key5": 1})

    assert result == {"key1" :1.1, "key2": True, "key3": {"key": {"key": "value"}}, "key4": "i am string", "key5": 1}


def test_should_parse_json_with_arrays():
    simple_json = '{"key1" : [3, {"key": {"key": [1,2]}, "key1": 1},1], "key2": 2}'

    result = convert(simple_json)
    print(result)

    assert result == {"key1": [3, {"key": {"key": [1,2]}, "key1": 1}, 1], "key2":2}


def test_should_parse_json_with_nested_arrays():
    simple_json = '{"key1":[3, [1,2], {"key": {"key": [1,2]}, "key1": 1},1], "key2": 2}'

    result = convert(simple_json)
    print(result)
    print({"key1":[3, [1,2], {"key": {"key": [1,2]}},1], "key2": 2})

    assert result == {"key1":[3, [1,2], {"key": {"key": [1,2]}, "key1": 1},1], "key2": 2}