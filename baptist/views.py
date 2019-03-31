from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from baptist import utils

import os

DEFAULT_RETROACTIVE_DATE = "1900-01-01"

import time
#from django.contrib.auth import authenticate

from baptist.models import *
# Create your views here.


def index(request):
    #return HttpResponse('Hello Martin')
    return render(request, 'home.html', {'user':'MartinA'})

@login_required
def report(request):
    #latest_rate_list = Rate.objects.all()
    template = loader.get_template("report_base.html")
    #context = RequestContext(request,{
    #    'latest_rate_list': latest_rate_list,
    #})
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def reports_generate(request):
    response = HttpResponse(mimetype='text/plain')
    filepath = os.pathsep.join([".", 'reports'])
    filename = "test"
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename
    response.write()
    return response

@login_required
def protal(request):
    template = loader.get_template("portal.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

@login_required
def setting(request):    
    #all_rates = 
    is_adm = utils.is_admin(request.user)
    rates_bincomcop = Rate.objects.filter(rat_code=RATE_CODE_BINCOMCOP).filter(rat_canOverride=1)
    rates_binind = Rate.objects.filter(rat_code__startswith=RATE_CODE_STARTSWITH_BININD).filter(rat_canOverride=0).filter(rat_amount__isnull=False)
    rates_eqzone = Rate.objects.filter(rat_code__startswith=RATE_CODE_STARTSWITH_EQZONE).filter(rat_canOverride=0).filter(rat_text__regex=r'.+')
    rate_goodsvc = Rate.objects.filter(rat_code=RATE_CODE_GOODS_SERVICES_TAX)
    rate_liaTruClA = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIATRUCL+"A")[0]
    rate_liaTruClB = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIATRUCL+"B")[0]
    rate_liaTruClC = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIATRUCL+"C")[0]
    rate_liaTruClD = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIATRUCL+"D")[0]
    rate_liaTruClE = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIATRUCL+"E")[0]
    rate_liaTruClF = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIATRUCL+"F")[0]
    rate_liaTruClG = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIATRUCL+"G")[0]
    
    rate_liaChuClA = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIACHUCL+"A")[0]
    rate_liaChuClB = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIACHUCL+"B")[0]
    rate_liaChuClC = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIACHUCL+"C")[0]
    rate_liaChuClD = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIACHUCL+"D")[0]
    rate_liaChuClE = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIACHUCL+"E")[0]
    rate_liaChuClF = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIACHUCL+"F")[0]
    rate_liaChuClG = Rate.objects.filter(rat_code=RATE_CODE_STARTSWITH_LIACHUCL+"G")[0]
    
    rate_schLiaMin = Rate.objects.filter(rat_code=RATE_CODE_SCHEME_LIA_MINI)[0]
    rate_schLiaTot = Rate.objects.filter(rat_code=RATE_CODE_SCHEME_LIA_TOTAL)[0]
    rate_schWorThr = Rate.objects.filter(rat_code=RATE_CODE_WORSHP_THRESHHOLD)[0]
    
    rate_mvFulCop = Rate.objects.filter(rat_code=RATE_CODE_MV_FULL_COP)[0]
    rate_mv3pCop = Rate.objects.filter(rat_code=RATE_CODE_MV_THIRDPARTY_COP)[0]
    rate_mv3pFtCop = Rate.objects.filter(rat_code=RATE_CODE_MV_THIRDPARTY_FT_COP)[0]
    rate_mvFSL = Rate.objects.filter(rat_code=RATE_CODE_MV_FIRE_SERVICE_LEVEL)[0]
    rate_mdComCop = Rate.objects.filter(rat_code=RATE_CODE_MD_COM_COP)[0]
    rate_mdComInf = Rate.objects.filter(rat_code=RATE_CODE_MD_COM_INFLATION)[0]
    rate_mdComEQI = Rate.objects.filter(rat_code=RATE_CODE_MD_COM_EQ_INFLATION)[0]
    rate_mdComFSL = Rate.objects.filter(rat_code=RATE_CODE_MD_COM_FIRE_SERVICE_LEVEL)[0]
    rate_mdResCop = Rate.objects.filter(rat_code=RATE_CODE_MD_RES_COP)[0]
    rate_mdResEQC = Rate.objects.filter(rat_code=RATE_CODE_MD_RES_EQC)[0]
    rate_mdResEQT = Rate.objects.filter(rat_code=RATE_CODE_MD_RES_EQ_TOPUP)[0]
    rate_mdResFSL = Rate.objects.filter(rat_code=RATE_CODE_MD_RES_FIRE_SERVICE_LEVEL)[0]
    
    def rate_money_format(rate):
        rate.money_format = utils.money_format(rate.rat_amount)
        
    for rate in [rate_liaTruClA,rate_liaTruClB,rate_liaTruClC,rate_liaTruClD,rate_liaTruClE,rate_liaTruClF,rate_liaTruClG,
                 rate_liaChuClA,rate_liaChuClB,rate_liaChuClC,rate_liaChuClD,rate_liaChuClE,rate_liaChuClF,rate_liaChuClG,
                 rate_schLiaMin,rate_schLiaTot,rate_schWorThr,rate_mvFSL,rate_mdComFSL]:
        rate_money_format(rate)
    
    t = loader.get_template("settings.html")
    context = RequestContext(request,{
        'rates_bincomcop' : rates_bincomcop,
        'rates_binind' : rates_binind,
        'rates_eqzone' : rates_eqzone,
        'rate_goodsvc' : rate_goodsvc,
        'rate_liaTruClA' : rate_liaTruClA,
        'rate_liaTruClB' : rate_liaTruClB,
        'rate_liaTruClC' : rate_liaTruClC,
        'rate_liaTruClD' : rate_liaTruClD,
        'rate_liaTruClE' : rate_liaTruClE,
        'rate_liaTruClF' : rate_liaTruClF,
        'rate_liaTruClG' : rate_liaTruClG,
        'rate_liaChuClA': rate_liaChuClA,
        'rate_liaChuClB': rate_liaChuClB,
        'rate_liaChuClC': rate_liaChuClC,
        'rate_liaChuClD': rate_liaChuClD,
        'rate_liaChuClE': rate_liaChuClE,
        'rate_liaChuClF': rate_liaChuClF,
        'rate_liaChuClG': rate_liaChuClG,
        'rate_schLiaMin' : rate_schLiaMin,
        'rate_schLiaTot': rate_schLiaTot,
        'rate_schWorThr': rate_schWorThr,
        'rate_mvFulCop': rate_mvFulCop,
        'rate_mv3pCop': rate_mv3pCop,
        'rate_mv3pFtCop': rate_mv3pFtCop,
        'rate_mvFSL': rate_mvFSL,
        'rate_mdComCop': rate_mdComCop,
        'rate_mdComInf': rate_mdComInf,
        'rate_mdComEQI': rate_mdComEQI,
        'rate_mdComFSL': rate_mdComFSL,
        'rate_mdResCop': rate_mdResCop,
        'rate_mdResEQC': rate_mdResEQC,
        'rate_mdResEQT': rate_mdResEQT,
        'rate_mdResFSL': rate_mdResFSL,
        'is_adm' : is_adm,
        
    })
    return HttpResponse(t.render(context))


