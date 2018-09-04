import React from 'react';
import {Component} from 'react';
import LoginForm from '../forms/LoginForm';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { login } from '../../actions/auth';

class LoginPage extends Component {
    // login after which                      redirect to homepage
    submit = (data) => this.props.login(data).then(() => this.props.history.push('/'));

    render() {
        return (
        <div>
            <h1>Login Page</h1>
            <LoginForm submit={this.submit}/>
        </div>
    )
    }
}

LoginPage.propTypes = {
    history: PropTypes.shape({
        push: PropTypes.func.isRequired
    }).isRequired,
    login: PropTypes.func.isRequired
};

export default connect(null, { login })(LoginPage);