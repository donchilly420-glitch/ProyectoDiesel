import { useState } from 'react'
import './App.css'

function App() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [token, setToken] = useState(null)
  
  // Estados para manejar las vistas y los datos
  const [view, setView] = useState('home') // 'home' | 'vehiculos' | 'mantenciones'
  const [vehiculos, setVehiculos] = useState([]) // Aquí guardaremos la lista que llegue de Django

  // --- 1. FUNCIÓN DE LOGIN (Igual que antes) ---
  const handleLogin = async (e) => {
    e.preventDefault()
    const datosLogin = { username, password }

    try {
      const respuesta = await fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datosLogin)
      })

      if (respuesta.ok) {
        const data = await respuesta.json()
        setToken(data.token) 
      } else {
        alert("❌ Error: Credenciales incorrectas.")
      }
    } catch (error) {
      console.error("Error:", error)
      alert("⚠️ Error de conexión")
    }
  }

  // --- 2. FUNCIÓN PARA CARGAR VEHÍCULOS ---
  const cargarVehiculos = async () => {
    try {
      // Petición GET al endpoint que vimos en Swagger
      const respuesta = await fetch('http://127.0.0.1:8000/api/vehiculos/', {
        method: 'GET',
        headers: {
          'Authorization': `Token ${token}`, // <--- LA LLAVE MAESTRA
          'Content-Type': 'application/json'
        }
      })

      if (respuesta.ok) {
        const data = await respuesta.json()
        setVehiculos(data) // Guardamos los autos en la memoria
        setView('vehiculos') // Cambiamos la pantalla para mostrar la tabla
      } else {
        alert("Error al cargar vehículos")
      }
    } catch (error) {
      console.error(error)
      alert("Error de conexión con el servidor")
    }
  }

  // --- 3. PANTALLA DE LOGIN ---
  if (!token) {
    return (
      <div style={{ maxWidth: '400px', margin: '0 auto', padding: '2rem' }}>
        <h1>🚚 Taller Diesel</h1>
        <h2>Ingreso de Personal</h2>
        <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <input type="text" placeholder="Usuario" value={username} onChange={(e) => setUsername(e.target.value)} style={{ padding: '10px' }} />
          <input type="password" placeholder="Contraseña" value={password} onChange={(e) => setPassword(e.target.value)} style={{ padding: '10px' }} />
          <button type="submit" style={{ padding: '10px', background: '#007bff', color: 'white', border: 'none', cursor: 'pointer', fontWeight: 'bold' }}>ENTRAR</button>
        </form>
      </div>
    )
  }

  // --- 4. PANEL DE CONTROL (DASHBOARD) ---
  return (
    <div style={{ padding: '2rem', textAlign: 'center', color: 'white' }}>
      
      {/* Barra superior */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h1>🔧 Servicio Diesel</h1>
        <div>
          <span style={{ marginRight: '15px' }}>Hola, <strong>{username}</strong></span>
          <button onClick={() => setToken(null)} style={{ background: '#dc3545', color: 'white', border: 'none', padding: '5px 10px', cursor: 'pointer' }}>Salir</button>
        </div>
      </div>

      {/* VISTA: MENÚ PRINCIPAL */}
      {view === 'home' && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '20px', maxWidth: '800px', margin: '0 auto' }}>
          
          <div 
            onClick={cargarVehiculos} // <--- AL HACER CLIC, CARGA LOS DATOS
            style={{ background: '#333', padding: '40px', borderRadius: '10px', cursor: 'pointer', transition: '0.3s' }}
            className="card-hover"
          >
            <h2 style={{ fontSize: '3rem' }}>🚗</h2>
            <h3>Vehículos</h3>
            <p>Ver listado de flota</p>
          </div>

          <div style={{ background: '#333', padding: '40px', borderRadius: '10px', opacity: 0.5 }}>
            <h2 style={{ fontSize: '3rem' }}>🛠️</h2>
            <h3>Mantenciones</h3>
            <p>(Próximamente)</p>
          </div>

        </div>
      )}

      {/* VISTA: LISTA DE VEHÍCULOS */}
      {view === 'vehiculos' && (
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <button onClick={() => setView('home')} style={{ marginBottom: '20px', background: '#6c757d', color: 'white', border: 'none', padding: '10px 20px', cursor: 'pointer' }}>⬅ Volver</button>
          
          <h2>Flota Registrada</h2>
          
          {vehiculos.length === 0 ? (
            <p>No hay vehículos registrados aún.</p>
          ) : (
            <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '20px', background: '#222' }}>
              <thead>
                <tr style={{ background: '#444' }}>
                  <th style={{ padding: '10px' }}>ID</th>
                  <th style={{ padding: '10px' }}>Datos del Vehículo</th>
                  <th style={{ padding: '10px' }}>Acción</th>
                </tr>
              </thead>
              <tbody>
                {vehiculos.map((auto) => (
                  <tr key={auto.id} style={{ borderBottom: '1px solid #555' }}>
                    <td style={{ padding: '10px' }}>{auto.id}</td>
                    {/* OJO: Aquí muestro todo el objeto para ver qué trae, luego lo arreglamos */}
                    <td style={{ padding: '10px' }}>{JSON.stringify(auto)}</td> 
                    <td style={{ padding: '10px' }}>
                      <button style={{ background: '#28a745', border: 'none', color: 'white', padding: '5px' }}>Ver</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      )}

    </div>
  )
}

export default App