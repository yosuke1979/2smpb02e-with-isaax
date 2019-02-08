Highcharts.chart('chart', {
    chart: {
      type: 'area',
      animation: Highcharts.svg,
      marginRight: 10,
      events: {
        load: function() {
          const request = window.superagent;
                series = this.series[0];
  
          setInterval(function () {
            request
              .get('/sensor')
              .end(function(err, res){
                let x = (new Date()).getTime(),
                    py = res.body.pressure,
                    ty = res.body.temperature;
                
                if (py < series.yAxis.oldMin | !series.yAxis.oldMin) {
                    series.yAxis.update({min: py});
                }
                series.addPoint([x, py], true, true);
              });
          }, 10000);
        } 
      }
    },
    title: {
      text: 'Pressure'
    },
    xAxis: {
      type: 'datetime'
    },
    yAxis: {
      title: {
        text: 'hPa' 
      }
    },
    series: [{
      name: 'Pressure',
      data: (function () {
        let data = [],
            time = (new Date()).getTime(),
            i;
  
        for (i=-99; i<=0; i+=1) {
          data.push({
            x: time + i * 1000,
            y: undefined
          });
        }
        return data;
      }())
    }]
  });
  
