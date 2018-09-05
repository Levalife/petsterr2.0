import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route } from 'react-router-dom';
import { createStore,applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import thunk from 'redux-thunk';
import { composeWithDevTools} from 'redux-devtools-extension';
import 'semantic-ui-css/semantic.min.css';
import App from './App';
import rootReducer from './rootReducer'
import { userLoggedIn } from './actions/auth'
// import registerServiceWorker from './registerServiceWorker';

const store = createStore(
    rootReducer,
    composeWithDevTools(applyMiddleware(thunk))
);

if (localStorage.tokenJWT) {
    const user = {token: localStorage.tokenJWT};
    store.dispatch(userLoggedIn(user));
}

let myComponent =  document.getElementById('reactify-django-ui');
ReactDOM.render(
    <BrowserRouter>
        <Provider store={store}>
            <Route component={App} />
        </Provider>
    </BrowserRouter>,
    myComponent);
// registerServiceWorker();
