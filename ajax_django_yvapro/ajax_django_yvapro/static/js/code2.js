
document.querySelector("#ajax-call").addEventListener("click",event=>{
	event.preventDefault();

  
    	// var a = document.querySelector("#a").value;
    	// var b = document.querySelector("#b").value;

    	let formData = new FormData();
	      formData.append('a',document.querySelector("#a").value);
	      formData.append('b',document.querySelector("#b").value);

     
       var xhr = new XMLHttpRequest(); 

       var url = 'compute/';

       xhr.onreadystatechange = function(){ 

         if(xhr.readyState == 4 && xhr.status == 200){ 
         	// alert(xhr.response); //pour voir si la requete fonctionne normalement
       
            // alert(JSON.stringify(response));
            // var dataRcv = JSON.stringify(xhr.response);

            const resultElement = document.querySelector("#ajax2");
        	// resultElement.innerHTML =result["operation_result"] 
        	// resultElement.innerHTML = dataRcv
        	resultElement.innerHTML = xhr.response;

          } 
       } 

       xhr.open('POST', url, true); 

       xhr.send(formData);

    
 });
