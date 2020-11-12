from django import forms
from ontrack_app.models import UserProfile, Review, Page, ContactForm
from django.contrib.auth.models import User

#the form for a review
class ReviewForm(forms.ModelForm):
    title = forms.CharField(widget=forms.HiddenInput(), initial="")
    
    price = forms.IntegerField(help_text="Rate the price.")
    quality = forms.IntegerField(help_text="Rate the quality.")
    atmosphere = forms.IntegerField(help_text="Rate the atmosphere.")
    
    comment = forms.CharField(max_length=128, help_text="Please enter a comment.")
    avgRating = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    
    class Meta:
        model = Review
        fields = ('reviewID','title','price','quality','atmosphere','avgRating','comment',)
        
#the form for the base review class
class Reviews(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('reviewID','title','comment','price','quality','atmosphere','avgRating',)

#the form for the base user class
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#the from for the users profile
class UserProfileForm(forms.ModelForm):
    class Meta:
            model = UserProfile
            fields = ('picture',)



#the form for the contact us page  
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True, max_length=11)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = ContactForm
    