def create_default_PolicyDetails_BIN(policy):
    policydetails_bin = PolicyDetails_BIN()
    policydetails_bin.pdb_polFK = policy
    policydetails_bin.pdb_incomeLossSI = 0
    policydetails_bin.pdb_payrollSI = 0
    policydetails_bin.pdb_increaseCostSI = 0
    policydetails_bin.pdb_claimPrepSI = 0
    policydetails_bin.pdb_TotalSI = 0
    default_indemnityPeriod_rate = Rate.objects.filter(rat_code__startswith=RATE_CODE_STARTSWITH_BININD).filter(rat_canOverride=1)[0]
    policydetails_bin.pdb_indemnityPeriod = default_indemnityPeriod_rate
    policydetails_bin.pdb_isEQExcluded = 0
    policydetails_bin.save()
    
def create_default_PolicyDetails_LIA(policy, is_trust):
    print "********", is_trust
    #default_date_str = time.strftime("%Y-%m-%d")
    default_date_str = DEFAULT_RETROACTIVE_DATE
    policydetails_lia = PolicyDetails_LIA()
    policydetails_lia.pdl_polFK = policy
    if is_trust:
        # Should be a Trust
        policydetails_lia.pdl_CLAIncluded = 1
        policydetails_lia.pdl_CLBIncluded = 1
        policydetails_lia.pdl_CLCIncluded = 1
        policydetails_lia.pdl_CLDIncluded = 1
        policydetails_lia.pdl_CLEIncluded = 1
        policydetails_lia.pdl_CLFIncluded = 1
        policydetails_lia.pdl_CLGIncluded = 1
        policydetails_lia.pdl_medicalExtensionIncluded = 1
        policydetails_lia.pdl_professionalIndemnityExcluded = 1
    else :
        # Should be a Church
        policydetails_lia.pdl_CLAIncluded = 1
        policydetails_lia.pdl_CLBIncluded = 1
        policydetails_lia.pdl_CLCIncluded = 1
        policydetails_lia.pdl_CLDIncluded = 1
        policydetails_lia.pdl_CLEIncluded = 1
        policydetails_lia.pdl_CLFIncluded = 0
        policydetails_lia.pdl_CLGIncluded = 0
        policydetails_lia.pdl_medicalExtensionIncluded = 0
        policydetails_lia.pdl_professionalIndemnityExcluded = 0
    policydetails_lia.pdl_CLARetroDate = default_date_str
    policydetails_lia.pdl_CLBRetroDate = default_date_str
    policydetails_lia.pdl_CLCRetroDate = default_date_str
    policydetails_lia.pdl_CLDRetroDate = default_date_str
    policydetails_lia.pdl_CLERetroDate = default_date_str
    policydetails_lia.pdl_CLFRetroDate = default_date_str
    policydetails_lia.pdl_CLGRetroDate = default_date_str
    policydetails_lia.pdl_CLALimit = 0
    policydetails_lia.pdl_CLBLimit = 0
    policydetails_lia.pdl_CLCLimit = 0
    policydetails_lia.pdl_CLDLimit = 0
    policydetails_lia.pdl_CLELimit = 0
    policydetails_lia.pdl_CLFLimit = 0
    policydetails_lia.pdl_CLGLimit = 0
    try:
        policydetails_lia.save()
    except Exception,e:
        print e

