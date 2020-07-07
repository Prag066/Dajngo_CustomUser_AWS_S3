function checkPassword(){
    var p = document.getElementById('password').value;
    var cp = document.getElementById('cpassword').value;
    var p_message = document.getElementById('p-match');
    var button = document.getElementById('sub-form');

    if (p != cp){
        console.log('password not matched');
        button.disabled = true;
        p_message.innerHTML = 'password not matched';
    }
    else {
        button.disabled = false;
        console.log('password matched')
        p_message.innerHTML = "";
    }
}