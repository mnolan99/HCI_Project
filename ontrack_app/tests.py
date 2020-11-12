from django.test import TestCase
from ontrack_app.models import Review, Page
from django.urls import reverse

def add_review(title, comment):
        r = Review.objects.create()
        r.title=title
        r.comment = comment  
        r.save()
        return r
def add_page(title):
    p = Page.objects.get_or_create(title=title)[0]
    p.save()
    return p
        
        
class CategoryMethodTests(TestCase): 
    def test_slug_line_creation(self): 
        """ slug_line_creation checks to make sure that
        when we add a category an appropriate slug line 
        is created i.e. "Random Category String" -> 
        "random-category-string" """ 
        page = Page(title="Test Slug String") 
        page.save() 
        self.assertEqual(page.slug, 'test-slug-string')
        
        
class IndexViewTests(TestCase):
    def test_index_view_with_no_reviews(self): 
        """ If no questions exist, an appropriate message 
        should be displayed. """ 
        response = self.client.get(reverse('index')) 
        self.assertEqual(response.status_code, 200) 
        
        
    def test_index_view_with_categories(self):
        add_review('test', "test1") 
        add_review('temp',"test2") 
        add_review('tmp', "test3") 
        add_review('tmp test temp', "test4")

        response = self.client.get(reverse('index')) 
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 2) #ReviewID autoincrements so response will contain 1-4
     
    def test_index_view_with_no_page(self): 
        """ If no questions exist, an appropriate message 
        should be displayed. """ 
        response = self.client.get(reverse('index')) 
        self.assertEqual(response.status_code, 200) 
        
        
    def test_index_view_with_pages(self):
        add_page('test') 
        add_page('temp') 
        add_page('tmp')
        add_page('tmp test temp')

        response = self.client.get(reverse('index')) 
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 1)
        
    