
const serverAddress = 'http://127.0.0.1:5000' // 127.0.0.1 è in HTTP l'indirizzo locale
// Cioè localhost
// Cioè, il tuo computer
// Ci va bene solo finché siamo in fase di sviluppo e lavoriamo sul nostro computer.

axios.get(serverAddress + "/universities")
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
