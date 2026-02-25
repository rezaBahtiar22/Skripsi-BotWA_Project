const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal'); // qrcode
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        headless: true, // false kalau mau lihat browser-nya
        args: ['--no-sandbox']
    }
});

const ML_API_URL = 'http://127.0.0.1:5000/predict';

// Fungsi simpan pesan ke file log
function simpanKeDataset(message, label) {
    const logFolder = path.join(__dirname, 'logs');
    const logFile = path.join(logFolder, 'log_pesan.csv');

    if (!fs.existsSync(logFolder)) {
        fs.mkdirSync(logFolder, { recursive: true });
    }

    const baris = `"${message.replace(/"/g, '""')}","${label}"\n`;

    fs.appendFile(logFile, baris, (err) => {
        if (err) {
            console.error('❌ Gagal menyimpan pesan ke log:', err.message);
        } else {
            console.log('📁 Pesan disimpan ke log_pesan.csv');
        }
    });
}

client.on('qr', (qr) => {
    qrcode.generate(qr, { small: true }); // Tampilkan QR di terminal dalam bentuk ASCII
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('authenticated', () => {
    console.log('✅ Client authenticated');
});

client.on('auth_failure', msg => {
    console.error('❌ AUTH ERROR', msg);
});

client.on('disconnected', reason => {
    console.log('⚠️ Disconnected', reason);
});

client.on('message', async message => {
    try {
        const userMessage = message.body;
        console.log('📩 Pesan diterima:', userMessage);

        const response = await axios.post(ML_API_URL, {
            message: userMessage
        });

        
        const label = response.data.label;
        console.log(response.data);

        // simpan data ke log
        if (label !== 'Normal') {
            simpanKeDataset(userMessage, label);
        }

        if (label === 'Penipuan') {
        try {
            await message.reply('🚨 Pesan ini terindikasi sebagai *PENIPUAN*! Harap berhati-hati!');
        } catch (e) {
            // console.error('❌ Gagal membalas pesan penipuan:', e.message);
        }
    } else if (label === 'Promosi') {
        try {
            await message.reply('📢 Pesan ini terindikasi sebagai *promosi*.');
        } catch (e) {
            // console.error('❌ Gagal membalas pesan promosi:', e.message);
        }
    }

    } catch (error) {
        console.error('❌ Gagal menghubungi model:', error.message);
        await message.reply('⚠️ Terjadi kesalahan saat mengecek pesan.');
    }
});

client.initialize();