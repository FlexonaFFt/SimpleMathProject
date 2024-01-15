class Cylinder {
    constructor(radius, height) {
      this.radius = radius;
      this.height = height;
    }
    getVolume() {
      const radius = this.radius;
      const height = this.height;
      const volume = Math.PI * radius * radius * height;
      return volume.toFixed(4);
    }
  }
  
  function findCylinder() {
    const V1 = parseFloat(document.getElementById("numCylinders").value);
    const r = Math.pow(V1, 1 / 3) / Math.pow(2 * Math.PI, 1 / 3);
    const h = V1 / (Math.PI * r ** 2);
    const s = 2 * Math.PI * r ** 2 + 2 * Math.PI * r * h;
    document.getElementById("output").innerHTML = `Площадь поверхности цилиндра: ${s.toFixed(4)}<br>Радиус основания: ${r.toFixed(4)}, Высота: ${h.toFixed(4)}`;
  }
