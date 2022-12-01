import json
import os
from typing import Dict, List, Optional

__all__ = [
    'save_to_json_file',
    'load_from_json_file'
]


def save_to_json_file(obj, file_path: str) -> None:
    json_file = json.dumps(obj.__dict__, indent=4, sort_keys=True, default=str)
    if os.path.exists(file_path) and not os.stat(file_path).st_size == 0:
        with open(file_path, 'r') as file:
            data = json.load(file)
            data.append(json_file)
        with open(file_path, 'w') as file:
            json.dump(data, file)
    else:
        with open(file_path, 'w') as file:
            json.dump([json_file, ], file)


def load_from_json_file(file_path: str) -> Optional[List[Dict]]:
    if os.path.exists(file_path) and not os.stat(file_path).st_size == 0:
        with open(file_path) as json_file:
            objects = [json.loads(data) for data in json.load(json_file)]
        return objects
