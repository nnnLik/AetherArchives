from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from src.core.models import AetherUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    class Meta:
        model = AetherUser
        fields = (
            "username",
            "email",
            "password",
        )
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }

    def clean_password_confirm(self) -> str:
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return password_confirm


class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super().form_valid(form)
