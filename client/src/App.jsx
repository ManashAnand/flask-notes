
import axios from 'axios'
import './App.css'

function App() {

  const handleBtn = async () => {
    const res = await axios.get('http://localhost:5000/');
    console.log(res)
  }
  const handleBtn2 = async () => {
    const name="manash"
    const res = await axios.get('http://localhost:5000/'+name);
    console.log(res)
  }

  return (
    <>
        <button onClick={handleBtn}>getData</button>
        <button onClick={handleBtn2}>getDataVariable</button>
    </>
  )
}

export default App
