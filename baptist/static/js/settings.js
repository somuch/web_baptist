$(function(){

	var change_list = new Array();
	
	function click2edit(){
		dom_id = $(this).attr('id');
		old_val = $(this).html();
		var is_money = false;
		if (old_val.indexOf("$") == 0){
			is_money = true;
		}
		$(this).empty();
		var input = $("<input>");
		input.css("text-align","center")  
		input.attr("value", old_val); 
		input.blur(function(event) {
			var spanNode = input.parent();
			var new_val = input.val();
			if(is_money){
				if (new_val.indexOf('$') != 0){
					new_val = "$" + new_val;
				}
			}
			spanNode.html(new_val);
			if (old_val != new_val){
				change_list[change_list.length] = dom_id;
				spanNode.addClass("highlight_text");
			} 
			spanNode.click(click2edit);
		});
		
		$(this).append(input);
		var inputdom = input.get(0);
		inputdom.select();
		$(this).unbind('click');
	};

	if ($("#is_adm").html() == "True"){
		$('[name="click2edit"]').click(click2edit);
		
	};
	
	function save_data(){
		var change_table = '';
		var change_pk = '';
		var change_field = '';
		var change_value = '';
		//alert("1.table:"+change_table +"--pk:"+change_pk+"--field:"+change_field+"--value:"+change_value );
		for (var i=0;i<change_list.length;i++){
			domId = change_list[i];
			var theNode = $('#'+domId); 
			change_pk = theNode.attr('value').trim();
			change_value = theNode.text().trim();
			if(domId.indexOf("rate") == 0){
				change_table = 'rate';
				if (domId=='rate_bincompremium'||domId.indexOf('rate_discount')==0||domId.indexOf('rate_eqzonerate')==0||domId=='rate_goodsvc'||domId.indexOf('rate_factor')==0){
					change_field = 'rat_factor';		
				}else if (domId.indexOf('rate_eqzonename')==0){
					change_field = 'rat_text';
				}else if (domId.indexOf('rate_month')==0 ||domId.indexOf('rate_clause')==0||domId.indexOf('rate_money')==0){
					change_field = 'rat_amount';
				} 
			}
			
			if (change_list[i].indexOf("somethingelse") == 0){
				actionURL = 'somethingelse';
			}
			//alert("new.table("+change_table +")-pk:"+change_pk+"--field("+change_field+")-value:("+change_value );
			$.ajax({
				type: 'GET',
				async: false,
				url: 'updateSetting',
				data: {'change_table':change_table,'change_pk':change_pk, 'change_field':change_field,'change_value':change_value}, 
				success: function(returnData){},
				dataType:"text"
			});
		};
	
	};
	
	$("#save").click(function(){
		if(change_list.length > 0){
			var cfm =  confirm("Sure to save the changes?");
			if(cfm){
				save_data();
				location.reload();
			}
		} else {
			alert("No changes at all!");
		}
        
    });
	$("#cancel").click(function(){
        location.reload();
    });
	
})