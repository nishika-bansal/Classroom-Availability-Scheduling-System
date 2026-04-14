// ➕ Add classroom
function addClassroom() {
    const room_number = document.getElementById("room_number").value;
    const capacity = document.getElementById("capacity").value;
    const room_type = document.getElementById("room_type").value;
    const messageEl = document.getElementById("message");

    console.log("Button clicked 😎");

    if (!room_number || !capacity) {
        messageEl.innerText = "Room number and capacity required ❌";
        messageEl.style.color = "red";
        return;
    }

    fetch("http://127.0.0.1:5001/classroom/add-room", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            room_number: room_number,
            capacity: capacity,
            type: room_type
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);

        messageEl.innerText = data.message;

        if (data.message && data.message.toLowerCase().includes("added")) {
            messageEl.style.color = "green";
        } else {
            messageEl.style.color = "red";
        }

        // clear form
        document.getElementById("room_number").value = "";
        document.getElementById("capacity").value = "";
        document.getElementById("room_type").value = "";
    })
    .catch(err => {
        console.error(err);
        messageEl.innerText = "Server error ⚠️";
        messageEl.style.color = "red";
    });
}


// 📋 Load classrooms
function loadClassrooms() {
    fetch("http://127.0.0.1:5001/classroom/get-rooms")
    .then(res => res.json())
    .then(data => {
        console.log(data);

        const list = document.getElementById("classroomList");
        list.innerHTML = "";

        data.data.forEach(room => {
            const li = document.createElement("li");
            li.innerText = `Room ${room.room_number} | Capacity: ${room.capacity} | Type: ${room.type}`;
            list.appendChild(li);
        });
    })
    .catch(err => console.error(err));
}


// 🔍 Search classroom
function searchRoom() {
    let value = document.getElementById("search").value.toLowerCase();
    let rows = document.querySelectorAll("tbody tr");

    rows.forEach(row => {
        row.style.display = row.innerText.toLowerCase().includes(value) ? "" : "none";
    });
}