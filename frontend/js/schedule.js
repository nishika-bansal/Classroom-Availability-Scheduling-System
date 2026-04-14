function addSchedule(event) {
    event.preventDefault();

    const room_number = document.getElementById("room_id").value;
    const course_name = document.getElementById("course_name").value;
    const faculty_name = document.getElementById("faculty_name").value;
    const date = document.getElementById("date").value;
    const start_time = document.getElementById("start_time").value;
    const end_time = document.getElementById("end_time").value;

    const messageEl = document.getElementById("message");

    // ✅ VALIDATION
    if (!room_number || !course_name || !faculty_name || !date || !start_time || !end_time) {
        alert("Please fill all fields ❌");
        return;
    }

    if (end_time <= start_time) {
        alert("End time must be greater than start time ❌");
        return;
    }

    console.log("Sending schedule 😎");

    // 🔥 STEP 1: Convert room_number → room_id
    fetch("http://127.0.0.1:5001/classroom/get-rooms")
    .then(res => res.json())
    .then(classroomData => {

        const room = classroomData.data.find(r => r.room_number == room_number);

        if (!room) {
            alert("Room not found ❌");
            return;
        }

        const room_id = room.id;

        // 🔥 STEP 2: Send correct data
        return fetch("http://127.0.0.1:5001/schedule/schedule", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                room_id,   // ✅ FIXED
                course: course_name,
                faculty: faculty_name,
                date,
                start_time,
                end_time
            })
        });
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);

        messageEl.innerText = data.message;

        if (data.status === "success") {
            messageEl.style.color = "green";
            alert("Schedule added successfully ✅");
        } else {
            messageEl.style.color = "red";
        }
    })
    .catch(error => {
        console.error(error);
        messageEl.innerText = "Error connecting to server ❌";
        messageEl.style.color = "red";
    });
}

function goBack() {
    window.location.href = "../dashboard.html";
}


// ✅ LOAD SCHEDULES (FIXED)
function loadSchedules() {

    Promise.all([
        fetch("http://127.0.0.1:5001/classroom/get-rooms").then(res => res.json()),
        fetch("http://127.0.0.1:5001/schedule/get-schedule").then(res => res.json())
    ])
    .then(([classroomData, scheduleData]) => {

        console.log("Classrooms:", classroomData);
        console.log("Schedules:", scheduleData);

        let table = document.getElementById("scheduleTable");
        table.innerHTML = "";

        let classrooms = classroomData.data || [];   // ✅ FIXED
        let schedules = scheduleData.data || [];     // ✅ FIXED

        if (schedules.length === 0) {
            table.innerHTML = "<tr><td colspan='6'>No scheduled lectures found</td></tr>";
            return;
        }

        // ✅ Create map
        const roomMap = {};
        classrooms.forEach(room => {
            roomMap[room.id] = room.room_number;
        });

        schedules.forEach((s) => {
            const roomNumber = roomMap[s.room_id] || s.room_id;

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
        console.error(err);
        alert("Error loading schedules ❌");
    });
}