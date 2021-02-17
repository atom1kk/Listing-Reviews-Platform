from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(status='active')


class Category(models.Model):
	title = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=250, unique=True)

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title

class Company(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('active', 'Active'),
	)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=250)
	category = models.ForeignKey(Category, related_name='company_category', on_delete=models.CASCADE)
	owner = models.ForeignKey(User, related_name='company_owner', on_delete=models.CASCADE)
	description = models.TextField()
	avatar = models.ImageField(upload_to='companies/profile_avatars/', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
	active = PublishedManager()

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title

	def average_rating(self):
		all_reviews = self.reviews.all()
		all_ratings = 0
		if len(all_reviews) > 0:
			for review in all_reviews:
				all_ratings += review.score
			return round(all_ratings / len(all_reviews))
		return 0


