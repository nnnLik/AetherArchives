from django.contrib.auth.mixins import LoginRequiredMixin as LoginMixin


class LoginRequiredMixin(LoginMixin):
    login_url = "/auth/login/"
