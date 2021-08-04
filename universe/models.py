from django.db import models

import math
π = math.pi

class NamedEntry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        abstract = True


class SpaceBody(NamedEntry):
    color = models.CharField(max_length=10)
    diameter = models.FloatField()
    area = models.FloatField()

    @property
    def area_count(self, diameter):
        self.area = π*diameter^2
        return self.area

    area = area_count()
        


    class Meta:
        ordering = NamedEntry.Meta.ordering
        abstract = True


class Galaxy(NamedEntry):

    size_x = models.PositiveIntegerField()
    size_y = models.PositiveIntegerField()


class StarSystem(NamedEntry):
    name = models.CharField(max_length=100)
    pos_x = models.PositiveIntegerField()
    pos_y = models.PositiveIntegerField()
    galaxy = models.ForeignKey("universe.Galaxy", on_delete=models.CASCADE, related_name="systems")


class Star(SpaceBody):
    star_system = models.ForeignKey("universe.StarSystem", on_delete=models.CASCADE)
    


class Planet(SpaceBody):
    star_system = models.ForeignKey("universe.StarSystem", on_delete=models.CASCADE)
    live = models.BooleanField(default=False)


class Moon(SpaceBody):
    planet = models.ForeignKey("universe.Planet", on_delete=models.CASCADE)


