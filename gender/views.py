# # gender/views.py
from django.shortcuts import render, redirect
from .models import UserBehavior

def home(request):
    return render(request, 'gender/home.html')

# def save_behaviors(gender, user_name, behaviors):
#     # Join multiple behaviors into a comma-separated string
#     behavior_str = ",".join(behaviors)
    
#     # Save the user and behaviors to the database
#     UserBehavior.objects.create(gender=gender, user_name=user_name, behavior=behavior_str)

# def male(request):
#     submitted_behaviors = None

#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         behaviors = request.POST.getlist('behaviors')
        
#         save_behaviors('male', user_name, behaviors)

#         # Set submitted behaviors to display in the template
#         submitted_behaviors = ", ".join(behaviors)

#     return render(request, 'gender/male.html', {'submitted_behaviors': submitted_behaviors})

# def female(request):
#     submitted_behaviors = None

#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         behaviors = request.POST.getlist('behaviors')
        
#         save_behaviors('female', user_name, behaviors)

#         # Set submitted behaviors to display in the template
#         submitted_behaviors = ", ".join(behaviors)

#     return render(request, 'gender/female.html', {'submitted_behaviors': submitted_behaviors})


# gender/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import UserBehavior

def save_behaviors(gender, user_name, behaviors):
    # Join multiple behaviors into a comma-separated string
    behavior_str = ",".join(behaviors)
    
    # Save the user and behaviors to the database
    UserBehavior.objects.create(gender=gender, user_name=user_name, behavior=behavior_str)

def male(request):
    submitted_behaviors = None

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        behaviors = request.POST.getlist('behaviors')
        
        save_behaviors('male', user_name, behaviors)

        # Set submitted behaviors to display in the template
        submitted_behaviors = ", ".join(behaviors)

        # Redirect to the message page
        return redirect(reverse('message', kwargs={'submitted_behaviors': submitted_behaviors}))

    return render(request, 'gender/male.html', {'submitted_behaviors': submitted_behaviors})

def female(request):
    submitted_behaviors = None

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        behaviors = request.POST.getlist('behaviors')
        
        save_behaviors('female', user_name, behaviors)

        # Set submitted behaviors to display in the template
        submitted_behaviors = ", ".join(behaviors)

        # Redirect to the message page
        return redirect(reverse('message', kwargs={'submitted_behaviors': submitted_behaviors}))

    return render(request, 'gender/female.html', {'submitted_behaviors': submitted_behaviors})

def message(request, submitted_behaviors):
    return render(request, 'gender/message.html', {'submitted_behaviors': submitted_behaviors})







# -------------------------------------------------------------------------------------

# # def male(request):
# #     if request.method == 'POST':
# #         user_name = request.POST.get('user_name')
# #         behavior = request.POST.get('behavior')
# #         UserBehavior.objects.create(gender='male', user_name=user_name, behavior=behavior)
# #         return redirect('home')
# #     return render(request, 'gender/male.html')

# # gender/views.py
# from django.shortcuts import render, redirect
# from .models import UserBehavior

# # def male(request):
# #     if request.method == 'POST':
# #         user_name = request.POST.get('user_name')
# #         behaviors = request.POST.getlist('behaviors')

# #         for behavior in behaviors:
# #             UserBehavior.objects.create(gender='male', user_name=user_name, behavior=behavior)

# #         return redirect('home')

# #     return render(request, 'gender/male.html')

# # gender/views.py
# from django.shortcuts import render, redirect
# from .models import UserBehavior

# def male(request):
#     submitted_behaviors = None

#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         behaviors = request.POST.getlist('behaviors')

#         for behavior in behaviors:
#             UserBehavior.objects.create(gender='male', user_name=user_name, behavior=behavior)

#         # Set submitted behaviors to display in the template
#         submitted_behaviors = ", ".join(behaviors)

#     return render(request, 'gender/male.html', {'submitted_behaviors': submitted_behaviors})

# # def female(request):
# #     if request.method == 'POST':
# #         user_name = request.POST.get('user_name')
# #         behavior = request.POST.get('behavior')
# #         UserBehavior.objects.create(gender='female', user_name=user_name, behavior=behavior)
# #         return redirect('home')
# #     return render(request, 'gender/female.html')

# def female(request):
#     submitted_behaviors = None

#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         behaviors = request.POST.getlist('behaviors')

#         for behavior in behaviors:
#             UserBehavior.objects.create(gender='female', user_name=user_name, behavior=behavior)

#         # Set submitted behaviors to display in the template
#         submitted_behaviors = ", ".join(behaviors)

#     return render(request, 'gender/female.html', {'submitted_behaviors': submitted_behaviors})
# gender/views.py

