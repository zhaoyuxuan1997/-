$(document).ready(function(){
	console.log("333333");
	//var json = {'popular_result': {'_id': '2017-12-01T00:00:00.000Zmonthly', 'articleAidList': ['4909', '4184', '8392', '5442', '8652']}, 'articleAidList_all': [{'texts': ['text_a4909.txt link:http://202.112.51.43:9871/download/text_a4909.txt'], 'images': ['image_a4909_0.jpg link:http://202.112.51.43:9871/download/image_a4909_0.jpg', 'image_a4909_1.jpg link:http://202.112.51.43:9871/download/image_a4909_1.jpg', ''], 'videos': [''], 'title': 'title4909'}, {'texts': ['text_a4184.txt link:http://202.112.51.43:9871/download/text_a4184.txt'], 'images': ['image_a4184_0.jpg link:http://202.112.51.43:9871/download/image_a4184_0.jpg', 'image_a4184_1.jpg link:http://202.112.51.43:9871/download/image_a4184_1.jpg', 'image_a4184_2.jpg link:http://202.112.51.43:9871/download/image_a4184_2.jpg', 'image_a4184_3.jpg link:http://202.112.51.43:9871/download/image_a4184_3.jpg', 'image_a4184_4.jpg link:http://202.112.51.43:9871/download/image_a4184_4.jpg', ''], 'videos': [''], 'title': 'title4184'}, {'texts': ['text_a8392.txt link:http://202.112.51.43:9871/download/text_a8392.txt'], 'images': ['image_a8392_0.jpg link:http://202.112.51.43:9871/download/image_a8392_0.jpg', 'image_a8392_1.jpg link:http://202.112.51.43:9871/download/image_a8392_1.jpg', 'image_a8392_2.jpg link:http://202.112.51.43:9871/download/image_a8392_2.jpg', ''], 'videos': [''], 'title': 'title8392'}, {'texts': ['text_a5442.txt link:http://202.112.51.43:9871/download/text_a5442.txt'], 'images': ['image_a5442_0.jpg link:http://202.112.51.43:9871/download/image_a5442_0.jpg', 'image_a5442_1.jpg link:http://202.112.51.43:9871/download/image_a5442_1.jpg', ''], 'videos': [''], 'title': 'title5442'}, {'texts': ['text_a8652.txt link:http://202.112.51.43:9871/download/text_a8652.txt'], 'images': ['image_a8652_0.jpg link:http://202.112.51.43:9871/download/image_a8652_0.jpg', ''], 'videos': [''], 'title': 'title8652'}]};
	//console.log(json.articleAidList_all);
	
	$.ajax({
          type: 'GET',
          url:'http://202.112.51.43:9872/search_popular?time=2017-12-01&temporalGranularity=monthly',
          dataType:'json',
		  async: false,
          success: function(json) {
            // JSON.stringify(data);
			console.log("111111");
            console.log(json); 
            var data = json.articleAidList_all;
			var str = "";
			for(var i=0;i<data.length;i++){
				str += "<tr>";
				str += "<td>"+data[i].title+"</td>";
				str += "<td>";
				if(data[i].images.length!=0){
					for(var n=0;n<data[i].images.length;n++){
						if(data[i].images[n]!=''){
							var im = data[i].images[n].split(' ');
							var l = im[1].substring(5);
							str += "<a href=\""+l+"\">"+im[0]+"</a><br>";
						}
					}
				}
				str += "</td>";
				str += "<td>";
				if(data[i].texts.length!=0){
					for(var n=0;n<data[i].texts.length;n++){
						if(data[i].texts[n]!=''){
							var im = data[i].texts[n].split(' ');
							var l = im[1].substring(5);
							str += "<a href=\""+l+"\">"+im[0]+"</a><br>";
						}
					}
				}
				str += "</td>";
				str += "<td>";
				if(data[i].videos.length!=0){
					for(var n=0;n<data[i].videos.length;n++){
						if(data[i].videos[n]!=''){
							var im = data[i].videos[n].split(' ');
							var l = im[1].substring(5);
							str += "<a href=\""+l+"\">"+im[0]+"</a><br>";
						}
					}
				}
				str += "</td>";
				str += "</tr>";
			}
			$("#favourite").html(str);
          },
          error: function(error) {
            console.log(error);
          }
    });
});

