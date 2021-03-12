const openFormBtn = document.querySelector('#open-form-btn');
const darkPanel = document.querySelector('#dark-panel');
const registerPanel = document.querySelector('#register-panel');
const closeForm = document.querySelector('#register-close');
const closeErrors = document.querySelector('#errors-close');


openFormBtn.addEventListener('click', function() {
    darkPanel.classList.add('active');
    registerPanel.classList.add('active');
});

closeForm.addEventListener('click', function() {
    darkPanel.classList.remove('active');
    registerPanel.classList.remove('active');

   document.querySelector('#id_username').value = '';
   document.querySelector('#id_email').value = '';
})

closeErrors.addEventListener('click', function(){
    const errors = this.parentNode;
    errors.style.animation = 'swoosh 0.3s ease-out';
    errors.addEventListener('animationend', function(){
        errors.remove()
    })
})