const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let m = [];

rl.question('Введите число цилиндров: ', (n) => {
  (function askVolume(V1) {
    if (V1 > n) {
      calculateAndPrint();
      rl.close();
      return;
    }
    rl.question(`Введите объем цилиндра ${V1}: `, (volume) => {
      m.push(parseFloat(volume));
      askVolume(V1 + 1);
    });
  })(1);
});

function calculateAndPrint() {
  for (let i = 0; i < m.length; i++) {
    const r = Math.pow(m[i], 1 / 3) / Math.pow(2 * Math.PI, 1 / 3);
    const h = m[i] / (Math.PI * Math.pow(r, 2));
    const s = 2 * Math.PI * Math.pow(r, 2) + 2 * Math.PI * r * h;
    console.log(`Площадь поверхности цилиндра ${i + 1}: ${s}`);
  }
}