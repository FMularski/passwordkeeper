$(document).ready( function() {
    const dark = $('#dark-panel');
    const pinForm = $('#pin-form');
    const accountFormPanel = $('#account-form-panel');
    const accountForm = document.querySelector('#account-form');
    console.log(accountForm);

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