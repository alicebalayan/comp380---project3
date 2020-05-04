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
function pad(num, size) {
    var s = num+"";
    while (s.length < size) s = "0" + s;
    return s;
}
function deleteItem(type,id) {
    $("#deleteID").html(type.substring(0, 1)+pad(id,4));
    $('#delete-modal').modal('show');
    $("#confirmDelete").click(function () {
        var requestURL = "/"+type+"Delete?id="+id;
        $.ajax(requestURL);
        $('#delete-modal').modal('hide');
        location.reload();


    });
    // var requestURL = $("#createbtn").attr();

    // $("#modal-sample").load(requestURL);
}