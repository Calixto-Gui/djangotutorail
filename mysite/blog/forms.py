from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'post_text', 'pub_date', 'photo')
        widgets = {
            'pub_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_name','comment_text', 'like')
