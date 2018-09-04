import { USER_LOGGED_IN } from '../types';
import api from '../api';


// const that equals to function that takes user and returns object with type and user

export const userLoggedIn = (user) => ({
    type: USER_LOGGED_IN,
    user
});

export const login = credentials => dispatch =>
    // make request and then    get user data and dispatch action which will change redux store
    api.user.login(credentials).then(user => dispatch(userLoggedIn(user))); // function which returns another function