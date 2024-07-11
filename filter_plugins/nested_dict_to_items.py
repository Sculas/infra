def nested_dict_to_items(d, parent_key='', sep='.'):
    """
    Recursively converts a nested dictionary into a list of dictionaries with fully qualified keys.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(nested_dict_to_items(v, new_key, sep=sep))
        else:
            items.append({'key': new_key, 'value': v})
    return items

class FilterModule(object):
    def filters(self):
        return {
            'nested_dict_to_items': nested_dict_to_items
        }
