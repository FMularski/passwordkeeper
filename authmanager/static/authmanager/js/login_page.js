const openFormBtn = document.querySelector('#open-form-btn');
const darkPanel = document.querySelector('#dark-panel');
const registerPanel = document.querySelector('#register-panel');
const closeForm = document.querySelector('i');

openFormBtn.addEventListener('click', function() {
    darkPanel.classList.add('active');
    registerPanel.classList.add('active');
});

closeForm.addEventListener('click', function() {
    darkPanel.classList.remove('active');
    registerPanel.classList.remove('active');

    const inputs = document.querySelectorAll('input');
    inputs.forEach( input => {
        input.value = "";
    })
})