const user = {
        nickname: "nickname_example",
        files: ["/path/to/file.txt"]
    };

    document.getElementById('userNickname').innerText = `Nickname: ${user.nickname}`;

    const userFilesList = document.getElementById('userFilesList');
    user.files.forEach(file => {
        const listItem = document.createElement('li');
        listItem.classList.add('list-group-item');
        listItem.innerText = file;
        userFilesList.appendChild(listItem);
    });

    function addFile() {
        const fileInput = document.getElementById('fileInput');
        const filePath = fileInput.value.trim();

        if (filePath !== "") {
            fetch('/add_file', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ filePath: filePath }),
            })
            .then(response => response.json())
            .then(data => {
                alert(`File added: ${data.filePath}`);
            })
            .catch(error => {
                console.error('Error adding file:', error);
                alert('Error adding file. Please try again.');
            });
        } else {
            alert('Please enter a file path.');
        }
    }