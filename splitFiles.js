const fs = require('fs')
const fileData = fs.readFileSync('before.csv', 'utf-8')
const elements = fileData.split(/",\s*|\s*"\n|\n\s*"/)

const chunkSize = 20
for (let i = 0; i < elements.length; i += chunkSize) {
    if(elements[i].split('\n').length>=25){
        const chunk = elements.slice(i, i + chunkSize)
        fs.writeFile(`filesUntil${i}_${chunkSize}.csv`, `${chunk.join('\n')}\n`, (err) => {
          if (err) throw err
          console.log(`Chunk ${i / chunkSize + 1} written`)
        })
    }

}
