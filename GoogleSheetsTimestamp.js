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