def _output_retroactive_date(given_date):
    if str(given_date) == DEFAULT_RETROACTIVE_DATE:
        return ""
    return given_date

@login_required
def policies_check(request):
    class PolicyType(object):
        def __init__(self, type_id, type_name):
            self.type_id = type_id
            self.type_name = type_name
    
    # policy types
    policytypes = []
    for item in Policy.POLICY_TYPES:
        policytypes.append(PolicyType(item[0],item[1]))

    # churchs
    churchs = Church.objects.all()
    
    #rates_binind (Months)
    rates_binind = Rate.objects.filter(rat_code__startswith=RATE_CODE_STARTSWITH_BININD).filter(rat_canOverride=0).filter(rat_amount__isnull=False)
    
    t = loader.get_template("policy_base.html")
    context = RequestContext(request,{
        'policytypes' : policytypes,
        'churchs' : churchs,
        'rates_binind' : rates_binind,
    })
    return HttpResponse(t.render(context)) 

def _isChurchOrTrust(is_trust): 
    if is_trust:
        return "Trust"
    else:
        return "Church"

def _get_default_bincomcop():
    return Rate.objects.filter(rat_code=RATE_CODE_BINCOMCOP).filter(rat_canOverride=1)[0].rat_factor
    
def find_policy_by_church(request):

    #polTypeName,churchName = "Undefined","Undefined"
    result = "Empty"
    policy = None
    
    items_map = {}
    for key, value in request.GET.items():
        items_map[key] = value
 
    churchID = items_map['churchID']
    polTypeID = items_map['polTypeID']
            
    # get policy name & church name from DB
    #for item in Policy.POLICY_TYPES:
    #    if str(item[0]) == polTypeID:
    #        polTypeName = item[1]
    churchset = Church.objects.filter(chu_pk=churchID)
    if churchset:
        church = churchset[0]
   
    #churchName = church.chu_name
    policyset = Policy.objects.filter(pol_typeID=polTypeID).filter(pol_chuFK=church)

    if policyset:
        policy = policyset[0]
        rate_factor_bincomcop,rate_factor_eq = None, None
        
        if not policy.pol_isRateOverride: # is not override, DEFAULT VALUE
            print "is NOT Override"
            rate_factor_bincomcop = _get_default_bincomcop()
            rate_factor_eq = church.chu_EQZoneFK.rat_factor
        else:
            print "is Override"
            try:
                rate_bincomcop_set = Rate.objects.filter(rat_code=RATE_CODE_BINCOMCOP).filter(rat_polFK=policy.pol_pk)
                rate_eq_set = Rate.objects.filter(rat_code__startswith=RATE_CODE_STARTSWITH_EQZONE).filter(rat_polFK=policy.pol_pk)
                if not rate_bincomcop_set:
                    print "------------------"
                    new_rate_bincomcop = Rate(rat_code=RATE_CODE_BINCOMCOP,rat_polFK=policy.pol_pk,rat_text="",rat_factor=_get_default_bincomcop(),rat_canOverride=0)
                    new_rate_bincomcop.save()
                    rate_bincomcop_set = Rate.objects.filter(rat_code=RATE_CODE_BINCOMCOP).filter(rat_polFK=policy.pol_pk)
                    if not rate_bincomcop_set:
                        print "Error!! will be logging this - new_rate_bincomcop_save"
                if not rate_eq_set:
                    print "++++++++++++++++++++++"
                    _default_eqz_rat = Rate.objects.filter(rat_code__startswith=RATE_CODE_STARTSWITH_EQZONE).filter(rat_canOverride=1)[0]
                    new_rate_eq = Rate(rat_code=_default_eqz_rat.rat_code,rat_polFK=policy.pol_pk,rat_text="",rat_factor=_default_eqz_rat.rat_factor,rat_canOverride=0)
                    new_rate_eq.save()
                    rate_eq_set = Rate.objects.filter(rat_code__startswith=RATE_CODE_STARTSWITH_EQZONE).filter(rat_polFK=policy.pol_pk)
                    if not rate_eq_set:
                        print "Error!! will be logging this - new_rate_eq_save"
            except Exception,e:
                print e
            rate_factor_bincomcop = rate_bincomcop_set[0].rat_factor
            rate_factor_eq = rate_eq_set[0].rat_factor
        json_content = """
            "pol_isRateOverride":"%s",
            "rate_factor_bincomcop":"%s",
            "rate_factor_eq":"%s",
            "pol_conditions":"%s",
            "pol_COPAmt":"%s",
            "pol_CEQAmt":"%s",
            "pol_EQCAmt":"%s",
            "pol_FSLAmt":"%s",
            "pol_FEEAmt":"%s",
            "pol_NETAmt":"%s",
            "pol_GSTAmt":"%s",
            "pol_GRSAmt":"%s" """ %(  policy.pol_isRateOverride,
                        rate_factor_bincomcop,
                        rate_factor_eq,
                        policy.pol_conditions,
                        utils.money_format(policy.pol_COPAmt),
                        utils.money_format(policy.pol_CEQAmt),
                        utils.money_format(policy.pol_EQCAmt),
                        utils.money_format(policy.pol_FSLAmt),
                        utils.money_format(policy.pol_FEEAmt),
                        utils.money_format(policy.pol_NETAmt),
                        utils.money_format(policy.pol_GSTAmt),
                        utils.money_format(policy.pol_GRSAmt),
                        )
        
        # Only for Business Interruption Policy  ( Pocily ID 1)
        if polTypeID == "1":
            polDetailBINSet = PolicyDetails_BIN.objects.filter(pdb_polFK=policy)         
            # Check Policy Details BIN
            if not polDetailBINSet:
                print "-------------- No policy details BIN"
                create_default_PolicyDetails_BIN(policy)
                polDetailBINSet = PolicyDetails_BIN.objects.filter(pdb_polFK=policy)
            if polDetailBINSet:
                print "++++++++++++++ Everything is good"
                polDetailBIN = polDetailBINSet[0]
                json_content += """,
                    "pdb_incomeLossSI": "%s",
                    "pdb_payrollSI": "%s",
                    "pdb_increaseCostSI": "%s",
                    "pdb_claimPrepSI": "%s",
                    "pdb_indemnityPeriod":"%d",
                    "pdb_isEQExcluded":"%s" """ % (
                            utils.money_format(polDetailBIN.pdb_incomeLossSI),
                            utils.money_format(polDetailBIN.pdb_payrollSI),
                            utils.money_format(polDetailBIN.pdb_increaseCostSI),
                            utils.money_format(polDetailBIN.pdb_claimPrepSI),
                            polDetailBIN.pdb_indemnityPeriod.rat_pk,
                            polDetailBIN.pdb_isEQExcluded,
                     )
                result = '{"retcode":"1",%s}' % json_content
                #print result
                 
        # Only for Liability Policy ( Pocily ID 2)
        if polTypeID == "2":
            polDetailLIASet = PolicyDetails_LIA.objects.filter(pdl_polFK=policy)
            # Check Policy Details LIA
            if not polDetailLIASet:
                print "---------------- No policy details LIA"
                create_default_PolicyDetails_LIA(policy,church.chu_isTrust)
                polDetailLIASet = PolicyDetails_LIA.objects.filter(pdl_polFK=policy)
            if polDetailLIASet:
                print "++++++++++++++ Everything is good"
                polDetailLIA = polDetailLIASet[0]
                json_content += """,
                    "ChurchOrTrust": "%s",
                    "pdl_CLAIncluded": "%s",
                    "pdl_CLARetroDate": "%s",
                    "pdl_CLALimit": "%s",
                    "pdl_CLBIncluded": "%s",
                    "pdl_CLBRetroDate": "%s",
                    "pdl_CLBLimit": "%s",
                    "pdl_CLCIncluded": "%s",
                    "pdl_CLCRetroDate": "%s",
                    "pdl_CLCLimit": "%s",
                    "pdl_CLDIncluded": "%s",
                    "pdl_CLDRetroDate": "%s",
                    "pdl_CLDLimit": "%s",
                    "pdl_CLEIncluded": "%s",
                    "pdl_CLERetroDate": "%s",
                    "pdl_CLELimit": "%s",
                    "pdl_CLFIncluded": "%s",
                    "pdl_CLFRetroDate": "%s",
                    "pdl_CLFLimit": "%s",
                    "pdl_CLGIncluded": "%s",
                    "pdl_CLGRetroDate": "%s",
                    "pdl_CLGLimit": "%s",
                    "pdl_medicalExtensionIncluded": "%s",
                    "pdl_professionalIndemnityExcluded":"%s" """ % (
                            _isChurchOrTrust(church.chu_isTrust),
                            polDetailLIA.pdl_CLAIncluded,
                            _output_retroactive_date(polDetailLIA.pdl_CLARetroDate),
                            utils.money_format(polDetailLIA.pdl_CLALimit),
                            polDetailLIA.pdl_CLBIncluded,
                            _output_retroactive_date(polDetailLIA.pdl_CLBRetroDate),
                            utils.money_format(polDetailLIA.pdl_CLBLimit),
                            polDetailLIA.pdl_CLCIncluded,
                            _output_retroactive_date(polDetailLIA.pdl_CLCRetroDate),
                            utils.money_format(polDetailLIA.pdl_CLCLimit),
                            polDetailLIA.pdl_CLDIncluded,
                            _output_retroactive_date(polDetailLIA.pdl_CLDRetroDate),
                            utils.money_format(polDetailLIA.pdl_CLDLimit),
                            polDetailLIA.pdl_CLEIncluded,
                            _output_retroactive_date(polDetailLIA.pdl_CLERetroDate),
                            utils.money_format(polDetailLIA.pdl_CLELimit),
                            polDetailLIA.pdl_CLFIncluded,
                            _output_retroactive_date(polDetailLIA.pdl_CLFRetroDate),
                            utils.money_format(polDetailLIA.pdl_CLFLimit),
                            polDetailLIA.pdl_CLGIncluded,
                            _output_retroactive_date(polDetailLIA.pdl_CLGRetroDate),
                            utils.money_format(polDetailLIA.pdl_CLGLimit),
                            polDetailLIA.pdl_medicalExtensionIncluded,
                            polDetailLIA.pdl_professionalIndemnityExcluded,
                     )
            result = '{"retcode":"2",%s}' % json_content
        
        return HttpResponse(result)
    else:
        result = """{"retcode":"-1","message":"No policy found!"}"""
        return HttpResponse(result)
    return HttpResponse("Error Happened")

