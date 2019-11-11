from django.test import TestCase
from.models import Image,Photo,location

# Create your tests here.
class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        
    # Testing  instance
    def test_instance(self):
        
   # Testing Save Method
    def test_save_method(self):
        editors = Image.objects.all()
        self.assertTrue(len(editors) > 0) 
class PhotoTestClass(TestCase):
    def setUp(self):
        
        
        #creating a new tag and saving it
        self.new_Tag(name='testing')
        self.new_Tag.save()
        
        self.new_Photo= Photo(title = 'Test Photo',post = 'This is a random test Post',image = self.rita)
        self.new_Photo.save()
        
        self.new_Photo.location.add(self.new_Tag)
    
    def tearDown(self):
        Image.objects.all().delete() 
        location.object.all().delete()
        Photo.object.all().delete()    