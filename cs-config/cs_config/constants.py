import paramtools
from marshmallow import fields, Schema


class MetaParameters(paramtools.Parameters):
    array_first = True
    defaults = {
        "year": {
            "title": "Year",
            "description": "Year for parameters.",
            "type": "int",
            "value": 2020,
            "validators": {
                "choice": {
                    "choices": [
                        yr for yr in range(2020, 2030 + 1)
                    ]
                }
            }
        }
    }
