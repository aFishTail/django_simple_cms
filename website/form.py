from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """留言板表单"""

    class Meta:
        model = Message
        fields = ['content', 'username', 'mobile', 'email']