from django import forms
from .models import FeedLink
from .rss_url_validator import validate_url


class AddFeedForm(forms.ModelForm):
	class Meta:
		model = FeedLink
		fields = [
			"feed_url",
			"category"
		]

	def clean_feed_url(self):
		link = self.cleaned_data.get("feed_url")
		if validate_url(link):
			return link
		else:
			raise forms.ValidationError("Please Enter a Valid RSS Feed URL")