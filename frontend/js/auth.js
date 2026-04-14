window.onbeforeunload = function () {
    console.log("PAGE IS LOADING");
};

function login() {
    console.log("Login Function called");

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // ✅ Basic validation
    if (!username || !password) {
        alert("Please enter username and password ❌");
        return;
    }

    console.log("Sending request");

    fetch("http://127.0.0.1:5001/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(async (res) => {
        console.log("response received");

        const data = await res.json();

        return {
            ok: res.ok,
            status: res.status,
            body: data
        };
    })
    .then(result => {
        console.log("DATA:", result.body);

        if (result.ok && result.body.status === "success") {

            // ✅ STORE COMPLETE USER OBJECT (BEST PRACTICE)
            localStorage.setItem("user", JSON.stringify(result.body.user));

            // (optional - if you still want separate keys)
            localStorage.setItem("username", result.body.user.username);
            localStorage.setItem("role", result.body.user.role);

            alert("Login successful ✅");

            console.log("Redirecting to dashboard...");
            window.location.href = "dashboard.html";

        } else {
            alert(result.body.message || "Invalid username or password ❌");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Server error ❌");
    });
}