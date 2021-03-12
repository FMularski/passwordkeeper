const openFormBtn = document.querySelector('#open-form-btn');
const darkPanel = document.querySelector('#dark-panel');
const registerPanel = document.querySelector('#register-panel');
const closeForm = document.querySelector('#register-close');
const popupCloses = document.querySelectorAll('.popup-close');


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


popupCloses.forEach( close => {
    close.addEventListener('click', function(){
        const popup = this.parentNode;
        popup.style.animation = 'swoosh 0.3s ease-out';
        popup.addEventListener('animationend', function(){
            popup.remove()
        })
    })
})

// closeErrors.addEventListener('click', function(){
//     const errors = this.parentNode;
//     errors.style.animation = 'swoosh 0.3s ease-out';
//     errors.addEventListener('animationend', function(){
//         errors.remove()
//     })
// })