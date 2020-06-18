var modal1 = document.getElementById('newcustomer');
window.onclick = function(event) {
    if (event.target == modal1) {
        modal.style.display = "none";
    }
}
var modal2 = document.getElementById('updatecustomer');

window.onclick = function(event) {
    if (event.target == modal2) {
        modal.style.display = "none";
    }
}


function servicesbut(){ 
    var val ='{{vala}}';
    console.log(val)
    if(val){
    alert("plz update the account id")
    document.getElementById('abccusservice').style.display='none'
    	}
    else {
    document.getElementById('abccusservice').style.display='block'
    }
    }


function viewbut(){ 
    var val ='{{vala}}';
    console.log(val)
    if(val){
    alert("plz update the account id")
    document.getElementById('view').style.display='none'
    	}
    else {
    document.getElementById('view').style.display='block'
    }
    }






function CS(){ 
    var val ='{{vals}}';
    console.log(val)
    if(val){
    alert("plz click on the status details")
    document.getElementById('customerstatus').style.display='none'
    	}
    else {
    document.getElementById('customerstatus').style.display='block'
    }
    }
    
  function AS(){ 
    var val ='{{vals}}';
    console.log(val)
    if(val){
    alert("plz click on the status details")
    document.getElementById('accountstatus').style.display='none'
    	}
    else {
    document.getElementById('accountstatus').style.display='block'
    }
    }




function updatecus(){ 
    var val ='{{val}}';
    console.log(val)
    if(val){
    alert("plz update the customer id")
    document.getElementById('updatecustomer').style.display='none'
    	}
    else {
    document.getElementById('updatecustomer').style.display='block'
    }
    }
function deletecus(){ 
    var val ='{{val}}';
    console.log(val)
    if(val){
    alert("plz update the customer id")
    document.getElementById('deletecustomer').style.display='none'
    	}
    else {
    document.getElementById('deletecustomer').style.display='block'
    }

}
var modal3 = document.getElementById('deletecustomer');

window.onclick = function(event) {
    if (event.target == modal3) {
        modal.style.display = "none";
    }
}
        
    
  


var modal4 = document.getElementById('addaccount');

window.onclick = function(event) {
    if (event.target == modal4) {
        modal.style.display = "none";
    }
}


var modal5 = document.getElementById('deleteaccount');

window.onclick = function(event) {
    if (event.target == modal5) {
        modal.style.display = "none";
    }
}



var modal6 = document.getElementById('searchcustomer');

window.onclick = function(event) {
    if (event.target == modal6) {
        modal.style.display = "none";
    }
}


var modal7 = document.getElementById('accountstatus');

window.onclick = function(event) {
    if (event.target == modal7) {
        modal.style.display = "none";
    }
}

var modal8 = document.getElementById('customerstatus');

window.onclick = function(event) {
    if (event.target == modal8) {
        modal.style.display = "none";
    }
}

var modal9 = document.getElementById('searchaccount');

window.onclick = function(event) {
    if (event.target == modal9) {
        modal.style.display = "none";
    }
}

var modal10 = document.getElementById('depositmoney');

window.onclick = function(event) {
    if (event.target == modal10) {
        modal.style.display = "none";
    }
}

var modal11 = document.getElementById('withdrawmoney');

window.onclick = function(event) {
    if (event.target == modal11) {
        modal.style.display = "none";
    }
}

var modal12 = document.getElementById('transfermoney');

window.onclick = function(event) {
    if (event.target == modal12) {
        modal.style.display = "none";
    }
}
var modal13 = document.getElementById('accountstatement');

window.onclick = function(event) {
    if (event.target == modal13) {
        modal.style.display = "none";
    }
}
var modal13 = document.getElementById('abccusservice');

window.onclick = function(event) {
    if (event.target == modal13) {
        modal.style.display = "none";
    }
}
var modal13 = document.getElementById('view');
window.onclick = function(event) {
    if (event.target == modal13) {
        modal.style.display = "none";
    }
}



