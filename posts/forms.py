from django.forms import ModelForm, Textarea

from posts.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
        widgets = {
            'content': Textarea(attrs={'class': 'textarea',
                                       'rows': 2,
                                       'cols': 0}),
        }