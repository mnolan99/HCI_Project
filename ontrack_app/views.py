from django.shortcuts import render
from django.http import HttpResponse
from ontrack_app.models import Review, Page
from ontrack_app.forms import UserForm, UserProfileForm, ContactForm,ReviewForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError

#collects cookie and returns response
def index(request):
    request.session.set_test_cookie()
    visitor_cookie_handler(request)
    response = render(request, 'ontrack_app/index.html',)
    return response

#gets restaurant name and prints status
def search(request):
    if request.method == 'GET':
        restaurant_name = request.GET.get('q')
        status = Page.objects.filter(title__icontains=restaurant_name)
        print(status)

    return render(request, 'ontrack_app/search.html', {'pages':status})


#shows if cookies are working
def about(request):
    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED!")
        request.session.delete_test_cookie()
    return render(request, 'ontrack_app/about.html')
    
    
def FAQ(request):
    return render(request, 'ontrack_app/FAQ.html')

def tAndC(request):
    return render(request, 'ontrack_app/t&cs.html')

def appointments(request):
    return render(request, 'ontrack_app/appointments.html')

def updates(request):
    return render(request, 'ontrack_app/updates.html')

#sends email for when user uses contact us including all details and message
def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            try:
                send_mail('contact form','phone: ' +phone + ' name: ' + name + ' message: ' + message, from_email,['westendrestaurant@gmail.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
    return render(request, "ontrack_app/contact-us.html", {'form': form})


def invalidLogin(request):
    return render(request, 'ontrack_app/invalidLogin.html')

#uses user and profile forms to register user and validate login details
def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request, 'ontrack_app/register.html', {'user_form': user_form, 
	'profile_form': profile_form, 'registered': registered})

#validate login details and logs user in
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your OnTrack account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return render(request, 'ontrack_app/invalidLogin.html', {})

	else:
		return render(request, 'ontrack_app/index.html', {})

@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")

#logs user out
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

#shows reviews   
def review(request, page_name_slug):
    #review_list = Review.objects.order_by('reviewID')[:4] 
    #pages = Page.objects.order_by('title')[:4]
    #context_dict = {'reviews': review_list, 'pages':pages}
    
    context_dict = {}
    try:
        page = Page.objects.get(slug=page_name_slug)
        pages = Page.objects.filter(title=page.title)
        reviews = Review.objects.filter(title=page.title)
        context_dict['pages'] = pages
        context_dict['page'] = page
        context_dict['reviews'] = reviews
        
        #name
    except Page.DoesNotExist:
        context_dict['page'] = None
        context_dict['pages'] = None 

    return render(request, 'ontrack_app/review.html', context_dict)    

#adds reviews to database using forms
def add_review(request, page_name_slug):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
           
    context_dict = {}
    try:
    
        context_dict['form'] = form
        page = Page.objects.get(slug=page_name_slug)
        pages = Page.objects.filter(title=page.title)
        context_dict['pages'] = pages
        context_dict['page'] = page
    except Page.DoesNotExist:
        context_dict['page'] = None
        context_dict['pages'] = None 
    return render(request, 'ontrack_app/add_review.html', context_dict)
#outlnes reviews of restaurants
def restaurant(request):
    review_list = Review.objects.order_by('reviewID') 
    pages = Page.objects.order_by('title')
    print(pages[0])
    context_dict = {'reviews': review_list, 'pages':pages}

    return render(request, 'ontrack_app/restaurant.html', context_dict)
#same as restaurant but only for on campus
def onCampus(request):
    review_list = Review.objects.order_by('reviewID') 
    pages = Page.objects.order_by('title')
    context_dict = {'reviews': review_list, 'pages':pages}

    return render(request, 'ontrack_app/onCampus.html', context_dict)
#same as restaurant but only for off campus   
def offCampus(request):
    review_list = Review.objects.order_by('reviewID') 
    pages = Page.objects.order_by('title')
    context_dict = {'reviews': review_list, 'pages':pages}

    return render(request, 'ontrack_app/offCampus.html', context_dict)


# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

# Updated the function definition
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
# If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
    #update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # set the last visit cookie
            request.session['last_visit'] = last_visit_cookie
    # Update/set the visits cookie
    request.session['visits'] = visits
