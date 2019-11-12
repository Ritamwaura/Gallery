from django.db import models

# Create your models here.
# class Image(models.Model):
#     first_name = models.CharField(max_length =30)
#     last_name = models.CharField(max_length =30)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length = 10,blank = True)
#     
#     def __str__(self):
#            return self.first_name
#     def save_editor(self):
#         self.save()
           
    #class Meta:
     #   odering = ['first_name']
        
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
  #  image = models.ForeignKey(Image) 
    location =models.ForeignKey(Location)   
    Photo_image = models.ImageField(upload_to = 'Photos/')

    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(location__name = search_term)
