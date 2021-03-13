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

    const closeForm = $('i');
    closeForm.on('click', function(){
      

        $('input').val('');

        dark.removeClass('active');
        pinForm.removeClass('active');
        accountForm.removeClass('active');
    });
});