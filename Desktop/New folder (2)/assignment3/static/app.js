const UserRegister = (firstname, lastname, username, password) => {
    fetch("http://127.0.0.1:5000/register",
        {
            method: "POST",
            body: JSON.stringify({
                firstname: firstname,
                lastname: lastname,
                username: username,
                password: password,
            }),
            headers: {
                "content-type": "application/json; charset=UTF-8 "
            }
        }).then((response) => {
            console.log(response)
        }).catch((err) => {
            console.log(err)
        });
}
const UserLogin = async (username, password) => {
    const response = await fetch("http://127.0.0.1:5000/auth",
        {
            method: "POST",
            body: JSON.stringify({
                username: username,
                password: password,
            }),
            headers: {
                "content-type": "application/json; charset=UTF-8 "
            }
        })
    const promise = await response.json();
    return promise.access_token;
}
const salesToday = async () => {
    const response = await fetch("http://127.0.0.1:5000/salesToday");
    const promise = await response.json();
    return (promise["today's sales"]);
}
const uniqueVisitors = async () => {
    const response = await fetch("http://127.0.0.1:5000/Uniquevisitors");
    const promise = await response.json();
    return promise;
}





