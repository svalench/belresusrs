const arrayInputId=["name_driver","data_auto","data_pricep","Nputev","pogruzka","razgruzka","agent","agentPoluchit","razreshil","osnovanie","prinal","sdal","gruzopoluchatel","doverennost","ttn","seria","nakladnaya","dateNakladnaya","name_tovar","ves_nakladnaya","ed_ves","cena","valuta","price_no_nds","nds","summ_nds","cena_nds","kol_mest","mass_gruza","description"];
const arrayLabelTrue=["Водитель","Автомобиль","Прицеп","№ путевого листа","Пункт погрузки","Пункт разгрузки","Грузоотправитель","Грузополучатель","Отпуск разрешил","Основание отпуска","Товар к доставке принял","Сдал грузоотправитель","Принял грузопучатель","Доверенность","Тип накладной","Серия накладной","Номер накладной","Дата накладной","Наименование товара","Количество","Ед","Цена","Валюта","Стоимость","Ставка НДС","Сумма НДС","Стоимость с НДС","Количествово мест","Масса груза","Описание"]
const arrayLabelFalse=["Водитель: Фамилия И.О.","Автомобиль","Прицеп","№ путевого листа","Пункт погрузки","Пункт разгрузки","Грузоотправитель","Грузополучатель","Отпуск разрешил","Основание отпуска","Товар к доставке принял","Сдал грузоотправитель","Принял грузопучатель","Доверенность","Тип накладной","Серия накладной","Номер накладной","Дата накладной","Наименование товара","Количество","Ед","Цена","Валюта","Стоимость","Ставка НДС","Сумма НДС","Стоимость с НДС","Количествово мест","Масса груза","Описание"]

$("#name_driver").change(function(e) {
   let regexp = /^[А-Яа-я\s.]+$/i;
    let lT=arrayLabelTrue[arrayInputId.indexOf(this.id)];
    let lF=arrayLabelFalse[arrayInputId.indexOf(this.id)];
    checkFieldRegexp(this,regexp,e);  
    changeLabel(this,$("label[for="+this.id+"]"),lT,lF)
});


$("#data_auto").change(function(e) {
    let lT=arrayLabelTrue[arrayInputId.indexOf(this.id)];
    let lF=arrayLabelFalse[arrayInputId.indexOf(this.id)];
    checkFieldEmpty(this,e);  
    changeLabel(this,$("label[for="+this.id+"]"),lT,lF)
});

$("#Nputev").change(function(e) {
    let lT=arrayLabelTrue[arrayInputId.indexOf(this.id)];
    let lF=arrayLabelFalse[arrayInputId.indexOf(this.id)];
    checkFieldEmpty(this,e);  
    changeLabel(this,$("label[for="+this.id+"]"),lT,lF)
});

$("#pogruzka").change(function(e) {
    let lT=arrayLabelTrue[arrayInputId.indexOf(this.id)];
    let lF=arrayLabelFalse[arrayInputId.indexOf(this.id)];
    checkFieldEmpty(this,e);  
    changeLabel(this,$("label[for="+this.id+"]"),lT,lF)
});

$("#razgruzka").change(function(e) {
    let lT=arrayLabelTrue[arrayInputId.indexOf(this.id)];
    let lF=arrayLabelFalse[arrayInputId.indexOf(this.id)];
    checkFieldEmpty(this,e);  
    changeLabel(this,$("label[for="+this.id+"]"),lT,lF)
});
// $("#data_auto").change(function(e) {
//    let regexp = /^[0-9]{4} [A-Z]{2}[-]{1}[0-9]{1}$/i;
//     checkField(this,regexp,e);  
//     changeLabel(this,$("label[for="+this.id+"]"),"Автомобиль","Номер: 1234 AB-7")
// });

// $("#data_pricep").change(function(e) {
//    let regexp = /^[0-9]{4} [A-Z]{2}[-]{1}[0-9]{1}$/i;
//     checkField(this,regexp,e);  
//     changeLabel(this,$("label[for="+this.id+"]"),"Автомобиль","Номер: 1234 AB-7")
// });
const checkFieldEmpty = (id,e) => {
    red = $(this).hasClass("border-danger");
    green = $(this).hasClass("border-success")
    if($(id).val() ==='' || $(id).val() ===0 || $(id).val() ===false) {
       e.preventDefault();
       if ((green==true) || (green==false && red==false)){
           $(id).removeClass("border-success");
            $(id).addClass("border-danger");
       };
   } else {
       if ((red==true) || (green==false && red==false)){
           $(id).removeClass("border-danger");
            $(id).addClass("border-success");
       }; 
   }
};


const checkFieldRegexp = (id, regexp,e) => {
    red = $(this).hasClass("border-danger");
    green = $(this).hasClass("border-success")
    if(!regexp.test($(id).val())) {
       e.preventDefault();
       if ((green==true) || (green==false && red==false)){
           $(id).removeClass("border-success");
            $(id).addClass("border-danger");
       };
   } else {
       if ((red==true) || (green==false && red==false)){
           $(id).removeClass("border-danger");
            $(id).addClass("border-success");
       }; 
   }
};

const changeLabel = (idInput,idLabel,labelTextTrue,labelTextFalse) =>{
    red = $(idInput).hasClass("border-danger");
    green = $(idInput).hasClass("border-success")
    if (green==true){
           $(idLabel).text(labelTextTrue);
           $(idLabel).css("color","#212529");
      
   } else {
       $(idLabel).text(labelTextFalse);
       $(idLabel).css("color","#dc3545");
       }
   };

const checkAllFields = () => {
    let status=0;
    arrayInputId.forEach(function(item,i){
        if (($("#"+item+"").val()==='') || ($("#"+item+"").val()===0)) {
            status++
            $("#"+item+"").addClass('border-danger');
            $("label[for="+item+"]").text(arrayLabelFalse[i]).css("color","#dc3545"); 
                                          };
                                          });
    if (status>0){
        return false;
    } else {
        return true;
    }
        };

const clearFields = () => {
    arrayInputId.forEach(function(item,i){
        $("#"+item+"").val('').removeClass("border-success").removeClass("border-danger");
        $("label[for="+item+"]").text(arrayLabelTrue[i]).css("color","#212529");
        // console.log(item+" - "+arrayLabelTrue[i])
    });
    $("#ttn").val('1');
    $("#ed_ves").val('1');
    $("#valuta").val('1');
    $("#nds").val('20');
    // alert('done');
};


