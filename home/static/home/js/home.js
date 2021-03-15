$(document).ready( function() {
    const dark = $('#dark-panel');
    const pinForm = $('#pin-form');
    const accountForm = $('#account-form-panel');

    /* show options buttons */
    const table = $('table');    
    table.on('click', '.gear', function(){
        const tr = $(this).parent().parent();
        const settings = tr.next();

        $(this).click(function() {
            settings.toggleClass('hidden');
        })
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
        accountForm.addClass('active');
    })

    /* show account form - ADD*/
    const addBtn = $('#add-btn');
    addBtn.on('click', function(){
        dark.addClass('active');
        accountForm.addClass('active');
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

    confDelNoBtn.addEventListener('click', function(){
        dark.removeClass('active');
        confirmDeleteDialog.removeClass('active');
    })

    const closeForm = $('i');
    closeForm.on('click', function(){
        $('.nes-input').val('');
        dark.removeClass('active');
        pinForm.removeClass('active');
        accountForm.removeClass('active');
    });
});