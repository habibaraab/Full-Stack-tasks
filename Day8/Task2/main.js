document.addEventListener("DOMContentLoaded", async function() {

    const apiUrl = "https://jsonplaceholder.typicode.com/users";
    
    const tableBody = document.querySelector("#usersTable tbody");
    try {
        const response = await fetch(apiUrl);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const users = await response.json();
        tableBody.innerHTML = "";

        users.forEach(user => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${user.name}</td>
                <td>${user.email}</td>
                <td>${user.address.city}</td>
                <td>${user.company.name}</td>
            `;
            tableBody.appendChild(row);
        });

    } catch (error) {
        console.error("Fail to fetch user data:", error);
        tableBody.innerHTML = `<tr><td colspan="4" style="text-align:center; color:red;">Failed to load data.</td></tr>`;
    }
});
