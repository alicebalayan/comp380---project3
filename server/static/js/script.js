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
    $("#itemFormSaveBTN").click(function () {
        $("#itemForm").submit();
    });
    $("#modal-sample").load(requestURL);
    $('#modal-sample').modal('show');
}
function pad(num, size) {
    var s = num+"";
    while (s.length < size) s = "0" + s;
    return s;
}
function deleteItem(type,id) {
    $("#deleteID").html(type.substring(0, 3).toUpperCase()+pad(id,4));
    $('#delete-modal').modal('show');
    $("#confirmDelete").click(function () {
        var requestURL = "/"+type+"Delete?id="+id;
        $.ajax(requestURL).done(function() {
            location.reload();
        });
        $('#delete-modal').modal('hide');
    });
}
function submitItem(){
    $("#itemForm").submit();

}
function editItem(type,id) {
   
    var requestURL = "/"+type+"Edit?id="+id;
    $("#modal-sample").load(requestURL);
    $('#modal-sample').modal('show');
    // var requestURL = $("#createbtn").attr();

    // $("#modal-sample").load(requestURL);
}