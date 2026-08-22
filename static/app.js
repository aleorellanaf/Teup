async function acortar() {
  const url = document.getElementById('urlInput').value;
  const resultadoDiv = document.getElementById('resultadoDiv');
  
  if(!url) {
    alert("Por favor, ingresa una URL larga primero.");
    return;
  }

  try {
    const res = await fetch('/acortar', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({url_larga: url})
    });
    
    const data = await res.json();
    
    if(res.ok) {
      resultadoDiv.style.display = "block";
      resultadoDiv.innerHTML = `Enlace acortado:<br><a href="${data.url_corta}" target="_blank">${data.url_corta}</a>`;
    } else {
      alert("Hubo un problema: " + data.detail);
    }
  } catch (error) {
    alert("Error de conexión con el servidor.");
  }
}

function borrar() {
  document.getElementById('urlInput').value = "";
  const resultadoDiv = document.getElementById('resultadoDiv');
  resultadoDiv.style.display = "none";
  resultadoDiv.innerHTML = "";
}