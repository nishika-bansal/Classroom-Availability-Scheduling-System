console.log("JS FILE LOADED ");
function loadSchedules() {

    fetch("http://127.0.0.1:5001/schedule/get-schedule")
    .then(res => res.json())
    .then(scheduleData => {

        console.log("Schedules:", scheduleData);

        let table = document.getElementById("tableBody");
        if (!table) {
            console.error("tableBody not found ❌");
            return;
        }
        table.innerHTML = "";

        let schedules = scheduleData.data || [];   // ✅ FIX HERE

        if (!schedules || schedules.length === 0) {
            table.innerHTML = "<tr><td colspan='6'>No data ❌</td></tr>";
            return;
        }

        schedules.forEach(s => {

            const roomNumber = s.room_number || s.room_id;

            table.innerHTML += `
                <tr>
                    <td>${roomNumber}</td>
                    <td>${s.course}</td>
                    <td>${s.faculty}</td>
                    <td>${s.date}</td>
                    <td>${s.start_time}</td>
                    <td>${s.end_time}</td>
                </tr>
            `;
        });
    })
    .catch(err => {
        console.error("Error:", err);
        alert("Error loading schedules ❌");
    });
}