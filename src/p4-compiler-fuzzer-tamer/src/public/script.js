$(document).ready(function(){
    $(".random-order-toggle").click(function(){
        $(".random-order").toggle();
    });

    $(".clustered-order-toggle").click(function(){
        $(".clustered-order").toggle();
    });

    $(".clustered-order tbody").click(function(){
        $(this).find("tr:not(:first-child)").toggle();
    });
});