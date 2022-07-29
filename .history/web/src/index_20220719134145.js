

const serverAddress = 'http://127.0.0.1:5000' // 127.0.0.1 è in HTTP l'indirizzo locale
// Cioè localhost
// Cioè, il tuo computer
// Ci va bene solo finché siamo in fase di sviluppo e lavoriamo sul nostro computer.
function getUniversities() {

    const searchInput = document.getElementById('search-input-text').value;


    axios.get(serverAddress + `/universities?search=${searchInput}`)
        .then(function (response) {
            // handle success

            const listOfUniversities = response.data.universities;

            document.getElementById("universities").replaceChildren([]);

            for (let i = 0; i < 10; i++) {

                const university = listOfUniversities[i]
                const universityNode = document.createElement('div');
                const universityTitleNode = document.createElement('h2');
                const universityImageNode = document.createElement('img');
                const universityDescriptionNode = document.createElement('p');
                universityTitleNode.innerText = university.name;
                universityImageNode.src = university.imgSrc;
                universityDescriptionNode.innerText = university.description;
                universityNode.classList.add('university');
                universityNode.appendChild(universityTitleNode);
                universityNode.appendChild(universityImageNode);
                universityNode.appendChild(universityDescriptionNode);

                document.getElementById("universities").appendChild(universityNode);

            }
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
}

function onSearchInputKeyUp(e) {
    if (e.key === 'Enter') {
        getUniversities();
    }

    if (e.key.value === 'ciao') {
        alert('ciao');
    }


    if (e.key.value === 'ciao') {
        getUniversities();
    }

}

function onLoad() {
    // Quello che vogliamo che succeda non appena la pagina ha finito di caricare la prima volta.
    getUniversities();
    let load = document.getElementById('');
}

window.onload = onLoad;


$(window).on("load", function () {
    $(".loader-wrapper").fadeOut("slow");
})

