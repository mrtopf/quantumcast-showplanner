

$(document).ready(function() {
    $(".link-source .draggable").draggable({
        helper: "clone",
        connectToSortable: ".link-destination",
    });
    $(".nolink-destination").droppable({
        activeClass: "droppable-active",
        drop: function( event, ui ) {
            $(ui.draggable).removeClass("draggable");
            $(ui.draggable).removeClass("ui-draggable");
            $(ui.draggable).appendTo(this);
        }
    });
    $(".link-destination").sortable({
        axis: "y"
    });

});
