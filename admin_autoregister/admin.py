from django.apps import apps
from django.contrib import admin
from django.conf import settings
from admin_autoregister.mixins import ListDisplayAdminMixin, ListFilterAdminMixin, AutocompleteFieldsAdminMixin, \
    SelectRelatedFieldsAdminMixin, DateHierarchyAdminMixin

ADMIN_AUTOREGISTER_EXCLUDE = [model.lower() for model in getattr(settings, 'ADMIN_AUTOREGISTER_EXCLUDE', [
    'contenttypes.ContentType',
    'auth.Permission',
    'session.Session',
    'admin.LogEntry',
])]
ADMIN_AUTOREGISTER_EXCLUDE_INLINES = getattr(settings, 'ADMIN_AUTOREGISTER_EXCLUDE_INLINES', True)

ADMIN_AUTOREGISTER_UNREGISTER_LIST = getattr(settings, 'ADMIN_AUTOREGISTER_UNREGISTER_LIST', [])

inline_models = [item.model for sublist in [v.inlines for k, v in admin.site._registry.items() if len(v.inlines) > 0]
                 for item
                 in sublist] if ADMIN_AUTOREGISTER_EXCLUDE_INLINES else []

models = [model for model in apps.get_models()
          if '{app_label}.{model_name}'.format(app_label=model._meta.app_label,
                                               model_name=model._meta.model_name) not in ADMIN_AUTOREGISTER_EXCLUDE
          and model not in inline_models]
for model in models:
    admin_class = type('AutoRegisteredAdmin',
                       (ListDisplayAdminMixin, ListFilterAdminMixin, AutocompleteFieldsAdminMixin,
                        SelectRelatedFieldsAdminMixin, DateHierarchyAdminMixin,
                        admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass

unregister_models = [model for model in apps.get_models() 
                    if '{app_label}.{model_name}'.format(app_label=model._meta.app_label, 
                                                model_name=model._meta.model_name) in ADMIN_AUTOREGISTER_UNREGISTER_LIST]

for model in unregister_models:
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass
