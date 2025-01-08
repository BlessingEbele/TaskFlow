const response = await fetch('http://127.0.0.1:8000/api/auth/', {
    method: 'GET',
    headers: {
        'Authorization': `Basic ${btoa(`${username}:${password}`)}`
    }
})



function saveCredentials(username, password) {
    localStorage.setItem('auth', btoa(`${username}:${password}`));
}

function getAuthHeader() {
    const auth = localStorage.getItem('auth');
    return auth ? `Basic ${auth}` : null;
}

function clearCredentials() {
    localStorage.removeItem('auth');
}
