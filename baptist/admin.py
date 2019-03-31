from django.contrib import admin
from baptist.models import *
#from baptist.custom_model_admin import CustomModelAdmin


# Register your models here.

"""
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Church
    extra = 2
"""

class ChurchAdmin(admin.ModelAdmin):
    list_display = ('chu_name','chu_postcode','chu_email','chu_isActive','chu_EQZoneFK','chu_isTrust')
    search_fields = ('chu_name',)
    #radio_fields = {'chu_EQZoneFK':admin.HORIZONTAL}
    #eqzone_filter = Rate.objects()
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'chu_EQZoneFK':
            kwargs["queryset"] = Rate.objects.filter(rat_code__startswith=RATE_CODE_STARTSWITH_EQZONE).filter(rat_canOverride=0).filter(rat_text__regex=r'.+')
        return super(ChurchAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
    fieldsets = (
        ('Church',{'fields':('chu_name','chu_account','chu_worshippers','chu_isActive','chu_isTrust','chu_EQZoneFK','chu_phone','chu_email')}),
        ('Address',{'fields':('chu_address1','chu_address2','chu_suburb','chu_city','chu_postcode')}),
    )
         
class RateAdmin(admin.ModelAdmin):
    #inlines = [ChoiceInline]
    
    list_display = ('rat_code','rat_polFK','rat_text','rat_amount','rat_factor','rat_canOverride')
    list_filter = ('rat_text','rat_amount','rat_canOverride')
    search_fields = ('rat_code','rat_text')
    #readonly_fields = ('rat_code',)
    fieldsets = (
        ('Rate Code',{'fields':('rat_code',)}),
        ('Update Rate',{'fields':('rat_polFK','rat_text','rat_amount','rat_factor','rat_canOverride')})
    )
    
class EQZoneAdmin(admin.ModelAdmin):
    list_display = ('eqzone','eqzone_number','eqzone_rate')
    
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('pol_typeID','pol_chuFK')
    list_filter = ('pol_typeID','pol_chuFK')
    search_fields = ('pol_chuFK__chu_name',)
    #readonly_fields = ('pol_COPAmt','pol_CEQAmt','pol_EQCAmt','pol_FSLAmt','pol_FEEAmt','pol_NETAmt','pol_GSTAmt','pol_GRSAmt')
    fieldsets = (
        ('Insurance Policy',{'fields':('pol_typeID','pol_chuFK','pol_isRateOverride')}),
        (None,{'fields':('pol_conditions',)}),
        ('Amount',{'fields':('pol_COPAmt','pol_CEQAmt','pol_EQCAmt','pol_FSLAmt','pol_FEEAmt','pol_NETAmt','pol_GSTAmt','pol_GRSAmt')}),
    )
    
admin.site.register(Church, ChurchAdmin)
admin.site.register(Policy, PolicyAdmin)

admin.site.register(Rate, RateAdmin)
admin.site.register(PolicyDetails_BIN)
admin.site.register(EQZone,EQZoneAdmin)
admin.site.register(PolicyDetails_LIA)