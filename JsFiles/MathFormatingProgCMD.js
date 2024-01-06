const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function findCylinderWithMinSurfaceArea(numCylinders) {
  const cylinders = [];
  let i = 0;
  const askForCylinderData = () => {
    rl.question(`Введите данные для цилиндра ${i + 1}:\nРадиус окружности: `, (radius) => {
      rl.question("Высота окружности: ", (height) => {
        const volume = Math.PI * (radius ** 2) * height;
        const lateralSurfaceArea = 2 * Math.PI * radius * (radius + height);
        const totalSurfaceArea = lateralSurfaceArea + volume;
        cylinders.push({ radius, height, volume, lateralSurfaceArea, totalSurfaceArea });
        i++;
        if (i < numCylinders) {
          askForCylinderData();
        } else {
          const minSurfaceAreaCylinder = cylinders.reduce((min, cylinder) => cylinder.totalSurfaceArea < min.totalSurfaceArea ? cylinder : min, cylinders[0]);
          console.log("Цилиндр, с минимальной площадью поверхности (r, h, min_surf): ", minSurfaceAreaCylinder);
          rl.close();
        }
      });
    });
  };
  askForCylinderData();
}

rl.question("Введите количество цилиндров: ", (numCylinders) => {
  findCylinderWithMinSurfaceArea(parseInt(numCylinders));
});