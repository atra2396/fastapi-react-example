import logo from './logo.svg';
import './App.css';
import Component1 from './Component1';
import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
  <BrowserRouter>
    <Routes>
      <Route index element={ <Home/> } />
      <Route path="test" element={ <Test/> } />
    </Routes>
  </BrowserRouter>
  )
}

const Home = () => {
  return (
    <div className="App">
      <nav>
        <Link to="test">Test</Link>
      </nav>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

const Test = () => {
  return <Component1></Component1>
}

export default App;
