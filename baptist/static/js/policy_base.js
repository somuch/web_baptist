$(function(){

 	$(".nav-sidebar li").click(function(){
		$(".nav-sidebar li").removeClass("active");
		$(this).addClass("active");
	});
	
	var fade_fast = 500;
	var fade_slow = 1500;
	var findPolicyByChurch = "findPolicyByChurch";
	
	function show_common_policy(obj){
		$("#div_specialcondition").fadeIn(fade_slow);
		$("#textarea_specialcondition").html(obj.pol_conditions);
		$("#div_totalpremium").fadeIn(fade_slow);
		$("#pol_COPAmt").val(obj.pol_COPAmt);
		$("#pol_CEQAmt").val(obj.pol_CEQAmt);
		$("#pol_EQCAmt").val(obj.pol_EQCAmt);
		$("#pol_FSLAmt").val(obj.pol_FSLAmt);
		$("#pol_FEEAmt").val(obj.pol_FEEAmt);
		$("#pol_NETAmt").val(obj.pol_NETAmt);
		$("#pol_GSTAmt").val(obj.pol_GSTAmt);
		$("#pol_GRSAmt").val(obj.pol_GRSAmt);
	}

	var first_openPage = true;
	
	function hide_all_policy(){
		if (first_openPage){
			$("#div_bindetail").hide();
			$("#div_liadetail").hide();
			$("#div_specialcondition").hide();
			$("#div_binrateoverride").hide();
			$("#div_totalpremium").hide();
			first_openPage = false;
		} else {
			$("#div_bindetail").fadeOut(fade_fast);
			$("#div_liadetail").fadeOut(fade_fast);
			$("#div_specialcondition").fadeOut(fade_fast);
			$("#div_binrateoverride").fadeOut(fade_fast);
			$("#div_totalpremium").fadeOut(fade_fast);	
		}

	}
	
	function activate_bin_override(){
		$("#bin_override_cpr").prop("readonly", false);
		$("#bin_override_eqr").prop("readonly", false);
	}
	
	function inactivate_bin_override(){
		$("#bin_override_cpr").prop("readonly", true);
		$("#bin_override_eqr").prop("readonly", true);

	}
	
	function set_checkbox(bool_val,checkbox_id){
		if (bool_val == "True"){
			$("#"+checkbox_id).prop("checked", true);
		} else {
			$("#"+checkbox_id).prop("checked", false);
		}
	}
	
	function show_existing_policy_bin(obj){
		$("#pdb_incomeLossSI").val(obj.pdb_incomeLossSI)
		$("#pdb_payrollSI").val(obj.pdb_payrollSI)
		$("#pdb_increaseCostSI").val(obj.pdb_increaseCostSI)
		$("#pdb_claimPrepSI").val(obj.pdb_claimPrepSI)
		$("#pdb_indemnityPeriod").val(obj.pdb_indemnityPeriod)
		set_checkbox(obj.pdb_isEQExcluded,"pdb_isEQExcluded")
		
		if (obj.pol_isRateOverride == "True"){
			$("#pol_isRateOverride").prop("checked", true);
			//alert($("#pol_isRateOverride").checked);
			activate_bin_override();
		} else {
			$("#pol_isRateOverride").prop("checked", false);
			inactivate_bin_override();
		};
		$("#bin_override_cpr").val(obj.rate_factor_bincomcop);
		$("#bin_override_eqr").val(obj.rate_factor_eq);		
		$("#div_bindetail").fadeIn(fade_slow);
		$("#div_binrateoverride").fadeIn(fade_slow);
		show_common_policy(obj);
		$("#decision").html("");
	}
	
	function reset_claA_subcheckbox(){
		if ($("#claA_override").prop("checked")){
			$("#tr_medicalExtensionIncluded").fadeIn();
			$("#tr_professionalIndemnityExcluded").fadeIn();
		} else {
			$("#tr_medicalExtensionIncluded").fadeOut();
			$("#tr_professionalIndemnityExcluded").fadeOut();
		}
	}
	
	function show_existing_policy_lia(obj){
		$("#lia_title").text(obj.ChurchOrTrust + $("#lia_title").text())
		$("#div_liadetail").fadeIn(fade_slow);
		set_checkbox(obj.pdl_CLAIncluded,"claA_override");
		set_checkbox(obj.pdl_CLBIncluded,"claB_override");
		set_checkbox(obj.pdl_CLCIncluded,"claC_override");
		set_checkbox(obj.pdl_CLDIncluded,"claD_override");
		set_checkbox(obj.pdl_CLEIncluded,"claE_override");
		set_checkbox(obj.pdl_CLFIncluded,"claF_override");
		set_checkbox(obj.pdl_CLGIncluded,"claG_override");
		set_checkbox(obj.pdl_medicalExtensionIncluded,"checkbox_medicalExtensionIncluded");
		set_checkbox(obj.pdl_professionalIndemnityExcluded,"checkbox_professionalIndemnityExcluded");
		$("#claA_date").val(obj.pdl_CLARetroDate);
		$("#claB_date").val(obj.pdl_CLBRetroDate);
		$("#claC_date").val(obj.pdl_CLCRetroDate);
		$("#claD_date").val(obj.pdl_CLDRetroDate);
		$("#claE_date").val(obj.pdl_CLERetroDate);
		$("#claF_date").val(obj.pdl_CLFRetroDate);
		$("#claG_date").val(obj.pdl_CLGRetroDate);
		$("#claA_limit").val(obj.pdl_CLALimit);
		$("#claB_limit").val(obj.pdl_CLBLimit);
		$("#claC_limit").val(obj.pdl_CLCLimit);
		$("#claD_limit").val(obj.pdl_CLDLimit);
		$("#claE_limit").val(obj.pdl_CLELimit);
		$("#claF_limit").val(obj.pdl_CLFLimit);
		$("#claG_limit").val(obj.pdl_CLGLimit);
		reset_claA_subcheckbox();
		show_common_policy(obj);
		$("#decision").html("");
	}
	
	function show_existing_policy_mv(obj){
	
	}
	
	function show_existing_policy_md(obj){
	
	}
	
	function show_corresponding_policy(obj){
		retcode = obj.retcode;
		if (retcode == "1"){
			show_existing_policy_bin(obj)
		} else if (retcode == "2"){
			show_existing_policy_lia(obj)
		} else if (retcode == "3"){
		    show_existing_policy_mv(obj)
		} else if (retcode == "4"){
		    show_existing_policy_md(obj)
		};
	}
	
	hide_all_policy();
	
	function no_policy_how2do(polTypeID,churchID){
		display = "<strong>[" + $("#select_policytype option:selected").text() +"] policy does not exist for [" + $("#select_church option:selected").text()+"]<br>Would you like to <a id='addDefaultPolicy'><font color='green'><u>Create One</u></a></font> right now?</strong>"
		$("#decision").html(display);
		hide_all_policy();
		$("#addDefaultPolicy").click(function(){
			$("#decision").html("");
			$.ajax({
				type: 'GET',
				url: 'addPolicy/'+ polTypeID+'/'+churchID+'/',
				data: {}, 
				success: function(data){
					if (data == "add_policy_success"){	
						$.ajax({
							type: 'GET',
							url: findPolicyByChurch,
							data: {'churchID': churchID, 'polTypeID':polTypeID }, 
							success: function(data){
								var new_obj = JSON.parse(data);
								show_corresponding_policy(new_obj)
							},
							dataType:"text"
						});
					};
				},
				dataType:"text"
			});
		});
						
	}
	
	var go_policyNchurch = function(){
		hide_all_policy();	
		if ( $("#select_policytype").val() != "999" && $("#select_church").val() != "999" ) {
			var polTypeID = $("#select_policytype").val();
			var churchID = $("#select_church").val();
			$("#decision").html("Loading ...");
 			$.ajax({
				type: 'GET',
				url: findPolicyByChurch,
				data: {'churchID': churchID, 'polTypeID':polTypeID }, 
				success: function(data){
					//alert(data);
					var obj = JSON.parse(data);
					if (obj.retcode == "-1"){
						no_policy_how2do(polTypeID,churchID)		
					} else {
						show_corresponding_policy(obj)
					};
				},
				dataType:"text"
			});
		};
	};
	
	
	$("#pol_isRateOverride").change(function(){
		//alert(this.checked);
		if (this.checked){
			activate_bin_override();
		} else {
			inactivate_bin_override();
		}
	});
	
	$("#claA_override").change(function(){
		reset_claA_subcheckbox();
	});
	
	$("#select_policytype").change(go_policyNchurch);
	$("#select_church").change(go_policyNchurch);
	
	$("fieldset > legend").click(function(){
		img_obj = $(this).find('img');
		if(img_obj.attr('src') =='/static/pic/uparrow.png'){
			img_obj.attr('src','/static/pic/downarrow.png');
		} else if(img_obj.attr('src') =='/static/pic/downarrow.png'){
			img_obj.attr('src','/static/pic/uparrow.png');
		}
		$(this).next("div").slideToggle("slow");
	});
	
})

