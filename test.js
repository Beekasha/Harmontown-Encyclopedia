const audio2text = require('audio2text');

const params = {
    url: 'https://storage.googleapis.com/assets.frapp.in/WhatsApp-Ptt-2020-10-16-at-6.02.22-PM.mp3'
}
audio2text.recognize(params).then(transcript => {
	console.log(transcript)
});
