from django.contrib import admin

from link.models import Target, TargetType, WebSiteLink, WebSiteType

admin.site.register(Target)
admin.site.register(TargetType)
# admin.site.register(WebSiteLink)
admin.site.register(WebSiteType)


@admin.register(WebSiteLink)
class WebSiteLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'target_id', 'type', 'url')
    list_filter = ('type',)
    search_fields = ('name', 'url')
