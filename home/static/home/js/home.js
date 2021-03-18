$(document).ready( function() {
    const dark = $('#dark-panel');
    const pinForm = $('#pin-form');
    const accountFormPanel = $('#account-form-panel');
    const accountForm = document.querySelector('#account-form');

    /* show options buttons */
    const table = $('table');    
    table.on('click', '.gear', function(){
        const tr = $(this).parent().parent();
        const settings = tr.next();

        settings.toggleClass('hidden');
    });

    /* show pin form - SHOW*/
    table.on('click', '.show-btn', function(){
        const pinForm = $('#pin-form');
        dark.addClass('active');
        pinForm.addClass('active');
    });

    /* show account form - EDIT */
    table.on('click', '.edit-btn', function(){
        dark.addClass('active');
        accountFormPanel.addClass('active');
    })

    /* show account form - ADD*/
    const addBtn = $('#add-btn');
    addBtn.on('click', function(){
        dark.addClass('active');
        accountFormPanel.addClass('active');
        accountForm.action = '';    // override action after clicking edit btn

        document.querySelector('#id_title').value = '';  
        document.querySelector('#id_login').value = '';
        document.querySelector('#id_email').value = '';
        document.querySelector('#id_password').value = '';
        document.querySelector('#id_confirm').value = '';
    });


    /* show confirm delete dialog */
    const confirmDeleteDialog = $('#confirm-del-form-panel');
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const confDelNoBtn = document.querySelector('#confirm-del-no-btn');
    const confDelForm = document.querySelector('#conf-del-form');

    deleteButtons.forEach(btn => {
        btn.addEventListener('click', function(){
            dark.addClass('active');
            confirmDeleteDialog.addClass('active');

            confDelForm.action = this.getAttribute('url-to-pass');
        })
    })

    // cancel delete
    confDelNoBtn.addEventListener('click', function(){
        dark.removeClass('active');
        confirmDeleteDialog.removeClass('active');
    })


    /* EDIT ACCOUNT */
    const editButttons = document.querySelectorAll('.edit-btn');

    editButttons.forEach(btn => {
        btn.addEventListener('click', function(){
            accountForm.action = this.getAttribute('url-to-pass');

            // fill account field with values
            const accInfo = this.parentNode.parentNode.previousElementSibling.childNodes;

            let title = accInfo[3].innerText;
            let login = accInfo[5].innerText;
            let email = accInfo[7].innerText;
            let password = accInfo[9].innerText;

            if (login == '-') login = '';
            if (email == '-') email = '';

            document.querySelector('#id_title').value = title;
            document.querySelector('#id_login').value = login;
            document.querySelector('#id_email').value = email;
            document.querySelector('#id_password').value = password;
            document.querySelector('#id_confirm').value = password;
        })
    })




    const closeForm = $('i');
    closeForm.on('click', function(){
        $('.nes-input').val('');
        dark.removeClass('active');
        pinForm.removeClass('active');
        accountFormPanel.removeClass('active');
    });
});