class GeneralHelpers:

    @staticmethod
    def update_object_attrs(obj, keys: list, data: dict) -> None:
        for key in keys:
            if key in data:
                setattr(obj, key, data.get(key))
