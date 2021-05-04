# json_converter
Repository with very naive JSON parser implementation (for education purposes)

# Implementation description
As a first step we try to write an algorithm that will be able to parse simple unnested JSON:
```python
def test_should_parse_simple_json():
    simple_json = '{"key1" : 1.1 , "key2":true, "key3"  :false, "key4": "i am string", "key5": 1 }'

    result = convert(simple_json)

    assert result == {"key1": 1.1, "key2": True, "key3": False, "key4": "i am string", "key5": 1}
```

First step would to learn how to parse field names. We read the JSON string from left to right and look for `"` symbols, which we treat as start of field name, which we them read symbol by symbol until we meet another `"`, after which we save field in name in `result` dict and we do this until string is read.

Maybe this diagram would help as well:
![Parsing field names](docs/parsing_field_names.png)

See the implementation here: (In progress)


# Overview of what is going on during parsing of
![state diagram](docs/states.png)
