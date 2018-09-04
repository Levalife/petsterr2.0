import { combineReducers } from 'redux';
import user from './reducers/user';


// Reducer is a function that takes state and returns new state
export default combineReducers({
    user
})