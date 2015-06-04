$(document).ready(function (){
    $('#featuredblog').click(function () {
        console.log('hi');
        mixpanel.track('Blog footer clicked');
        setTimeout(function(){},5000);
    });
});