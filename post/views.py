from django.shortcuts import render, redirect
from .models import productAdd
from django.core.mail import send_mail
from .forms import PhoneForm
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['tel']
            send_mail(
                'Вакансия',
                f'Имя: {name} \n Номер телефона: {phone}',
                'email', # enter email
                ['email'], #enter email
                fail_silently=False,
            )
            messages.success(request, 'Запрос успешно отправлен!')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка в отправке. Попробуйте снова.')
    else:
        form = PhoneForm()
    return render(request, 'index.html', context={'product': productAdd.objects.all()})

