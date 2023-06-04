# - la recursion de formularios quedaba feita, más que nada porque no la he visto por ahí
# - primero lo intente con inlinefromset_factory pero no fui capaz de hacerlo andar.
# - luego me di cuenta que inlinefromset_factory deja cosillas en el html
# - luego me di cuenta que puede haber más de una relacion entre dos entidades y era
#   necesario declararlas para tener un esquema coherente. (inlinefromset_factory
#   descartado)
# - y luego quedo este engendro, que tiene el mismo espiriu que la versión anterior pero
#   sin recursión, ademaś me dio fiaca declarar una clase nodo y otra hoja.
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