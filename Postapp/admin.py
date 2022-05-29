from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display=("title", "author",)
	list_filter=("title",)
	def has_change_permission(self, request, obj=None):
		if obj and (request.user == obj.author):
			return True
		return False

admin.site.register(Post, PostAdmin)