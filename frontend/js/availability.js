// 🔍 CHECK AVAILABILITY
console.log("JS LOADED 🚀");

function checkAvailability() {
    console.log("Button Clicked😎");

    const room_number = document.getElementById("room_id").value; // ✅ correct ID
    const date = document.getElementById("date").value;
    const start_time = document.getElementById("start_time").value;
    const end_time = document.getElementById("end_time").value;

    // ✅ VALIDATION
    if (!room_number || !date || !start_time || !end_time) {
        alert("Please fill all fields ⚠️");
        return;
    }

    // 🔥 STEP 1: Get classrooms to convert room_number → room_id
    fetch("http://127.0.0.1:5001/classroom/get-rooms")
    .then(res => res.json())
    .then(classroomData => {

        console.log("Classrooms:", classroomData);

        const room = classroomData.data.find(r => r.room_number == room_number);

        if (!room) {
            alert("Room not found ❌");
            return;
        }

        const room_id = room.id; // ✅ NOW defined

        console.log("Using room_id:", room_id);

        // 🔥 STEP 2: Check availability with correct room_id
        return fetch("http://127.0.0.1:5001/availability/check", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                room_id,
                date,
                start_time,
                end_time
            })
        });
    })
    .then(res => res.json())
    .then(data => {
        console.log("Response:", data);

        alert(data.message); // ✅ show backend message
    })
    .catch(err => {
        console.error(err);
        alert("Error connecting to server ❌");
    });
}


// 📋 LOAD SCHEDULE
function loadAvailability() {
    fetch("http://127.0.0.1:5001/schedule/get-schedule")
    .then(res => res.json())
    .then(scheduleData => {
        console.log("Schedules:", scheduleData);

        let table = document.getElementById("tableBody");
        table.innerHTML = "";

        let schedules = scheduleData.data; // ✅ correct key

        if (!schedules || schedules.length === 0) {
            table.innerHTML = "<tr><td colspan='5'>No scheduled lectures found ❌</td></tr>";
            return;
        }

        schedules.forEach(schedule => {
            const roomNumber = schedule.room_number || schedule.room_id;

            table.innerHTML += `
                <tr>
                    <td>${roomNumber}</td>
                    <td>${schedule.course}</td>
                    <td>${schedule.faculty}</td>
                    <td>${schedule.date}</td>
                    <td>${schedule.start_time} - ${schedule.end_time}</td>
                </tr>
            `;
        });
    })
    .catch(err => {
        console.error(err);
        alert("Error loading schedule data ❌");
    });
}