function onEdit(e) {
     const activeSheet = e.source.getActiveSheet()

     const inRange = col >= 2 && col <= 5    // what culumns to check/search? 
     const notStartRow = row >= startRow     // check every row
     const isLog = activeSheet.getName() === "log"     // name of the log inside the sheet (tab)


     if(
          inRange &&
          notStartingRow &&
          isLog
     ) {
         activeSheet.getRange(row, 7).setValue(new Date())     // if value is changed in those parameters then print timestamp at the end of the row, you can make it on specific cell.
     }
}
