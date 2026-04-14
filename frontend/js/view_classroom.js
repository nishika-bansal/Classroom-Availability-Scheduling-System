function loadClassrooms() {
    fetch("http://127.0.0.1:5001/classroom/get-rooms")
    .then(res => res.json())
    .then(data => {
        let table = document.getElementById("tableBody");
        table.innerHTML = "";

        // ✅ FIX: data.data ❌ → data ✅
        data.data.forEach(room => {
            table.innerHTML += `
                <tr>
                    <td>${room.id}</td>
                    <td>${room.room_number}</td>
                    <td>${room.capacity}</td>
                    <td>${room.type}</td>
                    <td>
                        <button onclick="deleteRoom(${room.id})">Delete</button>
                        <button onclick="editRoom(${room.id}, '${room.room_number}', ${room.capacity}, '${room.type}')">Edit</button>
                    </td>
                </tr>
            `;
        });
    })
    .catch(err => console.error(err));
}


// ❌ DELETE
function deleteRoom(id) {
    fetch(`http://127.0.0.1:5001/classroom/delete-room/${id}`, {
        method: "DELETE"
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadClassrooms(); // refresh table
    });
}


// ✏️ EDIT / UPDATE
function editRoom(id, room_number, capacity, room_type) {

    let newRoom = prompt("Enter new room number:", room_number);
    let newCapacity = prompt("Enter new capacity:", capacity);
    let newType = prompt("Enter new type:", room_type);

    fetch(`http://127.0.0.1:5001/classroom/update-room/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            room_number: newRoom,
            capacity: newCapacity,
            type: newType
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        loadClassrooms(); // refresh
    });
}


// 🔙 BACK
function goBack() {
    window.location.href = "../dashboard.html";
}