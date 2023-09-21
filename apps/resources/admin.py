from django.contrib import admin
from apps.resources.models import Tag, Category, Resources, Review, Rating, ResourcesTag
# Register your models here.

class CustomResources(admin.ModelAdmin):
    list_display = (
        'username', 
        'user_title',
        'title', 
        'link', 
        'get_tags', 
        'description'
        )
    
    @admin.display(description = "Tags")
    def get_tags(self,obj):
        return ", ".join([tag.name for tag in obj.tag.all()])
        
    
class CustomReview(admin.ModelAdmin):
    list_display = (
        'username', 
        'user_title',
        'resource_title',
        'get_body'
        )
    
    @admin.display(description = "Body")
    def get_body(self,obj):
        if len(obj.body)>50:
            return f"{obj.body[:50]}..."
    
        return f"{obj.body[:50]}"

class CustomResourcesTag(admin.ModelAdmin):
    list_display = (
        'title', 
        'tag'
        )
    
class CustomRating(admin.ModelAdmin):
    list_display = (
        'username', 
        'resource_title',
        'rate',
        )
    
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Resources, CustomResources)
admin.site.register(Review, CustomReview)
admin.site.register(ResourcesTag, CustomResourcesTag)
admin.site.register(Rating, CustomRating)

