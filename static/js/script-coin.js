
 function drawChart(){
    const container = document.querySelector('#chart');
    let new_1 = document.getElementById('p-read').innerText.replace("[[", "[");
    let new_2 = new_1.replace("]]", "]");
    let new_data = new_2.split("],");

    list_datas = [['Datas', 'Dollar']]
    for (let i=0; i < new_data.length; i++){
        let new_data2 = new_data[i].replace("]", "").replace("[", "").split(", ");
        console.log(new_data2)
        list_datas.push([new_data2[0].replace("'", "").replace(" ", "").replace("'", ""), parseFloat(new_data2[1])]);
    }

    console.log('------')
    console.log(list_datas)
    const data = new google.visualization.arrayToDataTable(list_datas)

    const options = {
      title: 'Ultimos 5 Dias',
      Height: 1200,
      width: 1000
    }
    const chart = new google.visualization.LineChart(container)
    chart.draw(data, options)
  }