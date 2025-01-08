document.addEventListener('DOMContentLoaded', async () => {
    const authHeader = getAuthHeader();
    if (!authHeader) {
        window.location.href = 'login.html';
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/api/tasks/', {
            method: 'GET',
            headers: {
                'Authorization': authHeader,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const tasks = await response.json();
            const taskList = document.getElementById('taskList');
            tasks.forEach(task => {
                const li = document.createElement('li');
                li.textContent = task.name;
                taskList.appendChild(li);
            });
        } else {
            const errorData = await response.json();
            document.getElementById('errorMessage').textContent = errorData.detail || 'Failed to fetch tasks.';
        }
    } catch (error) {
        document.getElementById('errorMessage').textContent = 'An error occurred. Please try again.';
    }
});

document.getElementById('logout').addEventListener('click', () => {
    clearCredentials();
    window.location.href = 'login.html';
});
