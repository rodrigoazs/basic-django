import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import AddProduct from "./components/add-product.component";
import Product from "./components/product.component";
import ProductsList from "./components/products-list.component";

function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <Link to={"/products"} className="navbar-brand">
          Basic
        </Link>
        <div className="navbar-nav mr-auto">
          <li className="nav-item">
            <Link to={"/products"} className="nav-link">
              Products
            </Link>
          </li>
          <li className="nav-item">
            <Link to={"/add"} className="nav-link">
              Create
            </Link>
          </li>
        </div>
      </nav>

      <div className="container mt-3">
        <Switch>
          <Route exact path={["/", "/products"]} component={ProductsList} />
          <Route exact path="/add" component={AddProduct} />
          <Route path="/products/:id" component={Product} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
