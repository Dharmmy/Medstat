from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from morbidity.models  import MorbidityData
from django.http import HttpResponseRedirect
# Include the `fusioncharts.py` file that contains functions to embed the charts.

from .fusioncharts import FusionCharts

def Chart(request):
  if request.user.is_superuser:
# Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

  # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Chart representation of Gender in Morbidity "
    chartConfig["subCaption"] = ""
    chartConfig["xAxisName"] = "Gender"
    chartConfig["yAxisName"] = "Number of cases"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

  # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
  # Insert the data into the `dataSource['data']` list.

    hope = MorbidityData.objects.filter(Sex='male').count()        
    data = {}
    data['label'] = 'male'
    data['value'] = hope
    dataSource['data'].append(data)
        
    hope = MorbidityData.objects.filter(Sex='female').count()  
        
    data = {}
    data['label'] = 'female'
    data['value'] = hope
    dataSource['data'].append(data)

    numberOfCases = MorbidityData.objects.all().count()

  # Create an object for the column 2D chart using the FusionCharts class constructor
  # The chart data is passed to the `dataSource` parameter.
    column3D = FusionCharts("column3D", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
    pie3D = FusionCharts("pie3D", "myFirstChart2", "600", "400", "myFirstchart-container2", "json", dataSource)
  
    return render(request, 'morbiditychart/dashboard.html', {
      'output': column3D.render(),
      'output2':pie3D.render(),
      'cases' : numberOfCases
  })





def diseaseChart(request):
  if request.user.is_superuser:
  
    if request.method == 'POST':
      diseaseNam = request.POST["diseaseTitle"]
    else:
      diseaseNam = ''
    

  # Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = ""
    chartConfig["subCaption"] = ""
    chartConfig["xAxisName"] = "Gender"
    chartConfig["yAxisName"] = "Number of cases"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.

    hope = MorbidityData.objects.filter(Disease=diseaseNam)
    hope2 = hope.filter(Sex='male').count()        
    data = {}
    data['label'] = 'male'
    data['value'] = hope2
    dataSource['data'].append(data)
          
      
    femaleFilter = MorbidityData.objects.filter(Sex='female')
    femaleFilter2 = femaleFilter.filter(Disease=diseaseNam).count() 
          
    data = {}
    data['label'] = 'female'
    data['value'] = femaleFilter2
    dataSource['data'].append(data)

    numberOfCases= MorbidityData.objects.filter(Disease=diseaseNam).count

    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    
    pie3D = FusionCharts("doughnut3D", "pieChart", "600", "400", "myFirstchart", "json", dataSource)
    column3D = FusionCharts("column3D", "pieChart1", "600", "400", "myFirstchart1", "json", dataSource)  
    return render(request, 'morbiditychart/disease Statistics.html', {
        'output1':pie3D.render(),
        'output2':column3D.render(),
        'diseaseName': diseaseNam,
        'cases': numberOfCases     
      })






