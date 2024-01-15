function findCylinder() {
    const numCylinders = document.getElementById('numCylinders').value;
    const cylinders = [];
    document.getElementById('output').innerHTML = '';
  
    for (let i = 1; i <= numCylinders; i++) {
      const cylinderObj = prompt(`Введите объем цилиндра ${i}: `);
      if (cylinderObj === null) {
        break;
      }
      cylinders.push(cylinderObj);
    }
  
    for (let i = 1; i <= numCylinders; i++) {
      const r = Math.pow(cylinders[i - 1], 1 / 3) / (2 * Math.PI) ** (1 / 3);
      const h = cylinders[i - 1] / (Math.PI * r ** 2);
      const s = 2 * Math.PI * r ** 2 + 2 * Math.PI * r * h;
      document.getElementById('output').innerHTML += `Площадь поверхности цилиндра ${i}: ${s}<br> Радиус основания: ${r.toFixed(4)}, Высота: ${h.toFixed(4)}<br>`;
    }
  }
