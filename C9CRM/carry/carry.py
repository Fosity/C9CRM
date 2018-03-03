from carry import models
from carry.service import carry
from carry.views.menuadmin import MenuAdmin
from carry.views.permissionadmin import PermissionAdmin
from carry.views.roleadmin import RoleAdmin
from carry.views.useradmin import UserAdmin

# Register your models here.
carry.site.register(models.User, UserAdmin)
carry.site.register(models.Role, RoleAdmin)
carry.site.register(models.Menu, MenuAdmin)
carry.site.register(models.Permission, PermissionAdmin)
