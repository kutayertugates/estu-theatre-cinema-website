from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from Period.models import Period
from Account.models import CustomUser, Department

def Login(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        if 'register_btn' in request.POST:
            latest_period = Period.objects.order_by('-start_year').first()

            first_name = request.POST.get('r_first_name')
            last_name = request.POST.get('r_last_name')
            email = request.POST.get('r_email')
            password = request.POST.get('r_password')
            re_password = request.POST.get('r_repassword')
            phone = request.POST.get('r_phone')
            department_id = request.POST.get('r_department')
            r_tc = request.POST.get('r_tc')
            terms = request.POST.get('r_terms')
            receipt_file = request.FILES.get('r_receipt')

            if password != re_password:
                messages.error(request, "Şifreler birbiriyle uyuşmuyor!")
                return redirect('Account:login')

            try:
                new_member = CustomUser(
                    period = latest_period,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    phone = phone,
                    department_id = department_id,
                    tc_no = r_tc
                )
                new_member.set_password(password)

                if receipt_file:
                    new_member.receipt = receipt_file

                new_member.save()
                
                messages.success(request, "Kayıt işlemi başarıyla gerçekleşti")
            except Exception as e:
                pass
        elif 'login_btn' in request.POST:
            email = request.POST.get('l_email')
            password = request.POST.get('l_password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Giriş işlemi başarıyla gerçekleşti")
                return redirect('Account:login')
            else:
                messages.error(request, 'E-Posta veya şifre yanlış')
                return redirect('Account:login')

    return render(request, 'Account/login.html', context={
        "departments" : departments
    })

def Profile(request):
    return render(request, 'Account/profile.html')