def add_policy_by_policyIdNchurch(request,polTypeID,churchID):
    policy = Policy(pol_typeID=polTypeID,pol_chuFK=Church.objects.get(chu_pk=churchID),pol_isRateOverride=0,pol_conditions="")
    policy.pol_COPAmt = 0
    policy.pol_CEQAmt = 0
    policy.pol_EQCAmt = 0
    policy.pol_FSLAmt = 0
    policy.pol_FEEAmt = 0
    policy.pol_NETAmt = 0
    policy.pol_GSTAmt = 0
    policy.pol_GRSAmt = 0
    policy.save()

    if polTypeID == "1":  # Business Interruption Policy  ( Pocily ID 1)
        #print "----------------------------"
        create_default_PolicyDetails_BIN(policy)
        
    if polTypeID == "2":
        create_default_PolicyDetails_LIA(policy,Church.objects.filter(chu_pk=churchID)[0].chu_isTrust)
    return HttpResponse("add_policy_success")

def updateSetting(request):
    change_table,change_pk,change_field,change_value='','','',''
    items = request.GET.items()
    print '++++++++++++',items
    for key, value in items:
        if key == "change_table":
            change_table = value
        elif key == "change_pk":
            change_pk = int(value)
        elif key == "change_field":
            change_field = value
        elif key == "change_value":
            change_value = value
    if change_table == 'rate':
        rate = Rate.objects.get(rat_pk=change_pk)
        if change_field == 'rat_text':
            rate.rat_text = change_value
        elif change_field == 'rat_factor':
            rate.rat_factor = utils.str_to_decimal(change_value,RATE_FACTOR_PLACES)
        elif change_field == 'rat_amount':  
            rate.rat_amount = utils.str_to_decimal(change_value,RATE_AMOUNT_PLACES)
    rate.save()
    return HttpResponse("ok")