function changeButton(value)
    {
        $("#dropdownMenuButton").text(value);
		console.log($("#dropdownMenuButton").text());
    }

function serach()
    {
        $.ajax({
          type: 'GET',
          url:'http://202.112.51.43:9872/search_popular?time='+$("#searchData").val()+'&temporalGranularity='+$("#dropdownMenuButton").text(),
          dataType:'json',
		  async: false,
          success: function(json) {
			if ($('#dataTable').html() != "") {
				$('#dataTable').dataTable().fnDestroy();
			}
            // JSON.stringify(data);
			var data = json.articleAidList_all;
			//var str = "<div class=\"card-body\" ><div class=\"table-responsive\"> <table class=\"table table-bordered\" id=\"dataTable\" width=\"100%\" cellspacing=\"0\"><thead><tr> <th>title</th> <th>images</th><th>texts</th><th>videos</th></tr></thead> <tfoot><tr><th>title</th> <th>images</th><th>texts</th><th>videos</th> </tr></tfoot><tbody id = \"userBook\">";
			var str = "";
			result = new Array(data.length);
			for(var i=0;i<data.length;i++){
				array = new Array(4);
				array[0] = data[i].title;
				str += "<tr>";
				str += "<td>"+data[i].title+"</td>";
				str += "<td>";
				if(data[i].images.length!=0){
					for(var n=0;n<data[i].images.length;n++){
						if(data[i].images[n]!=''){
							console.log("000000000")
							var im = data[i].images[n].split(' ');
							var l = im[1].substring(5);
							str += "<a href=\""+l+"\">"+im[0]+"</a><br>";
							if(n==0){
								array[1] = "<a href=\""+l+"\">"+im[0]+"</a><br>";
							}else{
								array[1] += "<a href=\""+l+"\">"+im[0]+"</a><br>";
							}
						}else{
							if(n==0){
								array[1] = "";
							}else{
								array[1] += "";
							}
						}
					}
				}
				str += "</td>";
				str += "<td>";
				if(data[i].texts.length!=0){
					for(var n=0;n<data[i].texts.length;n++){
						if(data[i].texts[n]!=''){
							var im = data[i].texts[n].split(' ');
							var l = im[1].substring(5);
							str += "<a href=\""+l+"\">"+im[0]+"</a><br>";
							if(n==0){
								array[2] = "<a href=\""+l+"\">"+im[0]+"</a><br>";
							}else{
								array[2] += "<a href=\""+l+"\">"+im[0]+"</a><br>";
							}
						}else{
							if(n==0){
								array[2] = "";
							}else{
								array[2] += "";
							}
						}
					}
				}
				str += "</td>";
				str += "<td>";
				if(data[i].videos.length!=0){
					for(var n=0;n<data[i].videos.length;n++){
						if(data[i].videos[n]!=''){
							var im = data[i].videos[n].split(' ');
							var l = im[1].substring(5);
							str += "<a href=\""+l+"\">"+im[0]+"</a><br>";
							if(n==0){
								array[3] = "<a href=\""+l+"\">"+im[0]+"</a><br>";
							}else{
								array[3] += "<a href=\""+l+"\">"+im[0]+"</a><br>";
							}
						}else{
							if(n==0){
								array[3] = "";
							}else{
								array[3] += "";
							}
						}
					}
				}
				str += "</td>";
				str += "</tr>";
				console.log(array);
				result[i] = array;
			}
			//str +="</tbody></table></div></div>";
			//$("#userBook").html(str);
			console.log(result);
			$('.table').dataTable().fnClearTable();   //将数据清除
            $('.table').dataTable().fnAddData(result);  //重新绑定table数据
          },
          error: function(error) {
            console.log(error);
          }
    });
    }