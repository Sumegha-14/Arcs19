document.getElementById('add').onclick = function()
{
    var places = document.getElementById('item').value;
    var content,ele,t,t1,t2;
    $.ajax({
        url: "https://api.apixu.com/v1/current.json?key=11217702a77b43b6a89215302192703&q="+places,
        type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
            content = res.location.name;
            console.log(res);
            console.log(res.location.country);
            ele= document.createElement('li');
            t = document.createTextNode(res.current.temp_c+ '°C\n ,');
            t1 = document.createTextNode(res.current.condition.text + '\n ->');
            t2 = document.createTextNode('\n' + res.location.name + '\n');
            ele.appendChild(t);
            ele.appendChild(t1);
            ele.appendChild(t2);

            document.getElementById("addto").appendChild(ele);
    
        }
     
    }); 
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker
                 .register('/service-worker.js')
                 .then(function() { console.log('Service Worker Registered'); });
      }
       //document.getElementById("addto").insertBefore(ele,document.getElementById("addto").childNodes[0]);
}