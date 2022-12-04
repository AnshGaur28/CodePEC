window.onload = function () {
    var spread = new GC.Spread.Sheets.Workbook(document.getElementById("ss"), { sheetCount: 1 });
    initSpread(spread);
};

function initSpread(spread) {
        spread.suspendPaint();
        spread.fromJSON(data);
        var sheet = spread.sheets[0];
        var printInfo = sheet.printInfo();

        printInfo.showBorder(false);
        printInfo.showGridLine(false);
        printInfo.showColumnHeader(GC.Spread.Sheets.Print.PrintVisibilityType.hide);
        printInfo.showRowHeader(GC.Spread.Sheets.Print.PrintVisibilityType.hide);
        
        var style = new GC.Spread.Sheets.Style();
        style.cellButtons = [
             {

                caption:"Print",
                buttonBackColor: "#FA896B",
                hoverBackColor: "#CCCCCC",
                useButtonStyle: true,
                width:150,
                height:70,
                command: (sheet, row, col, option) => {
                        spread.print(0);
                }
           }
        ];
        style.foreColor = "white";
        style.font = "15pt Calibri";
        sheet.setStyle(0, 20, style);
        spread.resumePaint();
    }



(function search(){
    let searchinput = document.getElementById("#searchbar")
    searchinput = searchinput.value.toLowerCase();
    let x = getElementByClassName('employee__info--title');

    for (i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(searchinput)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="";                 
        }
    }   
})();
