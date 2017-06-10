from django.contrib import admin
from models import *

# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['gtitle','gpic','gprice','isDelete','gunit','gclick','gjianjie','gkucun','gcontent','gtype']

admin.site.register(GoodsInfo,GoodsInfoAdmin)

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['ttitle','isDelete']

admin.site.register(TypeInfo,TypeInfoAdmin)
