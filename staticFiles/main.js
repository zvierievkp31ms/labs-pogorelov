function updateIndexSelectInput() {
    var selectedValue = document.getElementById("index").value;
    document.getElementById("filenames_by_index").value = index_items[selectedValue];
}
updateIndexSelectInput()

function updateDirSelectInput() {
    var selectedValue = document.getElementById("dir").value;
    document.getElementById("dir_files").value = dir_items[selectedValue].join('\n');
}
updateDirSelectInput()

function clearInput() {
    document.getElementById('input_index_file').value = 'index'
    document.getElementById('input_filenames_file').value = 'filenames'
}

function useInput() {
    let index = document.getElementById('input_index_file').value;
    const index_name = index.trim().length > 0 ? index.trim() : 'index';
    let filenames = document.getElementById('input_filenames_file').value;
    const filenames_name = filenames.trim().length > 0 ? filenames.trim() : 'filenames';
    const dir = document.getElementById("dir").value;

    const data = {
        index: index_name,
        filenames: filenames_name,
        dir: dir
    }
    fetch('/input', {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
        .then(response => clearInput())
        .catch(error => console.error('Error:', error));
}


//value index filenames



function selectFiles() {
    document.getElementById('uploadFiles').disabled = false
    var input = document.getElementById('indexed_file')
    let res = ''
    for (const file of input.files) {
        res += file.name + '\n'
    }
    document.getElementById('inputFilesTextarea').value = res
}

function uploadFiles() {
    var input = document.getElementById('indexed_file')
    var data = new FormData()
    for (const file of input.files) {
        data.append('file', file, file.name);
    }
    fetch('/upload', { method: 'POST', body: data })
        .then((response) => {
            if (response.status == 200) {
                return response.blob();
            }
            return
        })
        .then(blob => {
            if (blob) {
                var file = window.URL.createObjectURL(blob);
                window.location.assign(file);
            }
        }).then(res => clearIndexFilenames())
        .catch(error => console.error('Error:', error));
}

function clearFiles() {
    document.getElementById('indexed_file').value = ''
    document.getElementById('inputFilesTextarea').value = ''
    document.getElementById('uploadFiles').disabled = true
}

function selectIndexFilenames() {
    document.getElementById('uploadIndexFilenamesFiles').disabled = false
}

function uploadIndexFilenames() {
    var index_input = document.getElementById('index_file')
    var filenames_input = document.getElementById('filenames_file')
    var data = new FormData()
    if (index_input.files[0]) {
        data.append('file', index_input.files[0], 'index');
    }
    if (filenames_input.files[0]) {
        data.append('file', filenames_input.files[0], 'filenames');
    }
    fetch('/index_filenames', { method: 'POST', body: data })
        .then(response => clearFiles())
        .catch(error => console.error('Error:', error));
}

function clearIndexFilenames() {
    document.getElementById('index_file').value = ''
    document.getElementById('filenames_file').value = ''
    document.getElementById('uploadIndexFilenamesFiles').disabled = true
}

function inputSearch() {
    if (document.getElementById('searchInput').value.trim().length > 0) {
        document.getElementById('searchB').disabled = false
    }
}

function searchClick() {
    const text = document.getElementById('searchInput').value.trim();
    fetch('/query?value=' + text, { method: 'GET' })
        .then(response => response.text())
        .then(res => document.getElementById('searchResult').value = res)
        .catch(error => console.error('Error:', error));
}

function clearSearch() {
    document.getElementById('searchInput').value = ''
    document.getElementById('searchResult').value = ''
    document.getElementById('searchB').disabled = true
}