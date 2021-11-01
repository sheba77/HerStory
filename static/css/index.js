
var userInput;

$( document ).ready(function() {
//        localStorage.setItem("test1", "Smith");
    $(".searchImg").click(function(){
      userInput =  $("#searchbox").val();
      var data = localStorage.getItem("test1");
      $(".femBox").attr("data-femvalue",data);
    });

});