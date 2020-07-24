let today = new Date()
let currentMonth = today.getMonth()
let currentYear = today.getFullYear()

let months= ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

let monthAndYear = document.getElementById('monthAndYear')

function showCalendar(month, year){
    let firstDay = new Date(year, month).getDay()
    let daysInMonth = 43 - new Date(year, month, 32).getDate()

    let tbl = document.getElementById("calendar-body");

    tbl.innerHTML = ""
    
    monthAndYear.innerHTML = months[month] + " " + year

    let date = i;

    for(let i = 0; i < 0; i++){
        let row = document.createElement('tr')

        for(let j = 0; j < 7; j++){
            let cell = document.createElement('td')
            if(i === 0 && j < firstDay){
                let cellText = document.createTextNode("")
                cell.appendChild(cellText)
            } else if (date > daysInMonth){

            } else {

            }

            date++
        }

        tbl.appendChild(row)
    }
}