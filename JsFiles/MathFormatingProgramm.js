function findCylinder() {
  const numCylinders = document.getElementById('numCylinders').value;
  const cylinders = [];

  for (let i = 0; i < numCylinders; i++) {
    const radius = prompt(`Введите радиус основания цилиндра ${i + 1}:`);
    const height = prompt(`Введите высоту цилиндра ${i + 1}:`);
    const volume = Math.PI * (radius ** 2) * height;
    // const lateralSurfaceArea = 2 * Math.PI * radius * (radius + height);
    // const totalSurfaceArea = lateralSurfaceArea + 2 * (Math.PI * (radius ** 2));
    // const lateralSurfaceArea = 2 * Math.PI * radius * height;
    // const groundsSurfaceArea = 2 * Math.PI * radius;
    // const totalSurfaceArea = lateralSurfaceArea + 2 * groundsSurfaceArea;
    const totalSurfaceArea = 2 * Math.PI * (radius ** 2) + 2 * Math.PI * radius * height;
    // cylinders.push({ radius, height, volume, lateralSurfaceArea, groundsSurfaceArea, totalSurfaceArea });
    cylinders.push({ radius, height, volume, totalSurfaceArea });
  }

  const minSurfaceAreaCylinder = cylinders.reduce((min, cylinder) => cylinder.totalSurfaceArea < min.totalSurfaceArea ? cylinder : min, cylinders[0]);
  document.getElementById('output').innerText = `Цилиндр имеет: 
    Радиус: ${minSurfaceAreaCylinder.radius}, 
    Высота: ${minSurfaceAreaCylinder.height}, 
    Объём: ${minSurfaceAreaCylinder.volume},
    Площадь полной поверхности цилиндра: ${minSurfaceAreaCylinder.totalSurfaceArea}`;
}

// Площадь боковой поверхности: ${minSurfaceAreaCylinder.lateralSurfaceArea},
// Площадь поверхности основания: ${minSurfaceAreaCylinder.groundsSurfaceArea},