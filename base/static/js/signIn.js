$('#slideup').click(function(){
    $('#forgot').slideUp(500);

})
$('#slidedown').click(function(){
    $('#forgot').slideDown(500);

})

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const forgot = document.getElementById('forgot');
const container = document.getElementById('container');

forgot.addEventListener('click', () => {
    container.classList.add("left-panel-active");
});

signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});
