sqlalchemy based select fields for wtforms
==========================================

:date: 2008-03-10
:tags: python, web
:category: old


I did a few forms wasted much time doing all the choice stuff by myself, so i put together a simple class which manages it for me::

    from wtforms import SelectField

    class SelectRelated(SelectField):
        def __init__(self, type_, has_any=False, *k, **kw):

            self.type = type_
            #XXX: this is a killer
            items = type_.query.all()
            choices = [(x.slug, x.name) for x in items]
            self.objects = dict((x.slug, x) for x in items)

            if has_any:
                slug = 'Any ' + type_.__name__
                choices = [('any', slug)] + choices
                self.objects['any'] = None

            SelectField.__init__(self,
                    choices=choices,
                    checker=self.objects.get, *k, **kw)

        def process_data(self, value, has_formdata):
            self.data = value.slug

        def _validate(self, *args):
            print self.type, self.data
            if self.data not in self.objects.values():
                raise v.ValidationError('Not a valid choice')

