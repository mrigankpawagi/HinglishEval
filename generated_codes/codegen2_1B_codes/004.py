from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Diye gaye input numbers ki list ke liye, dataset ka Mean Absolute Deviation calculate karo.
    Mean Absolute Deviation woh average absolute difference hota hai jo har element aur ek centerpoint (is case mein mean) ke beech hota hai:
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    return sum(abs(x - x_mean) for x, x_mean in zip(numbers, mean(numbers)))
<|python|>from django.db import models
from django.db.models.deletion import CASCADE
from.contestants_model import ContestantModel


class Poll(models.Model):
    name=models.CharField(max_length=50)
    time=models.TimeField()
    contestants=models.ForeignKey(
        to=ContestantModel, on_delete=CASCADE,
        null=True, default=None
    )
    options=models.ManyToManyField(
        to=VoteOption, on_delete=CASCADE,
        default=None
    )
    def __str__(self):
        return self.name
    class Meta:
        ordering=("time","contestants__name",)
        unique_together= ("name","time",)  #