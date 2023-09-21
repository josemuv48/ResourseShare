from django.core.exceptions import ValidationError
 
 
 # CHECK(rate>0 AND rate<5)
def check_rating_range(value):
    if value < 0 or value > 5:
        raise ValidationError(f"{value} must be between 0 and 5")