import React from 'react';

import './App.css';
import {BrowserRouter, Route} from "react-router-dom";
import Products from './admin/Products';
import ProductCreate from './admin/ProductCreate';
import Main from './main/Main';
import ProductEdit from './admin/ProductEdit';

function App() {
  return (
    <div className="App">
      <div>
      <BrowserRouter>
        <Route path='/' exact component={Main} />
        <Route path='/admin/products' exact component={Products} />
        <Route path='/admin/products/create' exact component={ProductCreate} />
        <Route path='/admin/products/:id/edit' exact component={ProductEdit} />
      </BrowserRouter>
      </div>
    </div>
  );
}

export default App;
