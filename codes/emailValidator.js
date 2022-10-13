/**
 * @param {*string} email 
 * @returns Boolean
 */
function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

var validEmailsList = [
    "valid@gmail.com",
    "valid1@gmail.com",
    "valid.1.true@gmail.com"
]

var inValidEmailsList = [
    null,
    undefined,
    0,
    "+",
    "invalid@",
    "invalid@gmail",
    "invalid@gmail.",
    "invalid.gmail.com"
]

validEmailsList.forEach(element => {
    console.log("email - "+ " " + element + " ->", validateEmail(element));    
});
inValidEmailsList.forEach(element => {
    console.log("email - "+ " " + element + " ->", validateEmail(element));    
});
