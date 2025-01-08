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
