from django.db import models

# Create your models here.
RATE_FACTOR_DIGITS = 9
RATE_FACTOR_PLACES = 8
RATE_AMOUNT_DIGITS = 10
RATE_AMOUNT_PLACES = 2
POLICY_FEE_DIGITS = 10
POLICY_FEE_DECIMAL_PLACES = 2
EQZONE_RATE_FACTOR_DIGITS = 6
EQZONE_RATE_FACTOR_PLACES = 5

RATE_CODE_BINCOMCOP = "BINCOMCOP"
RATE_CODE_STARTSWITH_EQZONE = "CEQZON"
RATE_CODE_STARTSWITH_BININD = "BININD"
RATE_CODE_STARTSWITH_LIATRUCL = "LIATRUCL"
RATE_CODE_STARTSWITH_LIACHUCL = "LIACHUCL"
RATE_CODE_GOODS_SERVICES_TAX= "SCHGST"
RATE_CODE_SCHEME_LIA_MINI = "SCHLIAMIN"
RATE_CODE_SCHEME_LIA_TOTAL = "SCHLIATOT"
RATE_CODE_WORSHP_THRESHHOLD = "SCHWORTHR"
RATE_CODE_MV_FULL_COP = "MVLFULCOP"
RATE_CODE_MV_THIRDPARTY_COP = "MVLTPTCOP"
RATE_CODE_MV_THIRDPARTY_FT_COP = "MVLTPFCOP"
RATE_CODE_MV_FIRE_SERVICE_LEVEL = "MVLFSL"
RATE_CODE_MD_COM_COP = "MDACOMCOP"
RATE_CODE_MD_COM_INFLATION = "MDACOMINF"
RATE_CODE_MD_COM_EQ_INFLATION = "MDACOMEQI"
RATE_CODE_MD_COM_FIRE_SERVICE_LEVEL = "MDACOMFSL"
RATE_CODE_MD_RES_COP = "MDARESCOP"
RATE_CODE_MD_RES_EQC = "MDARESEQC"
RATE_CODE_MD_RES_EQ_TOPUP ="MDARESEQT"
RATE_CODE_MD_RES_FIRE_SERVICE_LEVEL = "MDARESFSL"

class EQZone(models.Model):
    eqzone = models.CharField(max_length=255, verbose_name="Earchquake Zone")
    eqzone_number = models.IntegerField(unique=True)
    eqzone_rate = models.DecimalField(max_digits=EQZONE_RATE_FACTOR_DIGITS, decimal_places=EQZONE_RATE_FACTOR_PLACES)
    
    def __unicode__(self):
        return self.eqzone

class Rate_EQZone(models.Model):
    rat_code = models.CharField(max_length=12, unique=True, default="", verbose_name="Rates Code ID" )
    eqzone_name = models.CharField(max_length=255, verbose_name="Earchquake Zone")
    eqzone_rate = models.DecimalField(max_digits=EQZONE_RATE_FACTOR_DIGITS, decimal_places=EQZONE_RATE_FACTOR_PLACES)
    def __unicode__(self):
        return self.eqzone

class Rate(models.Model):
    rat_pk = models.AutoField(max_length=11, primary_key=True, verbose_name="Primary Key")
    rat_code = models.CharField(max_length=12, default="", verbose_name="Rate Code")
    rat_polFK = models.IntegerField(null=True, verbose_name="Policy")
    rat_text = models.CharField(blank=True, max_length=255, verbose_name="Text")
    rat_amount = models.DecimalField(null=True, blank=True, default=None, max_digits=RATE_AMOUNT_DIGITS, decimal_places=RATE_AMOUNT_PLACES, verbose_name="Amount")
    rat_factor = models.DecimalField(null=True, blank=True, max_digits=RATE_FACTOR_DIGITS, decimal_places=RATE_FACTOR_PLACES,
                            verbose_name="Factor")
    rat_canOverride = models.BooleanField(default=False, verbose_name="can override?")

    def __unicode__(self):
        if self.rat_code.startswith(RATE_CODE_STARTSWITH_EQZONE) and self.rat_text:
            return self.rat_text
            #return "%s - %s" % (self.rat_code, self.rat_text)
        elif self.rat_code.startswith(RATE_CODE_STARTSWITH_BININD) and self.rat_amount:
            return "%s - %d Months" %(self.rat_code, self.rat_amount)
        elif self.rat_factor:
            return "%s" % (self.rat_code)
        else:
            return self.rat_code


