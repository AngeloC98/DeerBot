const Discord = require('discord.js');
const client = new Discord.Client();
const config = require('./config.json');

// On bot ready.
client.once('ready', () => {
    console.log('Bot is ready!');
});

client.login(config.token);