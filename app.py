import json
from hashlib import sha256
from collections import defaultdict


def remove_dict_duplicates(_list: list[dict]) -> list[dict]:
    _map = defaultdict(list)
    result = list()

    for list_index, _dict in enumerate(_list):
        key = sha256(json.dumps(_dict).encode('utf-8')).hexdigest()
        _map[key].append(list_index)

    for list_indices in _map.values():
        result.append(_list[list_indices[0]])

    return result


if __name__ == '__main__':
    _list = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"},
             {"key2": "value2"}]
    print(remove_dict_duplicates(_list))
