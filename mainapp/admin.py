from django.contrib import admin
from .models import PostPortfolio, Opcion, EnviarContacto,Blog


class PostPage_Admin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Opcion)
admin.site.register(PostPortfolio)
admin.site.register(EnviarContacto)
admin.site.register(Blog)

