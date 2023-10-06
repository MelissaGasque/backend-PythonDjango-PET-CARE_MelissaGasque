from django.db import models


class SexChoices(models.TextChoices):
    NOT_INFORMED = "Not Informed",
    MALE = "Male",
    FEMALE = "Female"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20,
        choices=SexChoices.choices,
        default=SexChoices.NOT_INFORMED
    )
    group = models.ForeignKey(
        "groups.Group",
        related_name="pets",
        on_delete=models.PROTECT,
    )
    traits = models.ManyToManyField(
        "traits.Trait",
        related_name="pets"
    )

    def __repr__(self) -> str:
        return f"<Pet:v {self.id} - {self.name}>"
