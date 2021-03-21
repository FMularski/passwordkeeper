$(document).ready( function () {
    const okBtn = document.querySelector('#ok-pin-btn');
    const dark = $('#dark-panel');
    const pinFormPanel = $('#pin-form-panel');
    let ajaxUrl = '';
    let currentShowBtn = null;

    function ajaxShowFunction() {
        const pin = $('#show-pin-input').val();

                $.ajaxSetup({
                    headers:{
                        "X-Requested-With": 'XMLHttpRequest'
                    }
                });

                $.ajax({
                    url: ajaxUrl,
                    method: 'GET',
                    data: {
                        'pin': pin
                    },
                    dataType: 'json',
                    success: response => {
                        $('.nes-input').val('');
                        dark.removeClass('active');
                        pinFormPanel.removeClass('active');

                        const shownPassword = $('.password-to-show');
                        shownPassword.text(response.decodedPassword);
                        shownPassword.addClass('shown-password');
                        currentShowBtn.classList.add('disabled');
                    },
                    error: xhr => {
                        location.reload();
                    }
                });
    }

    const showButtons = document.querySelectorAll('.show-btn');
    showButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            dark.addClass('active');
            pinFormPanel.addClass('active');
            currentShowBtn = this;
            
            ajaxUrl = this.getAttribute('url-to-pass');
            

            const accInfo = this.parentNode.parentNode.previousElementSibling.childNodes;
            let password = accInfo[9];

            // remove .password-to-show from other password tds
            const passwordsToShow = document.querySelectorAll('.password-to-show');
            passwordsToShow.forEach(pwd => {
                pwd.classList.remove('password-to-show');
            })

            // mark password to show with the class
            password.classList.add('password-to-show');

            okBtn.addEventListener('click', ajaxShowFunction, {once: true});

            
        }); 
    });


    const closePinFormIcon = $('#pin-form-close');
    closePinFormIcon.on('click', function(){
        $('.nes-input').val('');
        dark.removeClass('active');
        pinFormPanel.removeClass('active');

        okBtn.removeEventListener('click', ajaxShowFunction);
    });
})