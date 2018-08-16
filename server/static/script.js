var tableData = document.querySelectorAll("td");

tableData.forEach(function(element){
    element.addEventListener("mouseover", function(){
        element.style.color = "#20C20E";
    })

    element.addEventListener("mouseout", function(){
        element.style.color = "white";
    })

})