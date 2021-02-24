type map = {
    "difficulties": string[],
    "mapper": string,
    "status": string,
    "name": string,
    "cp": string,
    hash: string,
    cover: string
}

window.onload = async () => {
    var wholeTable = document.getElementById('maps-table')
    var loading = document.getElementById('loading-symbol')

    var maps: map[] = await (await fetch('/api/maps/all')).json().catch(() => {
        var error = document.getElementsByClassName('error')[0]

        error.innerHTML = "Error getting maps. 404 Not Found"
        error.classList.remove('hidden')
        loading.classList.add('hidden')

        return;
    })

    var table = document.getElementById('cp_table')

    maps.forEach(async (map) => {
        var scores = await (await fetch(`/api/maps/${map.hash}/scores`)).json()

        var row = document.createElement('tr')

        var name = document.createElement('th')
        name.innerHTML = `<img src="${map.cover}" class='pfp'> &nbsp; ${map.name}`
        row.appendChild(name)

        var mapper = document.createElement('th')
        mapper.innerText = map.mapper
        row.appendChild(mapper)

        var scoreCount = document.createElement('th')
        scoreCount.innerText = scores.scores.length.toString()
        row.appendChild(scoreCount)

        var cp = document.createElement('th')
        cp.innerText = map.cp + ' CP'
        row.appendChild(cp)

        table.appendChild(row)
    })
    wholeTable.classList.remove('hidden')
    loading.classList.add('hidden')
}
/*
<tr>
    <th><img src="src/Maps/b6b84dc10c68d379215a54ece4b108e5cfe084d8.jpg" class='pfp'> &nbsp; TTFAF but its all resets</th>
    <th>Thijnmens</th>
    <th>24</th>
    <th>670.48 CP</th>
</tr>
*/