class Church(models.Model):
    chu_pk = models.AutoField(max_length=11, primary_key=True)
    chu_name = models.CharField(max_length=99, default="", unique=True, verbose_name="Church Name")
    chu_account = models.CharField(max_length=11, unique=True, verbose_name="Account No.")
    chu_worshippers = models.PositiveSmallIntegerField(verbose_name="Worshippers")
    chu_isActive = models.BooleanField(default=True, verbose_name="Is Active?")
    chu_isTrust = models.BooleanField(default=False, verbose_name="Is Trust")
    chu_EQZoneFK = models.ForeignKey(Rate, verbose_name="EQ Zone")
    chu_phone = models.CharField(max_length=12, default="", verbose_name="Phone")
    chu_email = models.EmailField(verbose_name="Email")

    chu_address1 = models.CharField(max_length=255, default="", verbose_name="Address") 
    chu_address2 = models.CharField(max_length=255, default="", verbose_name="")
    chu_suburb = models.CharField(max_length=255, default="", verbose_name="Suburb")
    chu_city = models.CharField(max_length=255, default="", verbose_name="City")
    chu_postcode = models.CharField(max_length=4, default="", verbose_name="Postcode")

    def __unicode__(self):
        return self.chu_name
    

class Policy(models.Model):
    POLICY_TYPES = (
        (1, 'Business Interruption'),
        (2, 'Liability'),
        (3, 'Motor Vehicle'),
        (4, 'Material Damage'),
    )
    pol_pk = models.AutoField(primary_key=True, verbose_name="Primary Key")
    pol_chuFK = models.ForeignKey(Church, verbose_name="Belong to Church")
    pol_typeID = models.SmallIntegerField(choices=POLICY_TYPES, verbose_name="Policy Type")
    pol_isRateOverride = models.BooleanField(default=False, verbose_name="Rate Override?")
    pol_conditions = models.TextField(max_length=255, default="", verbose_name="Conditions")
    pol_COPAmt = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                     default=0, verbose_name="COP Amount", help_text="Total Policy Company Premium Amount" )
    pol_CEQAmt = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                     default=0, verbose_name="CEQ Amount", help_text="Total Policy Earthquake Premium Amount" )
    pol_EQCAmt = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                     default=0, verbose_name="EQC Amount", help_text="Total Policy Earthquake Commission Amount" )
    pol_FSLAmt = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                     default=0, verbose_name="FSL Amount", help_text="Total Policy Fire Services Levy Amount" )
    pol_FEEAmt = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                     default=0, verbose_name="FEE Amount", help_text="Total Policy Fee Amount" )
    pol_NETAmt = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                     default=0, verbose_name="NET Amount", help_text="Total Policy Net Amount = COP+CEQ+EQC+FSL" )
    pol_GSTAmt = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                     default=0, verbose_name="GST Amount", help_text="Total Policy Goods and Services Tax Amount" )
    pol_GRSAmt = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                     default=0, verbose_name="GRS Amount", help_text="Total Policy Gross Amount = Net+GST" )

    def __unicode__(self):
        pol_type = "No Policy_Type for Policy_ID[%d]" % self.pol_typeID
        for each_type in self.POLICY_TYPES:
            if each_type[0] == self.pol_typeID:
                pol_type = each_type[1]
        return "<%s> for <%s>" %(pol_type, self.pol_chuFK )

    
