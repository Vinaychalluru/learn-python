$( document ).ready(function() {

   function perform_calc() {
    var op1 = document.getElementById("op1").value ;
    var op2 = document.getElementById("op2").value ;
    var req_inp = '{ "op1" : ' + op1 + ', "op2" : ' + op2 + '}'
    // document.getElementById("calc_result").innerHTML = "Test"
    $.post( "/calc", {
        calc_inp : JSON.stringify(req_inp)
    }, function(err, req, resp){
        document.getElementById("calc_result").innerHTML = resp["responseJSON"]["calc_result"]
    });
    }
 });