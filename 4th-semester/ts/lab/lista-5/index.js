#!/usr/bin/env node

// very simple express server for serving static files
const express = require('express');
const app = express();
const path = require('path')

app.use(express.static('public'));

app.get('/request-headers', (req, res, next) => {

  for (let i = 0; i < req.rawHeaders.length; i+=2) {
    res.write(req.rawHeaders[i] + ' ' + req.rawHeaders[i+1] + '\n');
  }

  next();

})

app.get('/test-html', function (req, res) {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
  next();
});

app.use((req, res, next) => {
  res.end();
})

app.listen(3000, () => console.log('listening on port 3000'));
