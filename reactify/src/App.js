import React, {Component} from 'react';
import {BrowserRouter, Route, Redirect, Switch} from 'react-router-dom';
import PropTypes from 'prop-types';
import HomePage from './components/pages/HomePage';
import LoginPage from './components/pages/LoginPage';
import SignupPage from './components/pages/SignupPage';
import DashboardPage from './components/pages/DashboardPage';
import ForgotPasswordPage from './components/pages/ForgotPasswordPage';
import ResetPasswordPage from './components/pages/ResetPasswordPage';
import UserRoute from './components/routes/UserRoute';
import GuestRoute from './components/routes/GuestRoute';

const App = ({ location}) => <div className="ui container">
    <Route location={location} path="/" exact component={HomePage} />
    <GuestRoute location={location} path="/login" exact component={LoginPage} />
    <GuestRoute location={location} path="/signup" exact component={SignupPage} />
    <GuestRoute location={location} path="/forgot_password" exact component={ForgotPasswordPage} />
    <GuestRoute location={location} path="/reset_password/:token" exact component={ResetPasswordPage} />
    <UserRoute
        location={location}
        path="/dashboard"
        exact
        component={DashboardPage}
    />
</div>;

App.propTypes= {
    location: PropTypes.shape({
        pathname: PropTypes.string.isRequired
    }).isRequired,
};

//import Kennels from './kennels/Kennels';
// import KennelDetail from './kennels/KennelDetail';
// import KennelForm from './kennels/KennelForm';
// import IndexPage from "./web/IndexPage";
// import LoginForm from "./web/LoginForm";
// import TopMenu from "./web/TopMenu";

// class App extends Component {
//     render() {
//         return (
//             <BrowserRouter>
//                 <Switch>
//                     <Route exact path='/login' component={LoginForm} />
//                     <Route exact path='/kennels' component={Kennels} />
//                     <Route exact path='/kennels/create' component={KennelForm} />
//                     <Route exact path='/kennels/:slug' component={KennelDetail} />
//
//
//                     <Route component={TopMenu}/>
//                     <Route component={IndexPage}/>
//                     {/*<Route component={Kennels}/>*/}
//                 </Switch>
//             </BrowserRouter>
//             // <Kennels />
//
//         );
//     }
// }

    export default App;
