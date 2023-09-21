from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.resources import validators
from apps.core.models import CreatedModifiedAtDateTimeBase


# Create your models here.

class Tag(CreatedModifiedAtDateTimeBase):
    # id = None If you don't want the default id to ne created
    name = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name
    
class Category(CreatedModifiedAtDateTimeBase):
    cat = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat
    
class Resources(CreatedModifiedAtDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    cat_id = models.ForeignKey("resources.Category",default=1, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)
    tag = models.ManyToManyField("resources.Tag", through='ResourcesTag') 
    #rate = ArrayField(base_field=models.IntegerField()) # will create a INT ARRAY
    
    class Meta:
        verbose_name_plural = "Resources"
    
    def __str__(self):
        return f"{self.user_id.username}-{self.title}"
    
    # def get_username(self):
    #     return self.user_id.username
    

    def all_tags(self):
        return ", ".join([tag.name for tag in self.tag.all()])
    
    @property    
    def username(self):
        return self.user_id.username
    
    @property    
    def user_title(self):
        return self.user_id.title
    
      
class ResourcesTag(CreatedModifiedAtDateTimeBase): # if we need extra fields we create is by our selfs
    modified_at = None
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    tag_id = models.ForeignKey("resources.Tag", on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                "resources_id",
                "tag_id",
                name = "resource_tag_unique",
                violation_error_message = f"Tag already exist for resource"
            )
        ]
    
    
    # def __str__(self):
    #     return f"{self.resources_id.title} - self.tag_id.name"
    @property
    def title(self):
        return self.resources_id.title
    
    @property
    def tag(self):
        return self.tag_id.name
    
    
class Review(CreatedModifiedAtDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    body = models.TextField()
   
    def __str__(self):
        return f"{self.user_id.username}-{self.resources_id.title}"

    def username(self):
        return self.user_id.username
    
    def user_title(self):
        return self.user_id.title

    def resource_title(self):
        return self.resources_id.title
    
    

class Rating(CreatedModifiedAtDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[validators.check_rating_range])
    
    def username(self):
        return self.user_id.username
  
    def resource_title(self):
        return self.resources_id.title