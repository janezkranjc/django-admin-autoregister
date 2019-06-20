from django.contrib import admin

dummy_admin = type('dummyadmin', (object,),
                   {
                       'search_fields': []
                   })()


class ListDisplayAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = ['__str__', ] + [field.name for field in model._meta.fields if field.name != 'id'
                                             and type(field).__name__ != 'TextField']
        super().__init__(model, admin_site)


class ListFilterAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_filter = [field.name for field in model._meta.fields if field.choices]
        super().__init__(model, admin_site)


class AutocompleteFieldsAdminMixin(object):
    def __init__(self, model, admin_site):
        self.autocomplete_fields = [field.name for field in model._meta.fields if
                                    field.is_relation and admin.site._registry.get(
                                        field.related_model, dummy_admin
                                    ).search_fields]
        self.raw_id_fields = [field.name for field in model._meta.fields if
                              field.is_relation and not admin.site._registry.get(field.related_model,
                                                                                 dummy_admin).search_fields]
        super().__init__(model, admin_site)


class SelectRelatedFieldsAdminMixin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        related_fields = [field.name for field in self.model._meta.fields if field.is_relation]
        if related_fields:
            qs = qs.select_related(*related_fields)
        return qs


class DateHierarchyAdminMixin(object):
    def __init__(self, model, admin_site):
        date_and_datetime_fields = [field.name for field in model._meta.fields if
                                    type(field).__name__ in ['DateField', 'DateTimeField']]
        self.date_hierarchy = date_and_datetime_fields[0] if len(date_and_datetime_fields) == 1 else None
        super().__init__(model, admin_site)
