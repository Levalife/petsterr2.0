import { USER_LOGGED_IN, USER_LOGGED_OUT } from '../types';
import api from '../api';


// const that equals to function that takes user and returns object with type and user

export const userLoggedIn = (user) => ({
    type: USER_LOGGED_IN,
    user
});

export const userLoggedOut = () => ({
    type: USER_LOGGED_OUT
});

export const login = credentials => dispatch =>
    // make request and then    get user data and dispatch action which will change redux store
    api.user.login(credentials).then(user => {
        localStorage.tokenJWT = user.token;
        dispatch(userLoggedIn(user))
    }); // function which returns another function

export const logout = () => dispatch => {
        localStorage.removeItem('tokenJWT');
        dispatch(userLoggedOut())
    }; // function which returns another function