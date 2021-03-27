const popupCloses = document.querySelectorAll('.popup-close');

popupCloses.forEach( close => {
    close.addEventListener('click', function(){
        const popup = this.parentNode;
        popup.style.animation = 'swoosh 0.3s ease-out';
        popup.addEventListener('animationend', function(){
            popup.remove()
        })
    })
})
