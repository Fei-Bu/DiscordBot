const Discord = require('discord.js');
const{ prefix, token, giphytoken } = require('./config.json');
const client = new Discord.Client();
const puppeteer = require('puppeteer');


var GphApiClient = require('giphy-js-sdk-core')
giphy = GphApiClient(giphytoken)

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', (receivedMessage) => {
    if (receivedMessage.author == client.user) { // Prevent bot from responding to its own messages
        return
    }
    if (receivedMessage.content.startsWith(prefix)) {
        processCommand(receivedMessage)
    }
})

function processCommand(receivedMessage) {
    let fullCommand = receivedMessage.content.substr(1) // Remove the leading exclamation mark
    let splitCommand = fullCommand.split(" ") // Split the message up in to pieces for each space
    let primaryCommand = splitCommand[0] // The first word directly after the exclamation is the command
    let arguments = splitCommand.slice(1) // All other words are arguments/parameters/options for the command

    if (primaryCommand == "help") {
        helpCommand(arguments, receivedMessage)
    } else if (primaryCommand == "pleasehelp" || primaryCommand == "helpplease") {
        trueHelpCommand(arguments, receivedMessage)
    } else if (primaryCommand == "skribbl") {
        skribblCommand(arguments, receivedMessage)
    } else {
        receivedMessage.channel.send("I don't understand the command. Try `!help` or `!pleasehelp` or `!skribbl`")
    }
}

function helpCommand(arguments, receivedMessage) {
    giphy.search('gifs', {"q": "fuck you"})
        .then((response) => {
        var totalResponses = response.data.length;
        var responseIndex = Math.floor((Math.random() * 10) + 1) % totalResponses;
        var responseFinal = response.data[responseIndex]

        receivedMessage.channel.send("I ain't helpin you, ask nicely :tired_face:", {files: [responseFinal.images.fixed_height.url]})
    })
}

function trueHelpCommand(arguments, receivedMessage) {
    receivedMessage.channel.send("Try `!help` or `!skribbl keywords`")
}

async function skribblCommand(arguments, receivedMessage) {
    if (arguments.length < 1) {
        receivedMessage.channel.send("Gimme something to work with!")
        return
    } else {
        let keyword = ''
        arguments.forEach((word) => {
        keyword = keyword + word.toString() + '%20'
        })
        keyword = keyword.substring(0, keyword.length - 3)
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        await page.goto('https://reversedictionary.org/wordsfor/' + keyword, {waitUntil: 'networkidle2'});
        const customWords = await page.evaluate(() => {
            let rawWords = document.querySelectorAll(".item")
            const rawList = [...rawWords]
            return rawList.map(h => h.innerText)
        })
        await browser.close()

        if (customWords.join() === '') {
            giphy.search('gifs', {"q": "my bad"})
                .then((response) => {
                var totalResponses = response.data.length;
                var responseIndex = Math.floor((Math.random() * 10) + 1) % totalResponses;
                var responseFinal = response.data[responseIndex]
                receivedMessage.channel.send("I'm not very good at finding related words for niche keywords. Please choose a more common one. :upside_down:", {files: [responseFinal.images.fixed_height.url]})
                return
            })
        } else {
            receivedMessage.channel.send(customWords.slice(0, 150).join())
        }
    }
}





client.login(token);