class PolicyDetails_BIN(models.Model):
    pdb_pk = models.AutoField(primary_key=True, verbose_name="Primary Key")
    pdb_polFK = models.ForeignKey(Policy, verbose_name="Policy")
    pdb_incomeLossSI = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                        default=0, verbose_name="Income Loss SI", help_text="Loss of Income/Rents sum insured amount")
    pdb_payrollSI = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                        default=0, verbose_name="Payroll SI", help_text="Payroll sum insured amount")
    pdb_increaseCostSI = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                        default=0, verbose_name="Increased Cost SI", help_text="Increased cost of working sum insured amount")
    pdb_claimPrepSI = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                        default=0, verbose_name="Claim Preparation SI", help_text="Claims preparation sum insured amount")
    pdb_TotalSI = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, 
                                        default=0, verbose_name="Total SI", 
                                        help_text="Total Sum Insured for Risk record = Pdb_IncomeLossSI + Pdb_PayrollSI + Pdb_IncreasedCostSI + Pdb_ClaimPrepSI")
    pdb_indemnityPeriod = models.ForeignKey(Rate, default=0, verbose_name="Indemnity Period", 
                                        help_text="Foreign Key to Rates table - specifies which BININD# this policy relates to")
    pdb_isEQExcluded = models.BooleanField(default=False, verbose_name="EQ Excluded?", 
                                        help_text="Is Earthquake Cover excluded for this policy?")
    
    def __unicode__(self):
        return str(self.pdb_pk)

    
class PolicyDetails_LIA(models.Model):
    pdl_pk = models.AutoField(primary_key=True, verbose_name='Primary Key')
    pdl_polFK = models.ForeignKey(Policy, verbose_name="Policy",
                                  help_text="Foreign Key to Policy table - specifies which Policy this detail belongs to")
    pdl_CLAIncluded = models.BooleanField(default=False, verbose_name="Clause A Included?")
    pdl_CLARetroDate = models.DateField(verbose_name="Clause A Retroactive Date")
    pdl_CLALimit = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, verbose_name="Clause A Limit")
    pdl_CLBIncluded = models.BooleanField(default=False, verbose_name="Clause B Included?")
    pdl_CLBRetroDate = models.DateField(verbose_name="Clause B Retroactive Date")
    pdl_CLBLimit = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, verbose_name="Clause B Limit")
    pdl_CLCIncluded = models.BooleanField(default=False, verbose_name="Clause C Included?")
    pdl_CLCRetroDate = models.DateField(verbose_name="Clause C Retroactive Date")
    pdl_CLCLimit = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, verbose_name="Clause C Limit")
    pdl_CLDIncluded = models.BooleanField(default=False, verbose_name="Clause D Included?")
    pdl_CLDRetroDate = models.DateField(verbose_name="Clause D Retroactive Date")
    pdl_CLDLimit = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, verbose_name="Clause D Limit")
    pdl_CLEIncluded = models.BooleanField(default=False, verbose_name="Clause E Included?")
    pdl_CLERetroDate = models.DateField(verbose_name="Clause E Retroactive Date")
    pdl_CLELimit = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, verbose_name="Clause E Limit")
    pdl_CLFIncluded = models.BooleanField(default=False, verbose_name="Clause F Included?")
    pdl_CLFRetroDate = models.DateField(verbose_name="Clause F Retroactive Date")
    pdl_CLFLimit = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, verbose_name="Clause F Limit")
    pdl_CLGIncluded = models.BooleanField(default=False, verbose_name="Clause G Included?")
    pdl_CLGRetroDate = models.DateField(verbose_name="Clause G Retroactive Date")
    pdl_CLGLimit = models.DecimalField(max_digits=POLICY_FEE_DIGITS, decimal_places=POLICY_FEE_DECIMAL_PLACES, verbose_name="Clause G Limit")
    pdl_medicalExtensionIncluded = models.BooleanField(default=False, verbose_name="Is Medical Malpractice Vicarious Liability Extension Included?")
    pdl_professionalIndemnityExcluded = models.BooleanField(default=False, verbose_name="Is Professional Indemnity Excluded?")