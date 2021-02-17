from django.db import models
from companies.models import Company
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
import numpy as np


class Review(models.Model):
	title = models.CharField(max_length=100)
	comment = models.TextField(max_length=1000)
	score = models.IntegerField(default=3,
		validators=[MinValueValidator(1), MaxValueValidator(5)]
	)
	image = models.ImageField(upload_to='reviews/reviews_images/', blank=True)
	company = models.ForeignKey('companies.Company', related_name='reviews', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.title} - {self.company}"