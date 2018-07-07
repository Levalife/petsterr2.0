import React, {Component} from 'react';
import {BrowserRouter, Route, Redirect, Switch} from 'react-router-dom';
import './App.css';

import Kennels from './kennels/Kennels';
import KennelDetail from  './kennels/KennelDetail';
import KennelForm from './kennels/KennelForm';
import IndexPage from "./web/IndexPage";
import LoginForm from "./web/LoginForm";

class App extends Component {
    render() {
        return (
            <BrowserRouter>
                <Switch>
                    <Route exact path='/login' component={LoginForm} />
                    <Route exact path='/kennels' component={Kennels} />
                    <Route exact path='/kennels/create' component={KennelForm} />
                    <Route exact path='/kennels/:slug' component={KennelDetail} />
                    <Route component={IndexPage}/>
                    {/*<Route component={Kennels}/>*/}
                </Switch>
            </BrowserRouter>
            // <Kennels />

        );
    }
}

export default App;
