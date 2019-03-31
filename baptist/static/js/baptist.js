$(function(){
 	$(".nav-sidebar li").click(function(){
		$(".nav-sidebar li").removeClass("active");
		$(this).addClass("active");
	});
	
	var fade_fast = 500;
	var fade_slow = 1500;

	$("#div_bindetail").hide();
	$("#div_specialcondition").hide();
	$("#div_binrateoverride").hide();
	$("#div_totalpremium").hide();
	$("#select_policytype").change(function(){
 		if ($(this).val() == 1){
			$("#div_bindetail").fadeIn(fade_slow);
		} else {
			$("#div_bindetail").fadeOut(fade_fast);
		};
	});
	//$(".collapsable").attr('src','/static/pic/downarrow.png');
	//$(".collapse_dev").css("background-image","url(/static/pic/downarrow.png) no-repeat 0 0");
	
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
	
	function hide_all_policy(){
		$("#div_bindetail").fadeOut(fade_fast);;
		$("#div_specialcondition").fadeOut(fade_fast);
		$("#div_totalpremium").fadeOut(fade_fast);
	}
	$("#select_church").change(function(){
		var polTypeID = $("#select_policytype").val();
		var churchID = $(this).val();
		var actionStr = "findPolicyByChurch";

		$("#decision").html("Loading ...");
 		$.ajax({
			type: 'GET',
			url: actionStr,
			data: {'churchID': churchID, 'polTypeID':polTypeID }, 
			success: function(data){;
				var obj = JSON.parse(data);
				var retcode = obj.retcode;
				if (retcode == "1"){
					$("#pdb_incomeLossSI").val(obj.pdb_incomeLossSI)
					$("#pdb_payrollSI").val(obj.pdb_payrollSI)
					$("#pdb_increaseCostSI").val(obj.pdb_increaseCostSI)
					$("#pdb_claimPrepSI").val(obj.pdb_claimPrepSI)
					$("#pdb_indemnityPeriod").val(obj.pdb_indemnityPeriod)
					if (obj.pdb_isEQExcluded == "True"){
						$("#pdb_isEQExcluded").attr("checked", true);
					} else {
						$("#pdb_isEQExcluded").attr("checked", false);
					}
					$("#div_bindetail").fadeIn(fade_slow);
					show_common_policy(obj)
					$("#decision").html("")
				} else {
					$("#decision").html(obj.message);
					hide_all_policy();
				};
			},
			dataType:"text"
		});
	});
	
	//$(".collapsable").click(function(){
	//	if($(this).attr('src') =='/static/pic/uparrow.png'){
	//		$(this).attr('src','/static/pic/downarrow.png');
	//	} else if($(this).attr('src') =='/static/pic/downarrow.png'){
	//		$(this).attr('src','/static/pic/uparrow.png');
	//	}
	//	$(this).parent().next("div").slideToggle("slow");
	//});
	
	$("fieldset > legend").click(function(){
		img_obj = $(this).find('img');
		if(img_obj.attr('src') =='/static/pic/uparrow.png'){
			img_obj.attr('src','/static/pic/downarrow.png');
		} else if(img_obj.attr('src') =='/static/pic/downarrow.png'){
			img_obj.attr('src','/static/pic/uparrow.png');
		}
		$(this).next("div").slideToggle("slow");
	});
	
	$("#BINCOMCOP").click(function(){
		alert(111);
		//old_val = $(this).html();
		//$(this).html("<input type='text' value='" + old_val +' />")
	});
})

