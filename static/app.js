let enlaceCorto = "";

async function acortar() {
  const inputUrl = document.getElementById('urlInput').value;
  
  if (!inputUrl) return alert("Ingresa una URL larga primero.");

  try {
    const respuesta = await fetch('/acortar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url_larga: inputUrl })
    });
    
    const datos = await respuesta.json();
    
    if (respuesta.ok) {
      enlaceCorto = datos.url_corta;
      
      // Muestra el link sin el "http://" para que se vea más limpio
      document.getElementById('shortUrlText').innerText = enlaceCorto.replace('http://', '');
      
      // Hace visible la caja punteada
      document.getElementById('resultadoDiv').style.display = "block";
    } else {
      alert("Error: " + datos.detail);
    }
  } catch (error) {
    alert("Error de conexión con el servidor.");
  }
}

function copiarUrl() {
  navigator.clipboard.writeText(enlaceCorto);
  alert("¡Enlace copiado!");
}

function irUrl() {
  window.open(enlaceCorto, '_blank');
}