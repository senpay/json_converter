def convert(json_string: str) ->dict:

    value_started = False
    field_name = None
    result = {}

    i = 0
    while i < len(json_string):
        char = json_string[i]
        if not field_name:
            field_name, json_string = parse_field(json_string)
            json_string = skip_unnecessary_chars(json_string)
            i = 0
        elif not value_started and char == ':':
            value_started = True
        elif value_started:
            value, json_string = parse_array(json_string[i:])
            i = 0
            json_string = skip_unnecessary_chars(json_string)
            value = value if isinstance(value, list) else convert_value(value)
            result[field_name] = value

            field_name = None
            value_started = False
            continue
        i += 1
    return result


def skip_unnecessary_chars(string):
    i = 0
    all_char_skipped = False
    while not all_char_skipped and i < len(string):
        c = string[i]
        if c in (']', '}', ',', ' ', ':'):
            i += 1
        else:
            all_char_skipped = True
    return string[i:]


def parse_field(string):
    field_started = False
    field_name_builder = []

    i = 0
    while i < len(string):
        char = string[i]
        if not field_started and char == '"':
            field_started = True
        elif field_started:
            if char != '"':
                field_name_builder.append(char)
            else:
                return ''.join(field_name_builder), string[i:]
        i += 1
    raise ValueError('I really should not be here')


def parse_array(string):
    string = string.strip()
    value_list = []
    value_builder = []
    sq_brackets = []
    curly_brackets = []

    if not string.startswith('['):
        return parse_value(string)

    i = 0
    while i < len(string):
        i += 1
        char = string[i]
        if char == ',' and len(sq_brackets) == len(curly_brackets) == 0:
            value_list.append(''.join(value_builder))
            value_builder = []
        else:
            value_builder.append(char)

            if char == '[':
                sq_brackets.append('[')
            elif char == '{':
                curly_brackets.append('{')
            elif char == '}':
                curly_brackets.pop()
            elif char == ']':
                if len(sq_brackets):
                    sq_brackets.pop()
                else:
                    value_builder = value_builder[:-1]
                    value_list.append(''.join(value_builder))
                    return [convert_value(x) for x in value_list], string[i:]


def parse_object(string):
    value_builder = []
    curly_brackets = []

    for i in range(len(string)):
        char = string[i]
        if char == '{':
            curly_brackets.append('{')
        value_builder.append(char)
        if char == '}':

            if len(curly_brackets) > 1:
                curly_brackets.pop()
            else:
                value_str = ''.join(value_builder)
                return value_str, string[i:]


def parse_value(string):
    string = string.strip()
    value_builder = []
    is_string = False
    string_started = False

    if string.startswith('{'):
        return parse_object(string)

    if string.startswith('"'):
        is_string = True

    for i in range(len(string)):
        char = string[i]
        if char == '"' and is_string:
            string_started = not string_started
        if char in ('}', ',') and not string_started:
            value_str = ''.join(value_builder)
            return value_str, string[i:]
        else:
            value_builder.append(char)


def convert_value(value_str):
    value_str = value_str.strip()

    if value_str == 'true':
        return True
    elif value_str == 'false':
        return False
    elif value_str.startswith('"'):
        value_str = value_str.replace('"', '')
        return value_str
    elif value_str.startswith('{'):
        return convert(value_str)
    elif value_str.startswith('['):
        return parse_array(value_str)[0]
    elif '.' in value_str:
        return float(value_str)
    else:
        return int(value_str)
