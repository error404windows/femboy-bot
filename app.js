const express = require('express')
const app = express()
const port = process.env.PORT || 10000

app.get('/', (req, res) => {
  res.send('Running')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
