var collapse = false;

function togglesidebar() {
    $("#sideBar").toggleClass("collapsebar");
    $(".menuBtn span").toggleClass("hidden");
    $(".searchBoxSide").toggleClass("hidden");
    $('#sideBar .collapse').collapse('hide')
    collapse = (collapse) ? false : true;
}
$(".collapseBtn").click(function () {
    togglesidebar();
});
$(".dropDownMenu").click(function () {
    if (collapse) {
        togglesidebar();
    }
});

function create() {
    var requestURL = $("#createbtn").attr("data-url");

    $("#modal-sample").load(requestURL);
    $('#modal-sample').modal('show');
}