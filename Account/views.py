from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from Period.models import Period
from Account.models import CustomUser, Department

def Logout(request):
    logout(request)
    
    messages.success(request, "Başarıyla çıkış yaptınız.")
    return redirect('Account:Login')

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
                return redirect('Account:Login')

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
                
                messages.success(request, "Kayıt işlemi başarıyla gerçekleşti.")
            except Exception as e:
                pass
        elif 'login_btn' in request.POST:
            email = request.POST.get('l_email')
            password = request.POST.get('l_password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Giriş işlemi başarıyla gerçekleşti.")
                return redirect('Account:Login')
            else:
                messages.error(request, 'E-Posta veya şifre yanlış.')
                return redirect('Account:Login')

    return render(request, 'Account/login.html', context={
        "departments" : departments
    })



def Profile(request):
    if not request.user.is_authenticated:
        redirect('Account:Login')
    
    if request.method == 'POST':
        if 'update_btn' in request.POST:
            current_user = request.user

            current_user.first_name = request.POST.get('u_first_name')
            current_user.last_name = request.POST.get('u_last_name')
            current_user.phone = request.POST.get('u_phone')
            current_user.department_id = request.POST.get('u_department')

            try:
                current_user.save()
                messages.success(request, 'Profil Başarıyla güncellendi.')
                redirect('Account:Profile')
            except Exception as e:
                messages.error(request, 'Teknik bir hata gerçekleşti.')
                redirect('Account:Profile')
        elif 'update_password_btn' in request.POST:
            old_pass = request.POST.get('old_password')
            new_pass = request.POST.get('new_password')
            confirm_pass = request.POST.get('confirm_password')
            
            current_user = request.user

            if not current_user.check_password(old_pass):
                messages.error(request, "Mevcut şifrenizi yanlış girdiniz!")
                return redirect('Account:Profile')

            if new_pass != confirm_pass:
                messages.error(request, "Yeni şifreler birbiriyle uyuşmuyor!")
                return redirect('Account:Profile')
            
            if current_user.check_password(new_pass):
                messages.warning(request, "Yeni şifreniz eskisiyle aynı olamaz.")
                return redirect('Account:Profile')

            if len(new_pass) < 6:
                messages.warning(request, "Şifreniz en az 8 karakter olmalıdır.")
                return redirect('Account:Profile')

            try:
                current_user.set_password(new_pass)
                current_user.save()
                
                update_session_auth_hash(request, current_user)
                
                messages.success(request, "Şifreniz başarıyla değiştirildi.")
                return redirect('Account:Profile')

            except Exception as e:
                messages.error(request, "Bir hata oluştu, tekrar deneyin.")
                return redirect('Account:Profile')

    departments = Department.objects.all()
    return render(request, 'Account/profile.html', context={
        "departments" : departments
    })