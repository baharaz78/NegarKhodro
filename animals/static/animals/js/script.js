$("#add-button").on("click", (e) => {
    $(e.target).hide();
    $("#add-form").fadeIn();
})

$(".animal-edit").on("click", (e) => {
    $(e.target).hide().parent().parent().find(".card-body").fadeIn();
})