$(function(){
var width = 10240,
    height = 1024,
    svg = d3.select("#chart")
        .attr("style", "padding-bottom: " + Math.ceil(height * 100 / width) + "%")
        .append("svg")
        .attr("viewBox", "0 0 " + width + " " + height);

var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().rangeRound([height, 0]);

    d3.csv('./results.csv',function (data) {
        
        var timeParse = d3.timeParse('%Y-%m-%d');
        x.domain([timeParse('2018-01-26'), new Date()]);
        y.domain([0, 100000]);

        var drawAxis = function(yValueCallback, color) {
            svg.append('path')
                .datum(data)
                .attr("fill", "none")
                .attr("stroke", color)
                .attr("stroke-linejoin", "round")
                .attr("stroke-linecap", "round")
                .attr("stroke-width", 5)
                .attr("d", d3.line().x(function(d) { return x(timeParse(d.timestamp.split(' ')[0]
)); }).y(yValueCallback));
        };
        drawAxis(function(d) { return y(d.count); }, "blue");
    });
    
    // d3.csv('./results.csv',function (data) {
    // })
});