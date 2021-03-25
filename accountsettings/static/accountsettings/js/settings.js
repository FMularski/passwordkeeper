$(document).ready(function(){
    const darkPanel = document.querySelector('#dark-panel');
    
    const changePasswordPanel = document.querySelector('#change-password-form-panel');
    const changePasswordBtn = document.querySelector('#change-password-btn');
    
    const changePinPanel = document.querySelector('#change-pin-form-panel');
    const changePinBtn = document.querySelector('#change-pin-btn');
    
    const closeButtons = document.querySelectorAll('i');
    
    changePasswordBtn.addEventListener('click', function(){
        darkPanel.classList.add('active');
        changePasswordPanel.classList.add('active');
    })

    changePinBtn.addEventListener('click', function(){
        darkPanel.classList.add('active');
        changePinPanel.classList.add('active');
    })

    closeButtons.forEach(btn => {
        btn.addEventListener('click', function(){
            darkPanel.classList.remove('active');
            changePasswordPanel.classList.remove('active');
            changePinPanel.classList.remove('active');
        })
    })
})