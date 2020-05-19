$("#clickDataNakladnaya").click(function(){ 
   displayBlock("#DanniePoTransporty");                              
});

$("#clickDataSvet").click(function(){  
   displayBlock("#svetControl");                              
});

$("#clickDataCamera").click(function(){  
   displayBlock("#cameraControl");                               
});

const displayBlock = (blockId) => {
    if ($(blockId).css('display') == 'none') 
        { 
            $(blockId).animate({height: 'show'}, 300); 
        } 
    else 
        {     
            $(blockId).animate({height: 'hide'}, 300); 
        }  
};