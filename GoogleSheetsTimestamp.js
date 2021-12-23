function onEdit(e) {

  var startRow = 1;
  var row = e.range.getRow();
  var col = e.range.getColumn();

  const activeSheet = e.source.getActiveSheet()
  const inRange = col >= 1 && col <= 10    // what culumns to check/search? 
  const notStartingRow = row >= startRow     // check every row
  const isLog = activeSheet.getName() === "log"     // name of the log inside the sheet (tab)

  if(
      inRange &&
      notStartingRow &&
      isLog
  ) {
      activeSheet.getRange(row, 11).setValue(new Date())     // if value is changed in those parameters then print timestamp at the end of the row, you can make it on specific cell.
  }
}
// EXAMPLE:
// function onEdit(e) {

//   var startRow = 1;
  
//   var row = e.range.getRow();
//   var col = e.range.getColumn();

//   if(col >= 2 && col <= 6 && row >= startRow && e.source.getActiveSheet().getName() === "Log about stuff 1"){
//     e.source.getActiveSheet().getRange(row,8).setValue(new Date());
//   }

//   if(col >= 1 && col <= 11 && row >= startRow && e.source.getActiveSheet().getName() === "Log about other stuff"){
//     e.source.getActiveSheet().getRange('B1').setValue(new Date());
//   }

//   if(col >= 1 && col <= 5 && row >= startRow && e.source.getActiveSheet().getName() === "useless log"){
//     e.source.getActiveSheet().getRange('B1').setValue(new Date());
//   }

//   if(col === 3 && row >= startRow && e.source.getActiveSheet().getName() === "i.d.e.n"){
//     e.source.getActiveSheet().getRange(row,1).setValue(new Date());
//   }

// }
