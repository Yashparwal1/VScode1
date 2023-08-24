const loginAsAdminBtn = document.getElementById("login-admin")
const loginAsYashBtn = document.getElementById("login-yash")
const loginAsKetonBtn = document.getElementById("login-keton")
const AdminBtn = document.getElementById("admin")
const responseDiv = document.getElementById("responses")

loginAsAdminBtn.addEventListener("click", () => {
    login("parwals")
})
loginAsYashBtn.addEventListener("click", () => {
    login("yash")
})
loginAsKetonBtn.addEventListener("click", () => {
    login("keton")
})
AdminBtn.addEventListener("click", () => {
    fetch("http://localhost:3000/adminData", {
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then(res => res.text())
    .then(data => (responseDiv.textContent = data))
})

function login(username){
    fetch("http://localhost:3000/login",{
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type":"application/json",
        },
        body: JSON.stringify({username}),
    })
    .then(res => res.text())
    .then(data => (responseDiv.textContent = data))
}