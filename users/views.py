from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect

User = get_user_model()


def user_view(request):
    if request.method == 'GET':
        if request.user.is_anonymous:
            return render(request, 'users/login.html')
        else:
            return render(request, 'users/view.html', {'user':request.user, 'deliveries':request.user.deliveries.order_by('-date')})
    elif request.method == 'POST':
        if request.POST['act'] == 'login':
            user = authenticate(username=request.POST['email'], password=request.POST['password'])
            if user:
                login(request, user)
                return JsonResponse({'success':True})
            return JsonResponse({'success':False})
        elif request.POST['act'] == 'register':
            if not User.objects.filter(username=request.POST['email']).exists():
                user = User(username=request.POST['email'],
                            name=request.POST['name'],
                            phone=request.POST['phone'])
                user.set_password(request.POST['password'])
                user.save()
                login(request, user)
                return JsonResponse({'success':True})
            return JsonResponse({'success':False})


def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/user/')
