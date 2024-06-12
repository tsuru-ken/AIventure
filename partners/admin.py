from django.contrib import admin

from .models import Partners,ServiceContent,AiCategory,Cost,PartnerServiceContentLabel,PartnerAicategoryLabel,PartnerCostLabel,CaseStudy,ProductInfo

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name','address', 'url','established')
    search_fields =('name','address')
    list_filter = ('established',)
    ordering = ('name',)
    fields = ('name','logo','address','url','established','services','enginner','provision','cost','product','case')

class ServiceContentAdmin(admin.ModelAdmin):
    list_display = ('division',)
    search_fields = ('division',)

class AiCategoryAdmin(admin.ModelAdmin):
    list_display = ('genre',)
    search_fields =('genre',)

class CostAdmin(admin.ModelAdmin):
    list_display = ('breakdown',)
    search_fields =('breakdown',)
    
class PartnerServiceContentLabelAdmin(admin.ModelAdmin):
    list_display =('partner','service_content')
    search_fields =('partner__name','service_content__division')

class PartnerAicategoryLabelAdmin(admin.ModelAdmin):
    list_display = ('partner','ai_category')
    search_fields = ('partner__name','ai_category__genre')

class PartnerCostLabelAdmin(admin.ModelAdmin):
    list_display=('partner','cost')
    search_fields = ('partner__name','cost__breakdown')

class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('partner', 'name','content')
    search_fields = ('partner__name','name')

class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('partner','name','content')
    search_fields = ('partner__name','name')

admin.site.register(Partners,PartnersAdmin)
admin.site.register(ServiceContent,ServiceContentAdmin)
admin.site.register(AiCategory,AiCategoryAdmin)
admin.site.register(Cost,CostAdmin)
admin.site.register(PartnerServiceContentLabel,PartnerServiceContentLabelAdmin)
admin.site.register(PartnerAicategoryLabel,PartnerAicategoryLabelAdmin)
admin.site.register(PartnerCostLabel,PartnerCostLabelAdmin)
admin.site.register(CaseStudy,CaseStudyAdmin)
admin.site.register(ProductInfo,ProductInfoAdmin)
