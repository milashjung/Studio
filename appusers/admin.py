from django.contrib import admin
from .models import Client, Feedback,Photo,Post,Payment,bphotographer,Photoc,PhotoCategory
# Register your models here. (by sumit.luv)
class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientAdmin)

class PhotoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Photo, PhotoAdmin)




admin.site.register(Payment)


admin.site.register(Post)
admin.site.register(Feedback)


class PhotocAdmin(admin.ModelAdmin):
    pass
admin.site.register(Photoc, PhotocAdmin)


class PhotoCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(PhotoCategory, PhotoCategoryAdmin)

class bphotographerAdmin(admin.ModelAdmin):
    pass
admin.site.register(bphotographer, bphotographerAdmin)