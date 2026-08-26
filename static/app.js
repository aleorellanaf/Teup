let enlaceCorto = "";

async function acortar() {
  const inputUrl = document.getElementById('urlInput').value;
  
  if (!inputUrl) return alert("Ingresa una URL larga primero.");

  try {
    // Envía la URL larga al servidor mediante una petición POST
    const respuesta = await fetch('/acortar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url_larga: inputUrl })
    });
    
    const datos = await respuesta.json();
    
    if (respuesta.ok) {
      enlaceCorto = datos.url_corta;
      
      // Muestra el enlace limpio (ocultando el protocolo en pantalla)
      document.getElementById('shortUrlText').innerText = enlaceCorto.replace('http://', '');
      
      // Hace visible la caja de resultados
      document.getElementById('resultadoDiv').style.display = "block";
    } else {
      alert("Error: " + datos.detail);
    }
  } catch (error) {
    alert("Error de conexión con el servidor.");
  }
}

function copiarUrl() {
  // Copia el enlace corto al portapapeles del dispositivo
  navigator.clipboard.writeText(enlaceCorto);
  alert("¡Enlace copiado!");
}

function irUrl() {
  // Abre el enlace corto en una nueva pestaña del navegador
  window.open(enlaceCorto, '_blank');
}