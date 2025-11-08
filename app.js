const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = process.env.PORT || 10000; // Use this to bind correctly in Render

// Start Python bot
const startBot = () => {
  exec('python ../python-bot/bot.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error starting Python bot: ${error}`);
      return;
    }
    console.log(`Bot output: ${stdout}`);
    if (stderr) {
      console.error(`Bot errors: ${stderr}`);
    }
  });
};

// Endpoint to indicate the server is running
app.get('/', (req, res) => {
  res.send('Express app is running with the bot!');
});

// Start the bot when the server starts
startBot();

app.listen(port, () => {
  console.log(`Express app listening on port ${port}`);
});
