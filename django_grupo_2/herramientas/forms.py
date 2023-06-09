

class ParentWithChildrenForm:
    structure = {}

    def __init__(self, *args, **kwargs):
        dictionary, self.instance = self.get_forms_data(kwargs)

        self.parent = self.structure['parent'](*args, **dictionary,
            instance = self.instance
        )

        self.childrens = []
        for children in self.structure['childrens']:
            self.childrens.append(
                children['children'](*args, **dictionary,
                    instance = getattr(self.instance, children['related_name'])
                )
            )

    def get_forms_data(self, kwargs):
        dictionary = dict(kwargs)
        return dictionary, dictionary.pop('instance')

    def is_valid(self):
        returned_value = self.parent.is_valid()
        for children in self.childrens:
            returned_value = returned_value and children.is_valid()

        return returned_value

    # Nota: podria/puede haber problemas de atomicidad aca.
    def save(self):
        for children in self.childrens:
            children.save()

        return self.parent.save()