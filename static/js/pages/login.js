// UX Logic: Sayfa yenilemeden formlar arası geçiş
function switchTab(tab) {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const btnLogin = document.getElementById('btn-login');
    const btnRegister = document.getElementById('btn-register');

    if (tab === 'login') {
        // Fade out effect
        registerForm.style.opacity = '0';
        setTimeout(() => {
            registerForm.classList.add('d-none');
            loginForm.classList.remove('d-none');
            // Fade in effect start
            setTimeout(() => {
                loginForm.style.opacity = '1';
            }, 50);
        }, 300); // CSS transition süresiyle uyumlu bekleme

        btnLogin.classList.add('active');
        btnRegister.classList.remove('active');
    } else {
        loginForm.style.opacity = '0';
        setTimeout(() => {
            loginForm.classList.add('d-none');
            registerForm.classList.remove('d-none');
            setTimeout(() => {
                registerForm.style.opacity = '1';
            }, 50);
        }, 300);

        btnRegister.classList.add('active');
        btnLogin.classList.remove('active');
    }
}

document.addEventListener('DOMContentLoaded', function () {         
    const toggleIcon = document.getElementById('togglePassword');
    const passwordInput = document.getElementById('loginPassword');

    // Elementler sayfada varsa kod çalışsın (Hata almamak için)
    if (toggleIcon && passwordInput) {
        
        toggleIcon.addEventListener('click', function () {
            
            // 1. Tıklama anındaki güncel tipi al (her seferinde kontrol et)
            const currentType = passwordInput.getAttribute('type');
            
            // 2. Eğer şifre ise metin yap, metin ise şifre yap
            const newType = currentType === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', newType);
            
            // 3. İkonu değiştir (Göz açık/kapalı değişimi)
            this.classList.toggle('bi-eye');      // Açık gözü ekle/çıkar
            this.classList.toggle('bi-eye-slash'); // Çizgili gözü ekle/çıkar
        });
    }
});