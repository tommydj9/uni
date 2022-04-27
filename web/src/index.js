

const serverAddress = 'http://127.0.0.1:5000' // 127.0.0.1 è in HTTP l'indirizzo locale
// Cioè localhost
// Cioè, il tuo computer
// Ci va bene solo finché siamo in fase di sviluppo e lavoriamo sul nostro computer.

axios.get(serverAddress + "/universities")
    .then(function (response) {
        // handle success

        const listOfUniversities = response.data.universities;

        for (let i = 0; i < listOfUniversities.length; i++) {
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

function changePage() {
    window.open('./learnMore.html');
}

universities.addEventListener('click', function () {
    changePage();
});

let learn = document.getElementById("nameLearnMore");
learn.innerHTML = listOfUniversities;



