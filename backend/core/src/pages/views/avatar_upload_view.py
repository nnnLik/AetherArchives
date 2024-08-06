from typing import Any

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

from src.core.models import AetherUser


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = AetherUser
        fields = ("avatar",)
        widgets = {"avatar": forms.ClearableFileInput(attrs={"accept": "image/*"})}


class AvatarUploadView(LoginRequiredMixin, FormView):
    form_class = AvatarUploadForm
    template_name = "user_page/user_page.html"
    success_url = reverse_lazy("user_page")

    def form_valid(self, form: AvatarUploadForm) -> HttpResponseRedirect:
        user = self.request.user
        user.avatar = form.cleaned_data["avatar"]
        user.save()

        referer = self.request.META.get("HTTP_REFERER")
        if referer:
            return HttpResponseRedirect(referer)

        return super().form_valid(form)

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.request.user
        print("ASAs")
        return kwargs
