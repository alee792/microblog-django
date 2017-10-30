from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('content', 'user', 'created_at',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    
    def save_formset(self, request, form, formset, change): 
        if formset.model == Post:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            formset.save()


admin.site.register(Post, PostAdmin)
