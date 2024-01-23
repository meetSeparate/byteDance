from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from api.models import *


# Register your models here.

class UserInfoAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "tel", "sex", "age", "birth", "role")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "name", "tel", "sex", "age", "birth", "role")

    list_filter = ("is_staff", "is_superuser", "is_active")

    search_fields = ("username", "name", "tel")


class ProductAdmin(admin.ModelAdmin):

    def get_cover(self):
        if self.cover:
            return mark_safe(f'<img src="{self.cover}" style="height:60px; border-radius:5px;">')
        return

    get_cover.short_description = '产品封面'

    def get_logo(self):
        if self.logo:
            return mark_safe(f'<img src="{self.logo}" style="height:60px; border-radius:5px;">')

    get_logo.short_description = '产品logo'

    list_display = ['name', 'title', get_logo, get_cover, 'description', 'subDescription', 'link']

    search_fields = ['name', 'title']


class JobAdmin(admin.ModelAdmin):
    def get_category(self):
        if not self.category:
            return '无'
        return self.category.name

    get_category.short_description = '种类'

    def get_city(self):
        if not self.city:
            return '无'
        return self.city.name

    get_city.short_description = '城市'

    def get_type(self):
        if not self.recruit_type:
            return '无'
        return self.recruit_type.type

    get_type.short_description = '分类'

    list_display = ['nid', 'title', get_category, get_city, get_type, 'create_date']

    list_filter = ['category__name', 'city__name', 'recruit_type__type']

    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    def get_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image}" style="height:60px; border-radius:5px;">')

    get_image.short_description = '种类图片'

    list_display = ['nid', 'code', 'name', 'en_name', get_image]

    list_filter = ['code', 'name', 'en_name']


class RecruitTypeAdmin(admin.ModelAdmin):
    list_display = ['nid', 'type', 'en_type']

    list_filter = ['type', 'en_type']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(City, CategoryAdmin)
admin.site.register(RecruitType, RecruitTypeAdmin)