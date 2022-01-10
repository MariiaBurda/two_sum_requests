from django.db import models


class TwoSumRequest(models.Model):
    nums = models.JSONField()
    target = models.IntegerField()

    def __str__(self):
        return f"nums: {self.nums}, target: {self.target}"
