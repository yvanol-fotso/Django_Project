
var form= document.getElementById('#profileType');

function displayRightForm(){

    if (form.value == 'student') {
    	document.getElementById('#employeeForm').style.visibility='hidden';
    	document.getElementById('#studentForm').style.visibility='visible';
    }else{
    	document.getElementById('#employeeForm').style.visibility='visible';
    	document.getElementById('#studentForm').style.visibility='hidden';
    }

} 

