
// recuperation du jeton via le js et le passer a l'objet request de js
// let csrfTokenValue = document.querySelector('[name=csrffmiddlewartoken]').value;




document.querySelector("#ajax-call").addEventListener("click",event=>{
	event.preventDefault();

	let formData = new FormData();
	formData.append('a',document.querySelector("#a").value);
	formData.append('b',document.querySelector("#b").value);

	// on recupere la valeur du jeton  CSRF
   let csrfTokenValue = document.querySelector('[name=csrffmiddlewartoken]').value;

   const request = new Request('{% url "compute" %}' ,{
   	method:POST,
   	boddy:formData,
   	headers:{'X-CSRFToken':csrfTokenValue} //on ajoute le token dans l'entete

   });

   //on execute la requete 

   fetch(request)
        .then(response =>response.json())
        .then(result =>{
        	const resultElement = document.querySelector("#ajax1");
        	resultElement.innerHTML =result["operation_result"];
        })




})