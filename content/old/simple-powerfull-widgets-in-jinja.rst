simple powerfull widgets in jinja
=================================

:date: 2007-09-22
:tags: python, jinja, templates
:category: old


These days i hit a case, where jinja macros didn't fit any more,
since they don't support keyword parameters.

So i created a small widget system wich supports those.

The basic primitive is

.. code:: python

  class Widget(object):
      jinja_context_callable = True

      TEMPLATE = None

      def __call__(self, env, context, **kwargs):
          if not self.TEMPLATE:
              self.TEMPLATE = self.__class__.__name__.lower()
          template = env.get_template('widgets/%s.jinja'%self.TEMPLATE)
          return template.render(kwargs)

Wich is a nice and simple tool.

All you have to do is subclass and add a instance to the template globals


Example taken from one of my apps

.. code:: python

  class Select(Widget):
      TEMPLATE = 'display_select'


      def __call__(self, env, context, name,
                         has_any=True, items=None, selected=None):
          selected = context['request'].values.get(name) or selected

          if items is None:
              items = context[name + 's'] # XXX: hack

          display_items = [ (item.slug, item.name) for item in items ]


          return Widget.__call__(self, env, context,
                  items=display_items,
                  name=name,
                  selected=selected,
                  has_any=has_any,
                  )

and the fitting template fragment:

.. code:: html+jinja

  <select name="{{name}}">
  {%- if has_any %}
    <option value="any">Any {{ name|title }}
  {%- endif %}
  {%- for key, name in items %}
    <option value="{{ key|e }}"
            {%- if key==selected %} selected="selected"{% endif %}>
            {{- name|e -}}
    </option>
  {%- endfor %}
  </select>
