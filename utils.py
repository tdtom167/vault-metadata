from voluptuous import Any, Required
schema_metadata = {
    str: {
        'delivery': Any('live', 'on-demand', 'puppet'),
        Required('description'): str,
        Required('consumers'): str,
        Required('owner'): str,
        'rotation_description': str,
        'rotation_difficulty': Any('low', 'medium', 'high'),
        Required('rotation_priority'): Any('NBD', '30D', '1Q', 'OPT'),
        'sensitivity_description': str,
        Required('sensitivity_level'): Any('low', 'medium', 'high'),
        'refresh_interval': str,
        'ticket': str
            }
        }


class ConfigError():
    """Error raised in case of encountering an invalid configuration."""
