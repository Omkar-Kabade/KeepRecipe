from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator
# Create your models here.



class Tags(models.Model):
    food_type = models.CharField(max_length = 20)

    def __str__(self) :
        return f"{self.food_type}"
    
    class Meta:
        verbose_name_plural = "Tags(Cooking time & Food Type)"

class Recipe(models.Model):
    title = models.CharField(max_length=50 )
    ingrediants = models.TextField(max_length=150)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)],default=1
    )
    process = models.TextField(max_length=450 )
    chef = models.CharField(max_length=40)
    food_image = models.ImageField(upload_to="images")
    slug = models.SlugField(unique=True,db_index=True)
    post_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tags)
    def __str__(self):
        return f"{self.title}" 


class Comments(models.Model):
    user_name = models.CharField(max_length=24)
    comment = models.TextField(max_length=450,validators=[MinLengthValidator(20)])
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")

    def __str__(self) :
        return f"{self.user_name} Comments On {self.recipe}"

