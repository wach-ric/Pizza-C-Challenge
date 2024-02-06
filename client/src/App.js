
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Landing from './components/Landing';
import Restaurant from './components/Restaurant';
import RestaurantPizza from './components/RestaurantPizza';

function App() {
  return (
    <Router>
      <div>
        <Header />
        <main>
          <Routes>
            <Route path="/restaurant_pizzas/new" element={<RestaurantPizza />} />
            <Route path="/restaurants/:id" element={<Restaurant />} />
            <Route path="/" element={<Landing />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
