const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Bot has started, with ${client.users.size} users, in ${client.channels.size} channels of ${client.guilds.size} guilds.`);
  client.user.setActivity(`Serving ${client.guilds.size} servers`);
});

client.on('message', message => {
  if(message.content === '/ayuda') {
    message.channel.send('Los comandos disponibles son: \n - /ayuda para mostrar esta lista de comandos \n - /informacion para mostrar información sobre el bot');
  } else if(message.content === '/informacion') {
    message.channel.send('Este es un bot genérico creado como ejemplo. Puedes usarlo como base para crear tu propio bot.');
  }
});

client.login('your-token-here');
