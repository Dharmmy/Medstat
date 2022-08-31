  const check = document.getElementById("check");
   const chartdisplay = document.getElementById("chartdisplay");

  function displayCheck() {

    if ((chartdisplay.style.display = "none") && (document.getElementById("diseaseinput").value !==null)) {
        check.addEventListener("click", function(){
         document.getElementById("chartdisplay").style.display = "block";
        return;})
        }
    else {
                alert ("please input disease title")
                    return;
            };
          return displayCheck();
  }
    
