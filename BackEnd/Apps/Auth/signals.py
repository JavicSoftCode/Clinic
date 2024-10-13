import logging
from django.contrib.auth.models import Group
from BackEnd.Apps.Auth.models import CustomUser
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from plyer import notification

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CustomerUserSignals:
    notifications = []

    @staticmethod
    @receiver(post_save, sender=CustomUser)
    def user_post_save(sender, instance, created, **kwargs):
        if created:
            # Lógica para manejar la creación de un nuevo usuario
            CustomerUserSignals.handle_new_user(instance)
        else:
            # Lógica para manejar la actualización de un usuario existente, pero solo si realmente se actualiza
            if instance._state.db:  # Verificar si realmente se trata de una actualización
                CustomerUserSignals.handle_user_update(instance)

    @staticmethod
    @receiver(pre_delete, sender=CustomUser)
    def user_pre_delete(sender, instance, **kwargs):
        # Lógica para manejar la eliminación de un usuario
        CustomerUserSignals.handle_user_delete(instance)

    @staticmethod
    def handle_new_user(user):
        """
        Maneja la creación de un nuevo usuario y lo asigna al grupo correspondiente.
        No se crea un grupo 'superuser'. Solo se asigna al grupo 'administrador' si es superusuario o administrador.
        """
        if user.is_superuser or hasattr(user, 'useradmin'):
            # Asignar al grupo 'administrador'
            CustomerUserSignals.assign_group(user, 'administrador')
            CustomerUserSignals.add_notification(f'Se ha creado un nuevo administrador: {user.email}')
        else:
            # Usuarios normales no necesitan ser asignados a grupos administrativos
            CustomerUserSignals.add_notification(f'Se ha creado un nuevo usuario sin acceso administrativo: {user.email}')

    @staticmethod
    def handle_user_update(user):
        """
        Maneja la actualización de un usuario y verifica si necesita ser reasignado a grupos administrativos.
        Evita cambios en superusuarios que puedan afectar la jerarquía de seguridad.
        """
        previous_roles = set(user.groups.values_list('name', flat=True))

        # Determinar roles actuales
        current_roles = set()
        if user.is_superuser or hasattr(user, 'useradmin'):
            current_roles.add('administrador')

        # Actualizar grupos si han cambiado
        if previous_roles != current_roles:
            CustomerUserSignals.update_user_groups(user, previous_roles, current_roles)

        # Notificación de actualización de usuario
        CustomerUserSignals.add_notification(f'Se ha actualizado el usuario: {user.email}')

    @staticmethod
    def update_user_groups(user, previous_roles, current_roles):
        """
        Actualiza los grupos de un usuario basado en los roles actuales.
        Solo un superusuario o administrador puede cambiar los grupos.
        """
        # Limpiar grupos existentes y asignar los nuevos
        user.groups.clear()

        for group_name in current_roles:
            CustomerUserSignals.assign_group(user, group_name)

        # Notificar sobre cambios de rol
        for group in previous_roles:
            if group not in current_roles:
                CustomerUserSignals.add_notification(f'Se ha removido el grupo {group} de {user.email}')

    @staticmethod
    def handle_user_delete(user):
        """
        Maneja la eliminación de un usuario.
        """
        CustomerUserSignals.add_notification(f'Se ha eliminado el usuario: {user.email}')

    @staticmethod
    def assign_group(user, group_name):
        """
        Asigna un grupo a un usuario.
        """
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        if created:
            CustomerUserSignals.add_notification(f'Se ha creado y asignado el grupo {group_name} a {user.email}')

    @staticmethod
    def add_notification(message):
        """
        Añade una notificación a la lista y puede enviar una notificación al usuario.
        """
        CustomerUserSignals.notifications.append(message)
        # Notificación local usando Plyer
        notification.notify(
            title='Notificación de Usuario',
            message=message,
            app_name='Sistema de Gestión'
        )
        logger.info(message)  # Log de la notificación
