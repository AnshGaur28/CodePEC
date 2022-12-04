$(document).on("click", ".employee i", function(){
    $(this).next(".employee__info").toggle("medium");
    $(this).toggleClass(" fa-info fa-times");
});