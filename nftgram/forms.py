from django import forms
from models import Post
from nftgram.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'user_id',
            'title',
            'description',
            'nft_url'
        )