from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "phone_number")
        error_messages = {
            'username': {'required': 'نام کاربری الزامی است.'},
            'phone_number': {'required': 'شماره تلفن الزامی است.'},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # حذف help_text های انگلیسی
        for f in ("username", "password1", "password2"):
            if f in self.fields:
                self.fields[f].help_text = None

        # فارسی کردن label ها
        self.fields["username"].label = "نام کاربری"
        self.fields["password1"].label = "رمز عبور"
        self.fields["password2"].label = "تکرار رمز عبور"
        self.fields["phone_number"].label = "شماره تلفن"

        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
