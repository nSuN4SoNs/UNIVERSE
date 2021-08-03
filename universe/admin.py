from django.contrib import admin
from universe.models import (
    SpaceBody,
    Galaxy,
    StarSystem,
    Star,
    Planet,
    Moon
)
# Register your models here.
@admin.register(SpaceBody)
class SpaceBodyAdmin(admin.ModelAdmin):
    pass


@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    pass


@admin.register(StarSystem)
class StarSystemAdmin(admin.ModelAdmin):
    pass


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    pass


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass


@admin.register(Moon)
class MoonAdmin(admin.ModelAdmin):
    pass
