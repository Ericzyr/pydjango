function attackEnemy() {
    document.write("land on");
    alert("ready go");
}
function Ms938jump(){
 window.location.href="/Ms938reportupload"
}

function Ms938remp(){
	window.location.href="/ms938report"
}

function Ms648jump(){
 window.location.href="/Ms648reportupload"
}

function Ms648remp(){
	window.location.href="/ms648report"
}

function record938(){
	window.location.href="/reportrecord938"
}

function record(){
	window.location.href="/reportrecord"
}

function displayDate(){
	document.getElementById("demo").innerHTML=Date();
}

function sufuntion() {
    window.alert("删除");
    // var x;
    // var r=confirm("按下按钮");
    // if (r==true)
    // {
		// x="你按下了\"ok\"按钮!";
    // }
    // else
    // {
		// x="你按下了\"cancel\"按钮!";
    // }
    // document.getElementById("demo").innerHTML=x;
}



   var chart = Highcharts.chart('container', {
		title: {
				text: '2014 某网站各浏览器浏览量占比'
		},
		tooltip: {
				headerFormat: '{series.name}<br>',
				pointFormat: '{point.name}: <b>{point.percentage:.1f}%</b>'
		},
		plotOptions: {
				pie: {
						allowPointSelect: true,  // 可以被选择
						cursor: 'pointer',       // 鼠标样式
						dataLabels: {
								enabled: true,
								format: '<b>{point.name}</b>: {point.percentage:.1f} %',
								style: {
										color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
								}
						}
				}
		},
		series: [{
				type: 'pie',
				name: '浏览器访问量占比',
				data: [
						['Firefox',   45.0],
						['IE',       26.8],
						{
								name: 'Chrome',
								y: 12.8,
								sliced: true,  // 默认突出
								selected: true // 默认选中
						},
						['Safari',    8.5],
						['Opera',     6.2],
						['其他',   0.7]
				]
		}]
});


