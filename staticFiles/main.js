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

async function useInput() {
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
    const result = await fetch('/input', {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    if(result.status == 400){
        const old_value = document.getElementById("dir_files").value;
        document.getElementById("dir_files").value = await result.text();
        setTimeout(() => {
            document.getElementById("dir_files").value = old_value
        }, "5000");
    } else {
        const res = await result.json()
        let select = document.getElementById("index");
        select.innerHTML = '';
        for (const [key, value] of Object.entries(res)) {
            var option = document.createElement('option');
            option.value = key;
            option.text = key;
            select.add(option)
        }
        select.value = Object.keys(res)[0]
        index_items = res
        document.getElementById("filenames_by_index").value = index_items[Object.keys(res)[0]];
        clearInput()
    }
}

function clearQueryIndexFilenames() {
    document.getElementById("index").value = Object.keys(index_items)[0]
    document.getElementById("filenames_by_index").value = index_items[Object.keys(index_items)[0]];
}

function clearSearch() {
    document.getElementById('searchInput').value = ''
    document.getElementById('searchResult').value = ''
    document.getElementById('searchB').disabled = true
}

function inputSearch() {
    if (document.getElementById('searchInput').value.trim().length > 0) {
        document.getElementById('searchB').disabled = false
    }
}

function searchClick() {
    const text = document.getElementById('searchInput').value.trim();
    const index = document.getElementById("index").value.trim();
    const filenames = document.getElementById("filenames_by_index").value.trim();
    fetch(`/query?value=${text}&index=${index}&filenames=${filenames}`, { method: 'GET' })
        .then(response => response.text())
        .then(res => document.getElementById('searchResult').value = res)
        .catch(error => console.error('Error:', error));
}