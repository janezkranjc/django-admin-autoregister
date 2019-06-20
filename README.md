Django admin autoregister
=========================

This is a simple app that automatically registers all the models that have not yet been registered to the Django admin.

It also does the following:

- Adds all fields except `TextField` to `list_display`.
- Optimizes the database queries by selecting related fields.
- Adds fields that have `choices` set to `list_filter`.
- If a model only has one `DateField` or `DateTimeField` it adds that field to the `date_hierarchy` 
- Sets `raw_id_field` for related fields and `autocomplete_fields` for related fields that have `search_fields` set.
- Only registers models that you haven't yet registered.
- Ignores models that you wish to exclude from the admin.

Installation
------------

* Install django-admin-autoregister

```bash
pip install django-admin-autoregister
```

or 

```bash
pipenv install django-admin-autoregister
```


* Add `admin_autoregister` to the **bottom** INSTALLED_APPS setting like this:
```python
INSTALLED_APPS = [
    # ...
    'admin_autoregister',
]
```

Be extra careful to include it as the last app in the list, otherwise your own admin registrations will raise exceptions.

All your models should now be registered in the admin.

* You can use the following settings to tweak the admin auto registration:

  - `ADMIN_AUTOREGISTER_EXCLUDE` is a list of models to exclude in the admin.
    - Defaults to `['contenttypes.ContentType',
    'auth.Permission',
    'session.Session',
    'admin.LogEntry',]'`
  - `ADMIN_AUTOREGISTER_EXCLUDE_INLINES` is a boolean that determines whether or not to exclude models that are already registered as inlines of other models.
    - Defaults to `True`

Mixins
------

Each of the autoregister features can be used in your registered models by adding them as mixins.

The available mixins are:

* `admin_autoregister.mixins.ListDisplayAdminMixin` - Populates the `list_display` automatically.
* `admin_autoregister.mixins.ListFilterAdminMixin` - Populates the `list_filter` attribute automatically.
* `admin_autoregister.mixins.AutocompleteFieldsAdminMixin` - Populates the `raw_id_fields` and `autocomplete_fields` attributes automatically.
* `admin_autoregister.mixins.SelectRelatedFieldsAdminMixin` - Automatically selects all related fields with the queryset.
* `admin_autoregister.mixins.DateHierarchyAdminMixin` - Automatically sets the `date_hierarchy` if there's only one `DateTimeField` or `DateField`

Contributing
------------

Contributions are very welcome - submit a PR!
