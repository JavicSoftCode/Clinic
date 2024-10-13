from django.contrib import admin

from .models import Menu, Module, GroupModulePermission, CustomUser, SuperUser , UserAdmin


class MenuAdmin(admin.ModelAdmin):
  list_display = ('name', 'get_icon')
  search_fields = ('name',)
  ordering = ('-name',)

  class Media:
    css = {
      'all': ('css/adminDjango.css',)
    }


class ModuleAdmin(admin.ModelAdmin):
  list_display = ('name', 'url', 'menu', 'is_active')
  search_fields = ('name', 'url')
  ordering = ('-name',)

  class Media:
    css = {
      'all': ('css/adminDjango.css',)
    }


class GroupModulePermissionAdmin(admin.ModelAdmin):
  list_display = ('group', 'module', 'permission')
  list_filter = ('group', 'module')
  search_fields = ('group__name', 'module__name', 'permission__codename')
  ordering = ('-id',)

  class Media:
    css = {
      'all': ('css/adminDjango.css',)
    }


# Registro de los modelos personalizados en el admin
admin.site.register(SuperUser)
admin.site.register(UserAdmin)
admin.site.register(CustomUser)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(GroupModulePermission, GroupModulePermissionAdmin)
